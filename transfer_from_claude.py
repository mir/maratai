#!/usr/bin/env -S uv run --script
# /// script
# dependencies = ["pyyaml"]
# requires-python = ">=3.12"
# ///

"""
Transfer markdown files from Claude Code plugin folders to OpenCode format,
transforming frontmatter to OpenCode's syntax.

Source directories:
- claude-maratai-dev/agents/ -> ${OPENCODE_DIR}/agent/
- claude-maratai-dev/commands/ -> ${OPENCODE_DIR}/command/
- claude-maratai-manager/commands/ -> ${OPENCODE_DIR}/command/
- claude-maratai-manager/skills/ -> ${OPENCODE_DIR}/skill/

OpenCode Transformations:
- Agents: Remove name/model/tools fields, add mode: subagent
- Commands: Keep description field
- Skills: Keep SKILL.md as-is, copy scripts/ and references/ folders
- Replace ${CLAUDE_PLUGIN_ROOT}/skills/<skill>/ with ${OPENCODE_DIR}/skill/<skill>/
"""

import shutil
import yaml
from pathlib import Path
from typing import Callable


# =============================================================================
# Utility Functions
# =============================================================================


def file_needs_update(source_content: bytes | str, target_path: Path, is_text: bool = False) -> bool:
    """Return True if target doesn't exist or content differs."""
    if not target_path.exists():
        return True
    try:
        if is_text:
            return target_path.read_text(encoding='utf-8') != source_content
        return target_path.read_bytes() != source_content
    except Exception:
        return True


def copy_file_with_logging(
    source: Path,
    target: Path,
    project_root: Path,
    target_root: Path
) -> bool:
    """Copy file and log. Returns True if successful."""
    target.parent.mkdir(parents=True, exist_ok=True)
    try:
        shutil.copy2(source, target)
        print(f"  Copied: {source.relative_to(project_root)} -> {target.relative_to(target_root)}")
        return True
    except Exception as e:
        print(f"  Error copying {source}: {e}")
        return False


def write_text_with_logging(
    content: str,
    target: Path,
    source: Path,
    project_root: Path,
    target_root: Path,
    action: str = "Transferred"
) -> bool:
    """Write text file and log. Returns True if successful."""
    target.parent.mkdir(parents=True, exist_ok=True)
    try:
        target.write_text(content, encoding='utf-8')
        print(f"  {action}: {source.relative_to(project_root)} -> {target.relative_to(target_root)}")
        return True
    except Exception as e:
        print(f"  Error writing {target}: {e}")
        return False


def copy_directory_if_changed(
    source_dir: Path,
    target_dir: Path,
    project_root: Path,
    target_root: Path,
    exclude: list[str] | None = None
) -> tuple[int, int, set[Path]]:
    """
    Copy directory contents, skipping unchanged files.
    Returns (transferred_count, skipped_count, valid_target_paths).
    """
    transferred = 0
    skipped = 0
    valid_targets: set[Path] = set()
    exclude = exclude or []

    if not source_dir.exists() or not source_dir.is_dir():
        return transferred, skipped, valid_targets

    for source_file in source_dir.rglob("*"):
        if not source_file.is_file():
            continue

        if any(pattern in source_file.parts for pattern in exclude):
            continue

        rel_path = source_file.relative_to(source_dir)
        target_file = target_dir / rel_path
        valid_targets.add(target_file)

        try:
            source_content = source_file.read_bytes()
        except Exception as e:
            print(f"  Error reading {source_file}: {e}")
            skipped += 1
            continue

        if file_needs_update(source_content, target_file):
            if copy_file_with_logging(source_file, target_file, project_root, target_root):
                transferred += 1
            else:
                skipped += 1
        else:
            skipped += 1

    return transferred, skipped, valid_targets


def cleanup_orphan_files(
    search_root: Path,
    valid_targets: set[Path],
    display_root: Path
) -> int:
    """Remove files not in valid_targets, clean empty dirs. Returns count removed."""
    removed = 0

    if not search_root.exists():
        return 0

    for target_file in search_root.rglob("*"):
        if target_file.is_file() and target_file not in valid_targets:
            if prompt_delete(target_file, display_root):
                try:
                    target_file.unlink()
                    print(f"  Removed: {target_file.relative_to(display_root)}")
                    removed += 1
                except Exception as e:
                    print(f"  Error removing {target_file}: {e}")
            else:
                print(f"  Skipped: {target_file.relative_to(display_root)}")

    for dir_to_check in sorted(search_root.rglob("*"), reverse=True):
        if dir_to_check.is_dir() and not any(dir_to_check.iterdir()):
            try:
                dir_to_check.rmdir()
            except Exception:
                pass

    return removed


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

    metadata, body = parse_frontmatter(content)
    preamble = generate_opencode_preamble(metadata, file_type)
    new_content = preamble + body

    target_file.parent.mkdir(parents=True, exist_ok=True)
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
# Skill Transfer Functions
# =============================================================================


def transform_opencode_skill_body(body: str, skill_name: str) -> str:
    """Replace ${CLAUDE_PLUGIN_ROOT}/skills/<skill> with ${OPENCODE_DIR}/skill/<skill>"""
    old_path = f"${{CLAUDE_PLUGIN_ROOT}}/skills/{skill_name}"
    new_path = f"${{OPENCODE_DIR}}/skill/{skill_name}"
    return body.replace(old_path, new_path)


