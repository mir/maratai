#!/bin/bash

# Sync agentskills/skill/ to one or more CLI tool config directories.
# Supports opencode, codex, and gemini targets.
# During copy, ${AGENTSKILLS_DIR} in text files is replaced with the
# target-specific path variable (e.g. ${OPENCODE_DIR}).

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SOURCE_DIR="$SCRIPT_DIR/agentskills/skill"

# Options
DRY_RUN=false
SHOW_DIFF=false
EXPLICIT_TARGETS=""

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
CYAN='\033[0;36m'
NC='\033[0m'

# --- Target definitions (bash 3 compatible, no associative arrays) ---

ALL_TARGETS="opencode codex gemini"

target_skills_dir() {
    case "$1" in
        opencode) echo "$HOME/.config/opencode/skill" ;;
        codex)    echo "$HOME/.codex/skills" ;;
        gemini)   echo "$HOME/.gemini/skills" ;;
    esac
}

target_detect_dir() {
    case "$1" in
        opencode) echo "$HOME/.config/opencode" ;;
        codex)    echo "$HOME/.codex" ;;
        gemini)   echo "$HOME/.gemini" ;;
    esac
}

target_path_var() {
    case "$1" in
        opencode) echo 'OPENCODE_DIR' ;;
        codex)    echo 'CODEX_DIR' ;;
        gemini)   echo 'GEMINI_DIR' ;;
    esac
}

target_display_dir() {
    case "$1" in
        opencode) echo "~/.config/opencode/" ;;
        codex)    echo "~/.codex/" ;;
        gemini)   echo "~/.gemini/" ;;
    esac
}

# --- Help ---

show_help() {
    echo "Usage: $(basename "$0") [OPTIONS]"
    echo ""
    echo "Sync Agent Skills to CLI tool config directories."
    echo ""
    echo "Options:"
    echo "  -t, --target TARGETS  Comma-separated targets (opencode,codex,gemini)"
    echo "                        Skips interactive detection when provided"
    echo "  -n, --dry-run         Preview changes without making them"
    echo "  -d, --diff            Show diffs for changed files"
    echo "  -h, --help            Show this help message"
    echo ""
    echo "Examples:"
    echo "  $(basename "$0")                    # interactive target selection"
    echo "  $(basename "$0") -t opencode        # sync to opencode only"
    echo "  $(basename "$0") -t opencode,codex  # sync to multiple targets"
    echo "  $(basename "$0") -n                 # dry-run (interactive)"
    echo "  $(basename "$0") -d -t codex        # diffs for codex target"
}

# --- Argument parsing ---

while [ $# -gt 0 ]; do
    case $1 in
        -n|--dry-run)
            DRY_RUN=true
            shift
            ;;
        -d|--diff)
            SHOW_DIFF=true
            shift
            ;;
        -t|--target)
            EXPLICIT_TARGETS="$2"
            shift 2
            ;;
        -h|--help)
            show_help
            exit 0
            ;;
        *)
            echo -e "${RED}Unknown option: $1${NC}"
            show_help
            exit 1
            ;;
    esac
done

# --- Utility ---

prefix() {
    if [ "$DRY_RUN" = true ]; then
        echo "[DRY-RUN] "
    fi
}

is_text_file() {
    case "$1" in
        *.md|*.py|*.sh|*.txt|*.yaml|*.yml|*.json|*.toml|*.cfg|*.ini|*.html|*.css|*.js|*.ts)
            return 0 ;;
        *)
            return 1 ;;
    esac
}

# --- Interactive target selection ---

