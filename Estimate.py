import csv
import os
import math

# Set up file paths
script_dir = os.path.dirname(os.path.abspath(__file__))
data_csv = os.path.join(script_dir, 'data.csv')
output_csv = os.path.join(script_dir, 'output.csv')

# List of excluded data types
excluded_types = {'Old', 'old', 'Attachment', 'Attachments'} 

# Places CSV into a Dictionary
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
    # Headers of CSV 
    fieldnames = ['Category', 'Material', 'Amount', 'Unit', 'Linear', 'Unit', 'Other', 'Unit', 'Waste', 'Name', 'Total 1', 'Total 2', 'Total 3', 'Delivery']
    
    with open(csv_filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for category, materials in dictionary.items():
            for material, amount in materials.items():
                # Calculate waste and round to two decimal places
                waste = round((amount[0]*0.10)/20, 2)
                # What is added to CSV for each row
                row = {
                    'Category': category,
                    'Material': material,
                    'Amount': amount[0],
                    'Unit': 'SF',
                    'Linear': amount[1],
                    'Other': amount[2],
                    'Waste': waste,
                    'Name': material,
                    'Total 1': math.ceil((amount[0]*1.10)/10)*10,
                    'Total 2': math.ceil((amount[1]*1.10)/10)*10,
                    'Total 3': math.ceil((amount[2]*1.10)/10)*10,
                    'Delivery': round((amount[0]*1.10)/200, 2)
                }
                writer.writerow(row)

if __name__=="__main__":
    # Runs the functions above and saves the csv in the same folder
    my_dict = csv_to_dict(data_csv)
    write_dict_to_csv(my_dict, output_csv)
