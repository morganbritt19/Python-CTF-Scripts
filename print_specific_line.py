# This script will print a specific line of a set of files in a directory. This can be handy for quickly searching for oddities in files, which was useful in the Huntress 2023 CTF challenge HumanTwo.

import os

def print_line_36(directory):
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            try:
                with open(filepath, 'r') as file:
                    lines = file.readlines()
                    if len(lines) >= 36:
                        print(f"File: {filename}, Line 36: {lines[35].strip()}")
                    else:
                        print(f"File: {filename}, Line 36: File does not have 36 lines")
            except Exception as e:
                print(f"Error reading file {filename}: {str(e)}")

# Usage: Replace 'your_directory_path' with the path to your directory
print_line_36('your_directory_path')
