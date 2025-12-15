#!/usr/bin/env -S uv run --script
# /// script
# dependencies = ["pyyaml"]
# requires-python = ">=3.12"
# ///

"""
Transfer markdown files from Claude Code plugin folders to OpenCode and Cursor formats,
transforming frontmatter to each platform's syntax.

Source directories:
- claude-maratai-dev/agents/ -> opencode/agent/
- claude-maratai-dev/commands/ -> opencode/command/
- claude-maratai-manager/commands/ -> opencode/command/
- claude-maratai-manager/skills/ -> .cursor/rules/

OpenCode Transformations:
- Agents: Remove name/model/tools fields, add mode: subagent
- Commands: Keep description field

Cursor Transformations:
- Skills: Remove name, keep description, add alwaysApply: false
- Replace ${CLAUDE_PLUGIN_ROOT}/skills/<skill>/ with .cursor/rules/<skill>/
- Copy scripts/ directory alongside RULE.md
"""

import shutil
import yaml
from pathlib import Path


def prompt_delete(file_path: Path, target_root: Path) -> bool:
    """
    Prompt user to confirm deletion of orphan file.
    Returns True if user confirms deletion, False otherwise.
    """
    rel_path = file_path.relative_to(target_root)
    while True:
        response = input(f"  Delete orphan '{rel_path}'? [y/n]: ").strip().lower()
        if response in ('y', 'yes'):
            return True
        elif response in ('n', 'no'):
            return False
        print("  Please enter 'y' or 'n'")


def parse_frontmatter(content: str) -> tuple[dict, str]:
    """
    Parse YAML frontmatter from markdown content.

    Returns tuple of (metadata dict, body content).
    If no frontmatter, returns empty dict and full content.
    """
    content = content.lstrip()
    if not content.startswith('---'):
        return {}, content

    # Find the closing ---
    lines = content.split('\n')
    end_idx = None
    for i, line in enumerate(lines[1:], start=1):
        if line.strip() == '---':
            end_idx = i
            break

    if end_idx is None:
        return {}, content

    # Parse YAML
    yaml_content = '\n'.join(lines[1:end_idx])
    try:
        metadata = yaml.safe_load(yaml_content) or {}
    except yaml.YAMLError:
        metadata = {}

    # Get body (skip the closing --- and any immediate newline)
    body = '\n'.join(lines[end_idx + 1:])
    body = body.lstrip('\n')

    return metadata, body


def generate_opencode_preamble(metadata: dict, file_type: str) -> str:
    """
    Generate OpenCode-compliant YAML frontmatter.

    Args:
        metadata: Parsed source metadata dict
        file_type: 'agent' or 'command'

    Returns:
        OpenCode-compliant frontmatter string (including --- markers)
    """
    opencode_meta = {}

    # Always keep description
    if 'description' in metadata:
        opencode_meta['description'] = metadata['description']

    # Agent-specific fields
    if file_type == 'agent':
        opencode_meta['mode'] = 'subagent'

    # Command-specific fields (keep agent if present in source, though Claude Code doesn't use it)
    if file_type == 'command' and 'agent' in metadata:
        opencode_meta['agent'] = metadata['agent']

    if not opencode_meta:
        return ''

    # Generate YAML with proper formatting
    yaml_str = yaml.dump(opencode_meta, default_flow_style=False, allow_unicode=True, sort_keys=False)
    return f"---\n{yaml_str}---\n"


def get_file_type(relative_path: Path) -> str | None:
    """
    Determine if file is an agent or command based on its path.

    Returns 'agent', 'command', or None if neither.
    """
    parts = relative_path.parts
    if not parts:
        return None

    first_dir = parts[0]
    if first_dir in ('agents', 'agent'):
        return 'agent'
    elif first_dir in ('commands', 'command'):
        return 'command'
    return None


def get_target_path(source_path: Path, source_root: Path, target_root: Path) -> Path:
    """
    Convert source path to target path, mapping folder names:
    - agents -> agent
    - commands -> command
    """
    relative_path = source_path.relative_to(source_root)
    parts = list(relative_path.parts)

    # Map folder names
    if parts and parts[0] == 'agents':
        parts[0] = 'agent'
    elif parts and parts[0] == 'commands':
        parts[0] = 'command'

    return target_root / Path(*parts)


