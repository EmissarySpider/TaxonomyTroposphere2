#!/bin/bash

# Check if a directory path was provided
if [ -z "$1" ]; then
  echo "Usage: $0 /path/to/folder"
  exit 1
fi

SEARCH_DIR="$1"

# Find all .py files and search their contents for "user-agent" (case-insensitive)
find "$SEARCH_DIR" -type f -name "*.py" -exec grep -i "user-agent" {} +