def transfer_skill(
    skill_path: Path,
    skill_name: str,
    target_root: Path,
    project_root: Path,
    *,
    target_subdir: str | None,
    target_filename: str,
    frontmatter_fn: Callable[[dict, str], str],
    body_transform_fn: Callable[[str, str], str],
    subdirs: list[str]
) -> tuple[int, int, set[Path]]:
    """
    Transfer a skill to target format.

    Args:
        skill_path: Source skill directory
        skill_name: Name of the skill
        target_root: Root target directory
        project_root: Project root for relative paths
        target_subdir: Subdirectory under target_root (e.g., "skill" for OpenCode, None for Cursor)
        target_filename: Output filename (e.g., "SKILL.md" or "RULE.md")
        frontmatter_fn: Function to generate frontmatter from metadata
        body_transform_fn: Function to transform body content
        subdirs: List of subdirectories to copy (e.g., ["scripts", "references"])

    Returns (transferred_count, skipped_count, valid_targets set).
    """
    transferred = 0
    skipped = 0
    valid_targets: set[Path] = set()

    # Build target directory path
    if target_subdir:
        target_skill_dir = target_root / target_subdir / skill_name
    else:
        target_skill_dir = target_root / skill_name

    source_skill_md = skill_path / "SKILL.md"
    target_file = target_skill_dir / target_filename
    valid_targets.add(target_file)

    # Read and transform SKILL.md
    try:
        content = source_skill_md.read_text(encoding='utf-8')
    except Exception as e:
        print(f"  Error reading {source_skill_md}: {e}")
        return 0, 1, valid_targets

    metadata, body = parse_frontmatter(content)
    new_frontmatter = frontmatter_fn(metadata, skill_name)
    new_body = body_transform_fn(body, skill_name)
    new_content = new_frontmatter + new_body

    # Write main file if changed
    if file_needs_update(new_content, target_file, is_text=True):
        if write_text_with_logging(new_content, target_file, source_skill_md, project_root, target_root):
            transferred += 1
        else:
            skipped += 1
    else:
        skipped += 1

    # Copy subdirectories
    for subdir_name in subdirs:
        subdir_transferred, subdir_skipped, subdir_targets = copy_directory_if_changed(
            skill_path / subdir_name,
            target_skill_dir / subdir_name,
            project_root,
            target_root,
            exclude=['__pycache__']
        )
        transferred += subdir_transferred
        skipped += subdir_skipped
        valid_targets.update(subdir_targets)

    return transferred, skipped, valid_targets


# =============================================================================
# Frontmatter Generators
# =============================================================================


def generate_opencode_skill_frontmatter(metadata: dict, skill_name: str) -> str:
    """Generate OpenCode-compliant YAML frontmatter for skills.

    OpenCode requires:
    - name: 1-64 chars, lowercase alphanumeric with hyphens (matches directory name)
    - description: 1-1024 chars
    """
    opencode_meta = {'name': skill_name}

    if 'description' in metadata:
        opencode_meta['description'] = metadata['description']

    yaml_str = yaml.dump(opencode_meta, default_flow_style=False, allow_unicode=True, sort_keys=False)
    return f"---\n{yaml_str}---\n"


# =============================================================================
# Source Discovery
# =============================================================================


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


# =============================================================================
# Main Transfer Functions
# =============================================================================


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
    skills = get_skill_sources(project_root)

    if not sources and not skills:
        print("No source directories found!")
        return 0, 0, 0

    if sources:
        print(f"Found {len(sources)} source directories")
    if skills:
        print(f"Found {len(skills)} skill(s)")
    print()

    # Track all valid target files for orphan cleanup
    valid_targets: set[Path] = set()
    skill_valid_targets: set[Path] = set()

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

    # Process skills
    for skill_path, skill_name in skills:
        print(f"--- skill/{skill_name} ---")

        skill_transferred, skill_skipped, skill_targets = transfer_skill(
            skill_path, skill_name, target_root, project_root,
            target_subdir="skill",
            target_filename="SKILL.md",
            frontmatter_fn=generate_opencode_skill_frontmatter,
            body_transform_fn=transform_opencode_skill_body,
            subdirs=['scripts', 'references']
        )

        transferred += skill_transferred
        skipped += skill_skipped
        skill_valid_targets.update(skill_targets)

        print()

    # Cleanup orphans for agents/commands
    print("--- Cleanup ---")
    removed = cleanup_orphans(target_root, valid_targets)

    # Cleanup orphans for skills
    removed += cleanup_orphan_files(target_root / "skill", skill_valid_targets, target_root)

    if removed == 0:
        print("  No orphans found")
    print()

    return transferred, skipped, removed


def main():
    project_root = Path(__file__).parent

    # Transfer to OpenCode
    transferred, skipped, removed = transfer_opencode(project_root)

    # Final summary
    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"OpenCode: {transferred} transferred, {skipped} unchanged, {removed} removed")
    print("=" * 60)


if __name__ == "__main__":
    main()
