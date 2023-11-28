# This script will read a CSV, remove the content from the second column, and save the modified data to a .txt file. The second column of the CSV is used for an example and can be changed as necessary.

import csv

# Function to strip specific content from CSV and save to a text file
def strip_and_save(csv_file, output_txt_file):
    try:
        with open(csv_file, 'r') as csv_input, open(output_txt_file, 'w') as txt_output:
            # Create a CSV reader and a text file writer
            csv_reader = csv.reader(csv_input)
            
            for row in csv_reader:
                # Check if there are at least two columns in the row
                if len(row) >= 2:
                    # Remove the content of the second column (index 1)
                    del row[1]
                    
                    # Write the modified row to the text file
                    txt_output.write(','.join(row) + '\n')
    
        print(f'Stripped content from {csv_file} and saved to {output_txt_file}')
    except FileNotFoundError:
        print(f'File not found: {csv_file}')

# Replace 'input.csv' and 'output.txt' with your file paths
input_csv_file = 'input.csv'
output_txt_file = 'output.txt'

strip_and_save(input_csv_file, output_txt_file)
