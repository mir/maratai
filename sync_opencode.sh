#!/bin/bash

# Script to sync opencode/ files to ~/.config/opencode/
# This replaces files in ~/.config/opencode/ subfolders with files from opencode/ subfolders

set -e  # Exit on error

SOURCE_DIR="opencode"
TARGET_DIR="$HOME/.config/opencode"

# Options
DRY_RUN=false
SHOW_DIFF=false

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Help function
show_help() {
    echo "Usage: $(basename "$0") [OPTIONS]"
    echo ""
    echo "Sync files from opencode/ to ~/.config/opencode/"
    echo ""
    echo "Options:"
    echo "  -n, --dry-run    Preview changes without making them"
    echo "  -d, --diff       Show diffs for changed files"
    echo "  -h, --help       Show this help message"
    echo ""
    echo "Examples:"
    echo "  $(basename "$0")           # Normal sync with orphan cleanup"
    echo "  $(basename "$0") -n        # Dry-run (preview only)"
    echo "  $(basename "$0") -d        # Show diffs for changed files"
    echo "  $(basename "$0") -n -d     # Dry-run with diffs"
}

# Parse command-line arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        -n|--dry-run)
            DRY_RUN=true
            shift
            ;;
        -d|--diff)
            SHOW_DIFF=true
            shift
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

# Prefix for dry-run mode
prefix() {
    if [ "$DRY_RUN" = true ]; then
        echo "[DRY-RUN] "
    fi
}

echo -e "${BLUE}=== OpenCode Sync Script ===${NC}"
if [ "$DRY_RUN" = true ]; then
    echo -e "${YELLOW}*** DRY-RUN MODE - No changes will be made ***${NC}"
fi
echo -e "${BLUE}Source: ${SOURCE_DIR}${NC}"
echo -e "${BLUE}Target: ${TARGET_DIR}${NC}"
echo ""

# Check if source directory exists
if [ ! -d "$SOURCE_DIR" ]; then
    echo -e "${RED}Error: Source directory '$SOURCE_DIR' does not exist${NC}"
    echo -e "${YELLOW}Please run this script from the maratai project root${NC}"
    exit 1
fi

# Create target directory if it doesn't exist
if [ ! -d "$TARGET_DIR" ]; then
    echo -e "${YELLOW}$(prefix)Target directory does not exist. Creating: ${TARGET_DIR}${NC}"
    if [ "$DRY_RUN" = false ]; then
        mkdir -p "$TARGET_DIR"
    fi
fi

# Function to show diff between two files
show_diff() {
    local src_file="$1"
    local dst_file="$2"

    if [ -f "$dst_file" ]; then
        # Use diff with color if available
        if command -v colordiff &> /dev/null; then
            colordiff -u "$dst_file" "$src_file" 2>/dev/null || true
        else
            diff -u "$dst_file" "$src_file" 2>/dev/null || true
        fi
    fi
}

# Function to copy files recursively
sync_files() {
    local src="$1"
    local dst="$2"

    # Find all files in source directory
    find "$src" -type f | while read -r src_file; do
        # Get relative path from source directory
        rel_path="${src_file#$src/}"

        # Skip .DS_Store files
        if [[ "$rel_path" == *".DS_Store"* ]]; then
            continue
        fi

        # Construct destination path
        dst_file="$dst/$rel_path"
        dst_dir="$(dirname "$dst_file")"

        # Create destination directory if it doesn't exist
        if [ ! -d "$dst_dir" ]; then
            echo -e "${YELLOW}$(prefix)Creating directory: ${dst_dir}${NC}"
            if [ "$DRY_RUN" = false ]; then
                mkdir -p "$dst_dir"
            fi
        fi

        # Check if file exists and differs
        if [ -f "$dst_file" ]; then
            if ! cmp -s "$src_file" "$dst_file"; then
                echo -e "${GREEN}$(prefix)Updating: ${rel_path}${NC}"
                if [ "$SHOW_DIFF" = true ]; then
                    echo -e "${CYAN}--- Diff for ${rel_path} ---${NC}"
                    show_diff "$src_file" "$dst_file"
                    echo ""
                fi
                if [ "$DRY_RUN" = false ]; then
                    cp "$src_file" "$dst_file"
                fi
            fi
        else
            echo -e "${GREEN}$(prefix)Creating: ${rel_path}${NC}"
            if [ "$DRY_RUN" = false ]; then
                cp "$src_file" "$dst_file"
            fi
        fi
    done
}

# Function to clean up orphaned files
cleanup_orphans() {
    local src="$1"
    local dst="$2"

    # Check if target directory exists
    if [ ! -d "$dst" ]; then
        return
    fi

    # Find files in target that don't exist in source
    find "$dst" -type f | while read -r dst_file; do
        # Get relative path from target directory
        rel_path="${dst_file#$dst/}"

        # Skip .DS_Store files
        if [[ "$rel_path" == *".DS_Store"* ]]; then
            continue
        fi

        # Check if source file exists
        src_file="$src/$rel_path"
        if [ ! -f "$src_file" ]; then
            echo -e "${RED}$(prefix)Removing orphan: ${rel_path}${NC}"
            if [ "$DRY_RUN" = false ]; then
                rm "$dst_file"
            fi
        fi
    done

    # Clean up empty directories
    if [ "$DRY_RUN" = false ]; then
        find "$dst" -type d -empty -delete 2>/dev/null || true
    else
        # In dry-run, just report empty directories that would be removed
        find "$dst" -type d -empty 2>/dev/null | while read -r empty_dir; do
            rel_dir="${empty_dir#$dst/}"
            if [ -n "$rel_dir" ]; then
                echo -e "${RED}$(prefix)Would remove empty directory: ${rel_dir}${NC}"
            fi
        done
    fi
}

# Sync files
echo -e "${BLUE}--- Syncing files ---${NC}"
sync_files "$SOURCE_DIR" "$TARGET_DIR"

# Clean up orphans
echo ""
echo -e "${BLUE}--- Cleaning up orphans ---${NC}"
cleanup_orphans "$SOURCE_DIR" "$TARGET_DIR"

echo ""
echo -e "${BLUE}=== Sync Complete ===${NC}"
if [ "$DRY_RUN" = true ]; then
    echo -e "${YELLOW}This was a dry-run. No changes were made.${NC}"
else
    echo -e "${GREEN}All files from ${SOURCE_DIR}/ have been synced to ${TARGET_DIR}/${NC}"
fi
