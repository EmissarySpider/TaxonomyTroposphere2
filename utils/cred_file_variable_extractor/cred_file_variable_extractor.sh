#!/bin/bash

# Check if a directory path was provided
if [ -z "$1" ]; then
  echo "Usage: $0 /path/to/search"
  exit 1
fi

SEARCH_DIR="$1"

# Parse all .sh files and grep for the pattern
for file in "$SEARCH_DIR"/*.sh; do
  if [[ -f "$file" ]]; then
    egrep 'CRED_FILE_NAMES=.*\)' "$file" >> cred_file_names.txt
    echo -e "end $file \n------------------------\n" >> cred_file_names.txt
  fi
done
