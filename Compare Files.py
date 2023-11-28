# This script is designed to compare the contents of two files. Replace 'file1.txt' and 'file2.txt' with the files to be compared. 

def compare_files(file1_path, file2_path):
    try:
        with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
            lines1 = file1.readlines()
            lines2 = file2.readlines()

            # Compare the lines and output the differences
            print(f"Differences between {file1_path} and {file2_path}:")
            for line_num, (line1, line2) in enumerate(zip(lines1, lines2)):
                if line1 != line2:
                    print(f"Line {line_num + 1}:")
                    print(f"  {file1_path}: {line1.strip()}")
                    print(f"  {file2_path}: {line2.strip()}")
            # Check for extra lines in one of the files
            if len(lines1) > len(lines2):
                print(f"Additional lines in {file1_path}:")
                for line_num in range(len(lines2), len(lines1)):
                    print(f"  {file1_path}: {lines1[line_num].strip()}")
            elif len(lines1) < len(lines2):
                print(f"Additional lines in {file2_path}:")
                for line_num in range(len(lines1), len(lines2)):
                    print(f"  {file2_path}: {lines2[line_num].strip()}")

    except FileNotFoundError as e:
        print(f"Error: {e}")

# Usage: Replace 'file1.txt' and 'file2.txt' with your file paths
compare_files('file1.txt', 'file2.txt')
