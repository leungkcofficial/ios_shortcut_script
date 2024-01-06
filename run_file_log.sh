#!/bin/bash

# URL of the Python script
PYTHON_SCRIPT_URL="https://raw.githubusercontent.com/leungkcofficial/ios_shortcut_script/main/file_log.py"

# Destination filename for the Python script
DEST_FILENAME="file_log.py"

# Download the Python script
curl -o "$DEST_FILENAME" "$PYTHON_SCRIPT_URL"

# Make the Python script executable
chmod +x "$DEST_FILENAME"