def get_source_configs(project_root: Path) -> list[tuple[Path, str]]:
    """
    Get all source directories and their types.

    Returns list of (source_path, folder_type) tuples where folder_type is 'agents' or 'commands'.
    """
    sources = []

    # claude-maratai-dev
    dev_root = project_root / "claude-maratai-dev"
    if dev_root.exists():
        agents_dir = dev_root / "agents"
        commands_dir = dev_root / "commands"
        if agents_dir.exists():
            sources.append((agents_dir, 'agents'))
        if commands_dir.exists():
            sources.append((commands_dir, 'commands'))

    # claude-maratai-manager
    manager_root = project_root / "claude-maratai-manager"
    if manager_root.exists():
        commands_dir = manager_root / "commands"
        if commands_dir.exists():
            sources.append((commands_dir, 'commands'))

    return sources


def transfer_file(source_file: Path, target_file: Path, file_type: str) -> bool:
    """
    Transfer a single file, transforming frontmatter.

    Returns True if successful, False otherwise.
    """
    try:
        content = source_file.read_text(encoding='utf-8')
    except Exception as e:
        print(f"  Error reading {source_file}: {e}")
        return False

    # Parse source frontmatter
    metadata, body = parse_frontmatter(content)

    # Generate OpenCode preamble
    preamble = generate_opencode_preamble(metadata, file_type)

    # Combine preamble and body
    new_content = preamble + body

    # Ensure target directory exists
    target_file.parent.mkdir(parents=True, exist_ok=True)

    # Write to target
    try:
        target_file.write_text(new_content, encoding='utf-8')
        return True
    except Exception as e:
        print(f"  Error writing {target_file}: {e}")
        return False


def cleanup_orphans(target_root: Path, valid_targets: set[Path]) -> int:
    """
    Remove files in target that don't have corresponding sources.

    Returns number of files removed.
    """
    removed = 0

    # Check agent and command directories
    for subdir in ['agent', 'command']:
        dir_path = target_root / subdir
        if not dir_path.exists():
            continue

        for target_file in dir_path.rglob("*.md"):
            if target_file not in valid_targets:
                if prompt_delete(target_file, target_root):
                    try:
                        target_file.unlink()
                        print(f"  Removed: {target_file.relative_to(target_root)}")
                        removed += 1
                    except Exception as e:
                        print(f"  Error removing {target_file}: {e}")
                else:
                    print(f"  Skipped: {target_file.relative_to(target_root)}")

        # Clean up empty directories
        for dir_to_check in sorted(dir_path.rglob("*"), reverse=True):
            if dir_to_check.is_dir() and not any(dir_to_check.iterdir()):
                try:
                    dir_to_check.rmdir()
                except Exception:
                    pass

    return removed


# =============================================================================
# Cursor Rules Functions
# =============================================================================


def generate_cursor_frontmatter(metadata: dict) -> str:
    """
    Generate Cursor-compliant YAML frontmatter for RULE.md.

    Transformations:
    - Remove: name field
    - Keep: description field
    - Add: alwaysApply: false
    """
    cursor_meta = {}

    if 'description' in metadata:
        cursor_meta['description'] = metadata['description']

    cursor_meta['alwaysApply'] = False

    yaml_str = yaml.dump(cursor_meta, default_flow_style=False, allow_unicode=True, sort_keys=False)
    return f"---\n{yaml_str}---\n"


def transform_cursor_body(body: str, skill_name: str) -> str:
    """
    Transform script paths in body for Cursor rules.

    Replace ${CLAUDE_PLUGIN_ROOT}/skills/<skill> with .cursor/rules/<skill>
    """
    old_path = f"${{CLAUDE_PLUGIN_ROOT}}/skills/{skill_name}"
    new_path = f".cursor/rules/{skill_name}"
    return body.replace(old_path, new_path)


def get_skill_sources(project_root: Path) -> list[tuple[Path, str]]:
    """
    Get all skill directories.

    Returns list of (skill_path, skill_name) tuples.
    """
    skills = []

    # claude-maratai-manager/skills/
    manager_root = project_root / "claude-maratai-manager"
    if manager_root.exists():
        skills_dir = manager_root / "skills"
        if skills_dir.exists():
            for skill_path in skills_dir.iterdir():
                if skill_path.is_dir() and (skill_path / "SKILL.md").exists():
                    skills.append((skill_path, skill_path.name))

    # claude-maratai-dev/skills/ (if exists in future)
    dev_root = project_root / "claude-maratai-dev"
    if dev_root.exists():
        skills_dir = dev_root / "skills"
        if skills_dir.exists():
            for skill_path in skills_dir.iterdir():
                if skill_path.is_dir() and (skill_path / "SKILL.md").exists():
                    skills.append((skill_path, skill_path.name))

    return skills


