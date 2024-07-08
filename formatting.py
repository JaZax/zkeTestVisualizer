import csv

input_file = 'inputFile.csv'
output_file = 'output.csv'

"""
    convert delimiters in input csv file
"""

with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
    lines = infile.readlines()
    
    data_lines = lines[11:]
    
    for line in data_lines:
        parts = line.strip().split(',')
        
        new_line = f"{parts[0]};{parts[1]},{parts[2]};{parts[3]},{parts[4]}\n"
        
        outfile.write(new_line)
