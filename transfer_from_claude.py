#!/usr/bin/env -S uv run --script
# /// script
# dependencies = ["pyyaml"]
# requires-python = ">=3.12"
# ///

"""
Transfer skills from Claude Code plugin folders to Agent Skills format.

Source directories:
- claude-maratai-dev/skills/<name>/ -> agentskills/skill/<name>/
- claude-maratai-manager/skills/<name>/ -> agentskills/skill/<name>/

Transformations:
- SKILL.md frontmatter is rewritten with compliant name/description
- ${CLAUDE_PLUGIN_ROOT}/skills/<skill>/ replaced with ${AGENTSKILLS_DIR}/skill/<skill>/
- scripts/, references/, and workflows/ subdirectories are copied as-is
"""

import shutil
import yaml
from pathlib import Path


# =============================================================================
# Utility Functions
# =============================================================================


def file_needs_update(source_content: bytes | str, target_path: Path, *, is_text: bool = False) -> bool:
    """Return True if target doesn't exist or content differs."""
    if not target_path.exists():
        return True
    try:
        if is_text:
            return target_path.read_text(encoding='utf-8') != source_content
        return target_path.read_bytes() != source_content
    except Exception:
        return True


def prompt_delete(file_path: Path, display_root: Path) -> bool:
    """Prompt user to confirm deletion of orphan file."""
    rel_path = file_path.relative_to(display_root)
    while True:
        response = input(f"  Delete orphan '{rel_path}'? [y/n]: ").strip().lower()
        if response in ('y', 'yes'):
            return True
        elif response in ('n', 'no'):
            return False
        print("  Please enter 'y' or 'n'")


def parse_frontmatter(content: str) -> tuple[dict, str]:
    """Parse YAML frontmatter from markdown content.

    Returns (metadata dict, body content). If no frontmatter, returns ({}, full content).
    """
    content = content.lstrip()
    if not content.startswith('---'):
        return {}, content

    lines = content.split('\n')
    end_idx = None
    for i, line in enumerate(lines[1:], start=1):
        if line.strip() == '---':
            end_idx = i
            break

    if end_idx is None:
        return {}, content

    yaml_content = '\n'.join(lines[1:end_idx])
    try:
        metadata = yaml.safe_load(yaml_content) or {}
    except yaml.YAMLError:
        metadata = {}

    body = '\n'.join(lines[end_idx + 1:])
    body = body.lstrip('\n')

    return metadata, body


# =============================================================================
# Skill Transfer
# =============================================================================


def get_skill_sources(project_root: Path) -> list[tuple[Path, str]]:
    """Find all skill directories across plugins.

    Returns list of (skill_path, skill_name) tuples.
    """
    skills = []

    for plugin_dir in ['claude-maratai-dev', 'claude-maratai-manager']:
        skills_dir = project_root / plugin_dir / 'skills'
        if not skills_dir.exists():
            continue
        for skill_path in sorted(skills_dir.iterdir()):
            if skill_path.is_dir() and (skill_path / 'SKILL.md').exists():
                skills.append((skill_path, skill_path.name))

    return skills


def generate_opencode_frontmatter(metadata: dict, skill_name: str) -> str:
    """Generate OpenCode-compliant YAML frontmatter for a skill."""
    opencode_meta = {'name': skill_name}

    if 'description' in metadata:
        opencode_meta['description'] = metadata['description']

    yaml_str = yaml.dump(opencode_meta, default_flow_style=False, allow_unicode=True, sort_keys=False)
    return f"---\n{yaml_str}---\n"


def transform_body(body: str, skill_name: str) -> str:
    """Replace Claude plugin path variables with OpenCode equivalents."""
    old_path = f"${{CLAUDE_PLUGIN_ROOT}}/skills/{skill_name}"
    new_path = f"${{AGENTSKILLS_DIR}}/skill/{skill_name}"
    return body.replace(old_path, new_path)


