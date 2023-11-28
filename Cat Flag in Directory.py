# This Python script is designed to search for a specific text pattern, denoted by 'flag{', within files located in a specified directory.

import os
import re

directory_path = "/path/to/your/directory"

# List all files in the directory
files = os.listdir(directory_path)

for file in files:
    if os.path.isfile(os.path.join(directory_path, file)):
        try:
            # Read the file contents
            with open(os.path.join(directory_path, file), "r") as f:
                file_contents = f.read()

                # Use regex to search for the flag pattern with any content in the curly braces
                flag_matches = re.findall(r'flag{([^}]+)}', file_contents)

                # Check if any matches were found
                if flag_matches:
                    for match in flag_matches:
                        print(f"Flag found in {file}: flag{{{match}}}")
                    break  # Stop searching if the flag is found

        except Exception as e:
            print(f"Error occurred while reading {file}: {str(e)}")
