import csv
import os

# Set up file paths
script_dir = os.path.dirname(os.path.abspath(__file__))
data_csv = os.path.join(script_dir, 'data.csv')
output_csv = os.path.join(script_dir, 'output.csv')

# List of excluded data types
excluded_types = {'Old', 'old', 'Attachment', 'Attachments'} 

def csv_to_dict(filename):
    result_dict = {}
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if not any(type in row for type in excluded_types):
                column_c, column_d, column_h, column_j, column_l = row[2], row[3], int(row[7]), int(row[9]), int(row[11])
                result_dict.setdefault(column_c, {}).setdefault(column_d, [0, 0, 0])
                result_dict[column_c][column_d][0] += column_h
                result_dict[column_c][column_d][1] += column_j
                result_dict[column_c][column_d][2] += column_l
    return result_dict

def write_dict_to_csv(dictionary, csv_filename):
    fieldnames = ['Category', 'Material', 'Size', 'Amount', 'Unit', 'Linear', 'Unit', 'Other', 'Unit',
    'Notes', 'Waste', 'Name','Total 1', 'Total 2', 'Total 3', 'Delivery']
    with open(csv_filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