def transfer_skill(
    skill_path: Path,
    skill_name: str,
    target_root: Path,
    project_root: Path,
) -> tuple[int, int, set[Path]]:
    """Transfer a single skill to OpenCode format.

    Returns (transferred_count, skipped_count, valid_target_paths).
    """
    transferred = 0
    skipped = 0
    valid_targets: set[Path] = set()

    target_skill_dir = target_root / 'skill' / skill_name

    # --- SKILL.md ---
    source_skill_md = skill_path / 'SKILL.md'
    target_file = target_skill_dir / 'SKILL.md'
    valid_targets.add(target_file)

    try:
        content = source_skill_md.read_text(encoding='utf-8')
    except Exception as e:
        print(f"  Error reading {source_skill_md}: {e}")
        return 0, 1, valid_targets

    metadata, body = parse_frontmatter(content)
    new_content = generate_opencode_frontmatter(metadata, skill_name) + transform_body(body, skill_name)

    if file_needs_update(new_content, target_file, is_text=True):
        target_file.parent.mkdir(parents=True, exist_ok=True)
        try:
            target_file.write_text(new_content, encoding='utf-8')
            print(f"  Transferred: {source_skill_md.relative_to(project_root)} -> {target_file.relative_to(target_root)}")
            transferred += 1
        except Exception as e:
            print(f"  Error writing {target_file}: {e}")
            skipped += 1
    else:
        skipped += 1

    # --- Subdirectories (scripts, references, workflows) ---
    for subdir_name in ['scripts', 'references', 'workflows']:
        source_subdir = skill_path / subdir_name
        if not source_subdir.exists() or not source_subdir.is_dir():
            continue

        target_subdir = target_skill_dir / subdir_name
        for source_file in source_subdir.rglob('*'):
            if not source_file.is_file():
                continue
            if '__pycache__' in source_file.parts:
                continue

            rel_path = source_file.relative_to(source_subdir)
            target = target_subdir / rel_path
            valid_targets.add(target)

            try:
                source_bytes = source_file.read_bytes()
            except Exception as e:
                print(f"  Error reading {source_file}: {e}")
                skipped += 1
                continue

            if file_needs_update(source_bytes, target):
                target.parent.mkdir(parents=True, exist_ok=True)
                try:
                    shutil.copy2(source_file, target)
                    print(f"  Copied: {source_file.relative_to(project_root)} -> {target.relative_to(target_root)}")
                    transferred += 1
                except Exception as e:
                    print(f"  Error copying {source_file}: {e}")
                    skipped += 1
            else:
                skipped += 1

    return transferred, skipped, valid_targets


def cleanup_orphans(skill_root: Path, valid_targets: set[Path], display_root: Path) -> int:
    """Remove files under skill_root that aren't in valid_targets. Returns count removed."""
    removed = 0
    if not skill_root.exists():
        return 0

    for target_file in skill_root.rglob('*'):
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

    # Clean empty directories
    for d in sorted(skill_root.rglob('*'), reverse=True):
        if d.is_dir() and not any(d.iterdir()):
            try:
                d.rmdir()
            except Exception:
                pass

    return removed


# =============================================================================
# Main
# =============================================================================


def main():
    project_root = Path(__file__).parent
    target_root = project_root / 'agentskills'

    print("=" * 60)
    print("Transfer Claude Code Skills -> Agent Skills")
    print("=" * 60)
    print(f"Target: {target_root}")
    print()

    skills = get_skill_sources(project_root)
    if not skills:
        print("No skills found!")
        return

    print(f"Found {len(skills)} skill(s)")
    print()

    if not target_root.exists():
        target_root.mkdir(parents=True, exist_ok=True)

    total_transferred = 0
    total_skipped = 0
    all_valid_targets: set[Path] = set()

    for skill_path, skill_name in skills:
        print(f"--- skill/{skill_name} ---")
        transferred, skipped, valid_targets = transfer_skill(
            skill_path, skill_name, target_root, project_root
        )
        total_transferred += transferred
        total_skipped += skipped
        all_valid_targets.update(valid_targets)
        print()

    # Cleanup orphans
    print("--- Cleanup ---")
    removed = cleanup_orphans(target_root / 'skill', all_valid_targets, target_root)
    if removed == 0:
        print("  No orphans found")
    print()

    # Summary
    print("=" * 60)
    print(f"Done: {total_transferred} transferred, {total_skipped} unchanged, {removed} removed")
    print("=" * 60)


if __name__ == "__main__":
    main()