select_targets_interactive() {
    local detected=""
    local idx=0
    local has_missing=false

    for t in $ALL_TARGETS; do
        ddir="$(target_detect_dir "$t")"
        if [ -d "$ddir" ]; then
            idx=$((idx + 1))
            detected="${detected}${idx}:${t} "
        else
            has_missing=true
        fi
    done

    if [ -z "$detected" ]; then
        echo -e "${RED}No supported CLI tools detected.${NC}"
        echo "Looked for: $ALL_TARGETS"
        exit 1
    fi

    echo -e "${BLUE}Detected CLI tools:${NC}"
    for entry in $detected; do
        num="${entry%%:*}"
        name="${entry#*:}"
        echo "  ${num}) ${name}	($(target_display_dir "$name"))"
    done

    if [ "$has_missing" = true ]; then
        echo ""
        echo -e "${YELLOW}Not detected:${NC}"
        for t in $ALL_TARGETS; do
            ddir="$(target_detect_dir "$t")"
            if [ ! -d "$ddir" ]; then
                echo "  - ${t}	($(target_display_dir "$t") not found)"
            fi
        done
    fi

    echo ""
    local max_idx=0
    for entry in $detected; do
        num="${entry%%:*}"
        if [ "$num" -gt "$max_idx" ]; then max_idx=$num; fi
    done
    printf "Sync to which targets? [1"
    if [ "$max_idx" -gt 1 ]; then
        printf ",%d" "$max_idx"
    fi
    printf " / all / none]: "
    read -r choice

    if [ "$choice" = "none" ] || [ -z "$choice" ]; then
        echo "No targets selected."
        exit 0
    fi

    SELECTED_TARGETS=""
    if [ "$choice" = "all" ]; then
        for entry in $detected; do
            name="${entry#*:}"
            SELECTED_TARGETS="${SELECTED_TARGETS} ${name}"
        done
    else
        # Parse comma-separated numbers
        OLD_IFS="$IFS"
        IFS=','
        for n in $choice; do
            IFS="$OLD_IFS"
            n="$(echo "$n" | tr -d ' ')"
            for entry in $detected; do
                num="${entry%%:*}"
                name="${entry#*:}"
                if [ "$num" = "$n" ]; then
                    SELECTED_TARGETS="${SELECTED_TARGETS} ${name}"
                fi
            done
        done
        IFS="$OLD_IFS"
    fi

    if [ -z "$SELECTED_TARGETS" ]; then
        echo -e "${RED}No valid targets selected.${NC}"
        exit 1
    fi
}

# --- Resolve targets ---

if [ -n "$EXPLICIT_TARGETS" ]; then
    SELECTED_TARGETS=""
    OLD_IFS="$IFS"
    IFS=','
    for p in $EXPLICIT_TARGETS; do
        IFS="$OLD_IFS"
        p="$(echo "$p" | tr -d ' ')"
        case "$p" in
            opencode|codex|gemini)
                SELECTED_TARGETS="${SELECTED_TARGETS} ${p}"
                ;;
            *)
                echo -e "${RED}Unknown target: ${p}${NC}"
                echo "Valid targets: opencode, codex, gemini"
                exit 1
                ;;
        esac
    done
    IFS="$OLD_IFS"
else
    select_targets_interactive
fi

# --- Show diff between two files ---

show_diff() {
    local src_file="$1"
    local dst_file="$2"

    if [ -f "$dst_file" ]; then
        if command -v colordiff &> /dev/null; then
            colordiff -u "$dst_file" "$src_file" 2>/dev/null || true
        else
            diff -u "$dst_file" "$src_file" 2>/dev/null || true
        fi
    fi
}

# --- Copy a single file with variable substitution ---

copy_file() {
    local src_file="$1"
    local dst_file="$2"
    local path_var="$3"

    local dst_dir
    dst_dir="$(dirname "$dst_file")"

    if [ ! -d "$dst_dir" ]; then
        if [ "$DRY_RUN" = false ]; then
            mkdir -p "$dst_dir"
        fi
    fi

    if is_text_file "$src_file"; then
        # Text file: substitute variable then compare
        local substituted
        substituted="$(sed "s/\${AGENTSKILLS_DIR}/\${${path_var}}/g" "$src_file")"

        if [ -f "$dst_file" ]; then
            local existing
            existing="$(cat "$dst_file")"
            if [ "$substituted" = "$existing" ]; then
                return 1  # no change
            fi
        fi

        if [ "$DRY_RUN" = false ]; then
            printf '%s\n' "$substituted" > "$dst_file"
        fi
        return 0  # changed
    else
        # Binary file: copy as-is
        if [ -f "$dst_file" ] && cmp -s "$src_file" "$dst_file"; then
            return 1  # no change
        fi
        if [ "$DRY_RUN" = false ]; then
            cp "$src_file" "$dst_file"
        fi
        return 0  # changed
    fi
}