def transfer_cursor_skill(
    skill_path: Path,
    skill_name: str,
    target_root: Path,
    project_root: Path
) -> tuple[int, int, set[Path]]:
    """
    Transfer a skill to Cursor rules format.

    Returns (transferred_count, skipped_count, valid_targets set).
    """
    transferred = 0
    skipped = 0
    valid_targets: set[Path] = set()

    target_skill_dir = target_root / skill_name
    source_skill_md = skill_path / "SKILL.md"
    target_rule_md = target_skill_dir / "RULE.md"

    valid_targets.add(target_rule_md)

    # Read and transform SKILL.md -> RULE.md
    try:
        content = source_skill_md.read_text(encoding='utf-8')
    except Exception as e:
        print(f"  Error reading {source_skill_md}: {e}")
        return 0, 1, valid_targets

    metadata, body = parse_frontmatter(content)
    new_frontmatter = generate_cursor_frontmatter(metadata)
    new_body = transform_cursor_body(body, skill_name)
    new_content = new_frontmatter + new_body

    # Check if RULE.md needs update
    needs_update = True
    if target_rule_md.exists():
        try:
            existing_content = target_rule_md.read_text(encoding='utf-8')
            if existing_content == new_content:
                needs_update = False
        except Exception:
            pass

    if needs_update:
        target_skill_dir.mkdir(parents=True, exist_ok=True)
        try:
            target_rule_md.write_text(new_content, encoding='utf-8')
            rel_source = source_skill_md.relative_to(project_root)
            rel_target = target_rule_md.relative_to(target_root)
            print(f"  Transferred: {rel_source} -> {rel_target}")
            transferred += 1
        except Exception as e:
            print(f"  Error writing {target_rule_md}: {e}")
            skipped += 1
    else:
        skipped += 1

    # Copy scripts/ directory if exists
    source_scripts = skill_path / "scripts"
    target_scripts = target_skill_dir / "scripts"

    if source_scripts.exists() and source_scripts.is_dir():
        # Track all script files as valid targets
        for script_file in source_scripts.rglob("*"):
            if script_file.is_file():
                rel_path = script_file.relative_to(source_scripts)
                target_file = target_scripts / rel_path
                valid_targets.add(target_file)

                # Check if script needs update
                script_needs_update = True
                if target_file.exists():
                    try:
                        source_content = script_file.read_bytes()
                        target_content = target_file.read_bytes()
                        if source_content == target_content:
                            script_needs_update = False
                    except Exception:
                        pass

                if script_needs_update:
                    target_file.parent.mkdir(parents=True, exist_ok=True)
                    try:
                        shutil.copy2(script_file, target_file)
                        rel_source = script_file.relative_to(project_root)
                        rel_target = target_file.relative_to(target_root)
                        print(f"  Copied: {rel_source} -> {rel_target}")
                        transferred += 1
                    except Exception as e:
                        print(f"  Error copying {script_file}: {e}")
                        skipped += 1
                else:
                    skipped += 1

    return transferred, skipped, valid_targets


def cleanup_cursor_orphans(target_root: Path, valid_targets: set[Path]) -> int:
    """
    Remove files in .cursor/rules/ that don't have corresponding sources.

    Returns number of files removed.
    """
    removed = 0

    if not target_root.exists():
        return 0

    # Find all files in target
    for target_file in target_root.rglob("*"):
        if target_file.is_file() and target_file not in valid_targets:
            if prompt_delete(target_file, target_root):
                try:
                    target_file.unlink()
                    print(f"  Removed: {target_file.relative_to(target_root)}")
                    removed += 1
                except Exception as e:
                    print(f"  Error removing {target_file}: {e}")
            else:
                print(f"  Skipped: {target_file.relative_to(target_root)}")

    # Clean up empty directories
    for dir_to_check in sorted(target_root.rglob("*"), reverse=True):
        if dir_to_check.is_dir() and not any(dir_to_check.iterdir()):
            try:
                dir_to_check.rmdir()
            except Exception:
                pass

    return removed