# --- Sync files for a single target ---

sync_target() {
    local target_name="$1"
    local target_dir
    local path_var

    target_dir="$(target_skills_dir "$target_name")"
    path_var="$(target_path_var "$target_name")"

    echo -e "${BLUE}=== Syncing to ${target_name} ===${NC}"
    if [ "$DRY_RUN" = true ]; then
        echo -e "${YELLOW}*** DRY-RUN MODE - No changes will be made ***${NC}"
    fi
    echo -e "${BLUE}Source: ${SOURCE_DIR}/${NC}"
    echo -e "${BLUE}Target: ${target_dir}/${NC}"
    echo -e "${BLUE}Variable: \${AGENTSKILLS_DIR} -> \${${path_var}}${NC}"
    echo ""

    # Check source
    if [ ! -d "$SOURCE_DIR" ]; then
        echo -e "${RED}Error: Source directory '$SOURCE_DIR' does not exist${NC}"
        exit 1
    fi

    # Create target if needed
    if [ ! -d "$target_dir" ]; then
        echo -e "${YELLOW}$(prefix)Creating target directory: ${target_dir}${NC}"
        if [ "$DRY_RUN" = false ]; then
            mkdir -p "$target_dir"
        fi
    fi

    # Sync files
    echo -e "${BLUE}--- Syncing files ---${NC}"
    find "$SOURCE_DIR" -type f | while read -r src_file; do
        rel_path="${src_file#$SOURCE_DIR/}"

        # Skip .DS_Store
        case "$rel_path" in
            *.DS_Store*) continue ;;
        esac

        dst_file="$target_dir/$rel_path"

        if copy_file "$src_file" "$dst_file" "$path_var"; then
            if [ -f "$dst_file" ]; then
                echo -e "${GREEN}$(prefix)Updated: ${rel_path}${NC}"
            else
                echo -e "${GREEN}$(prefix)Creating: ${rel_path}${NC}"
            fi

            if [ "$SHOW_DIFF" = true ] && [ -f "$dst_file" ]; then
                echo -e "${CYAN}--- Diff for ${rel_path} ---${NC}"
                show_diff "$src_file" "$dst_file"
                echo ""
            fi
        fi
    done

    # Cleanup orphans
    echo ""
    echo -e "${BLUE}--- Cleaning up orphans ---${NC}"
    if [ -d "$target_dir" ]; then
        find "$target_dir" -type f | while read -r dst_file; do
            rel_path="${dst_file#$target_dir/}"

            case "$rel_path" in
                *.DS_Store*) continue ;;
            esac

            src_file="$SOURCE_DIR/$rel_path"
            if [ ! -f "$src_file" ]; then
                echo -e "${RED}$(prefix)Removing orphan: ${rel_path}${NC}"
                if [ "$DRY_RUN" = false ]; then
                    rm "$dst_file"
                fi
            fi
        done

        # Clean empty directories
        if [ "$DRY_RUN" = false ]; then
            find "$target_dir" -type d -empty -delete 2>/dev/null || true
        fi
    fi

    echo ""
}

# --- Main ---

echo -e "${BLUE}=== Agent Skills Sync ===${NC}"
echo ""

for target in $SELECTED_TARGETS; do
    sync_target "$target"
done

echo -e "${BLUE}=== Sync Complete ===${NC}"
if [ "$DRY_RUN" = true ]; then
    echo -e "${YELLOW}This was a dry-run. No changes were made.${NC}"
else
    echo -e "${GREEN}All skills synced successfully.${NC}"
fi