def transfer_opencode(project_root: Path) -> tuple[int, int, int]:
    """
    Transfer Claude Code files to OpenCode format.

    Returns (transferred, skipped, removed) counts.
    """
    target_root = project_root / "opencode"

    print("=" * 60)
    print("Transfer Claude Code -> OpenCode")
    print("=" * 60)
    print(f"Target: {target_root}")
    print()

    if not target_root.exists():
        print(f"Creating target directory: {target_root}")
        target_root.mkdir(parents=True, exist_ok=True)

    # Get all source directories
    sources = get_source_configs(project_root)
    if not sources:
        print("No source directories found!")
        return 0, 0, 0

    print(f"Found {len(sources)} source directories")
    print()

    # Track all valid target files for orphan cleanup
    valid_targets: set[Path] = set()

    # Process each source
    transferred = 0
    skipped = 0

    for source_dir, folder_type in sources:
        file_type = 'agent' if folder_type == 'agents' else 'command'
        parent_name = source_dir.parent.name

        print(f"--- {parent_name}/{folder_type} ---")

        md_files = list(source_dir.rglob("*.md"))
        if not md_files:
            print("  No .md files found")
            continue

        for source_file in md_files:
            # Calculate target path
            relative_to_parent = source_file.relative_to(source_dir.parent)
            target_file = get_target_path(
                source_dir.parent / relative_to_parent,
                source_dir.parent,
                target_root
            )

            valid_targets.add(target_file)

            # Check if content changed
            needs_update = True
            if target_file.exists():
                try:
                    # Parse both files to compare
                    source_content = source_file.read_text(encoding='utf-8')
                    source_meta, source_body = parse_frontmatter(source_content)
                    expected_preamble = generate_opencode_preamble(source_meta, file_type)
                    expected_content = expected_preamble + source_body

                    target_content = target_file.read_text(encoding='utf-8')
                    if target_content == expected_content:
                        needs_update = False
                except Exception:
                    pass

            if needs_update:
                if transfer_file(source_file, target_file, file_type):
                    rel_source = source_file.relative_to(project_root)
                    rel_target = target_file.relative_to(target_root)
                    print(f"  Transferred: {rel_source} -> {rel_target}")
                    transferred += 1
                else:
                    skipped += 1
            else:
                skipped += 1

        print()

    # Cleanup orphans
    print("--- Cleanup ---")
    removed = cleanup_orphans(target_root, valid_targets)
    if removed == 0:
        print("  No orphans found")
    print()

    return transferred, skipped, removed


def transfer_cursor(project_root: Path) -> tuple[int, int, int]:
    """
    Transfer Claude Code skills to Cursor rules format.

    Returns (transferred, skipped, removed) counts.
    """
    target_root = project_root / ".cursor" / "rules"

    print("=" * 60)
    print("Transfer Claude Code -> Cursor Rules")
    print("=" * 60)
    print(f"Target: {target_root}")
    print()

    # Get all skill directories
    skills = get_skill_sources(project_root)
    if not skills:
        print("No skills found!")
        return 0, 0, 0

    print(f"Found {len(skills)} skill(s)")
    print()

    # Track all valid target files for orphan cleanup
    all_valid_targets: set[Path] = set()

    # Process each skill
    total_transferred = 0
    total_skipped = 0

    for skill_path, skill_name in skills:
        print(f"--- {skill_name} ---")

        transferred, skipped, valid_targets = transfer_cursor_skill(
            skill_path, skill_name, target_root, project_root
        )

        total_transferred += transferred
        total_skipped += skipped
        all_valid_targets.update(valid_targets)

        print()

    # Cleanup orphans
    print("--- Cleanup ---")
    removed = cleanup_cursor_orphans(target_root, all_valid_targets)
    if removed == 0:
        print("  No orphans found")
    print()

    return total_transferred, total_skipped, removed


def main():
    project_root = Path(__file__).parent

    # Transfer to OpenCode
    oc_transferred, oc_skipped, oc_removed = transfer_opencode(project_root)

    # Transfer to Cursor
    cursor_transferred, cursor_skipped, cursor_removed = transfer_cursor(project_root)

    # Final summary
    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"OpenCode: {oc_transferred} transferred, {oc_skipped} unchanged, {oc_removed} removed")
    print(f"Cursor:   {cursor_transferred} transferred, {cursor_skipped} unchanged, {cursor_removed} removed")
    print("=" * 60)


if __name__ == "__main__":
    main()
