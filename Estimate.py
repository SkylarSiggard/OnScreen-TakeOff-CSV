import csv
import os
import math

#! Setup
script_dir = os.path.dirname(os.path.abspath(__file__))
data_csv = os.path.join(script_dir, 'data.csv')
output_csv = os.path.join(script_dir, 'output.csv')

#! List of Data to avoid 
excluded_types = ['Old', 'old', 'Attachment', 'Attachments'] 

#! Function 1 
def csv_to_dict(filename):
    '''
    This function reads in a CSV file and converts it into a nested dictionary format. The CSV file is expected to have 
    columns labeled C, D, H, J, and L, and the function only includes rows that do not contain any excluded types. 
    The resulting dictionary has the unique values from column C as the keys of the outer dictionary, and the values 
    of each key are inner dictionaries. The inner dictionaries have the unique values from column D as their keys, 
    and the values are lists containing the sum of values from columns H, J, and L for each corresponding row in the CSV file. 
    If a key-value pair already exists for a given combination of column C and column D, the values for H, J, and L are 
    added to the existing values in the dictionary.
    '''
    result_dict = {}
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader: 
            if not any(type in row for type in excluded_types):
                column_c = row[2]
                column_d = row[3]
                column_h = int(row[7])
                column_j = int(row[9])
                column_l = int(row[11])
                if column_c not in result_dict:
                    result_dict[column_c] = {}
                if column_d in result_dict[column_c]:
                    result_dict[column_c][column_d][0] += column_h
                    result_dict[column_c][column_d][1] += column_j
                    result_dict[column_c][column_d][2] += column_l
                else:
                    result_dict[column_c][column_d] = [column_h, column_j, column_l]
    return result_dict

#! Function 2
def write_dict_to_csv(dictionary, csv_filename):
    '''
    This function takes a nested dictionary in the format described above and writes it to a CSV file. The CSV file contains 
    a header row with 16 columns, and subsequent rows represent each category/material combination from the input dictionary. 
    For each row, the function calculates several values and adds them to the CSV file. The calculation involves multiplying 
    the amount of material by 1.1 (representing a 10% waste factor), and then rounding up to the nearest multiple of 10. This 
    value is then divided by 200 to give the delivery fee. The function uses the Python csv module to write the data to the 
    CSV file specified in the input.
    '''
    with open(csv_filename, 'w', newline='') as csvfile:
        #! Headers of CSV 
        fieldnames = ('Category', 'Material', 'Size', 'Amount', 'Unit', 'Linear', 'Unit','Other','Unit','Notes','Waste', 'Name','Total 1', 'Total 2', 'Total 3','Delivery')
        writer = csv.writer(csvfile)
        writer.writerow(fieldnames)
        for category, materials in dictionary.items():
            for material, amount in materials.items():
                #! What is added to CSV for each row
                row = [category, material, '', amount[0], 'SF', amount[1], 'LF', amount[2], 'LF','','110%',material,math.ceil((amount[0]*1.10)/10)*10,math.ceil((amount[1]*1.10)/10)*10,math.ceil((amount[2]*1.10)/10)*10,round((amount[0]*1.10)/200)] 
                writer.writerow(row)

if __name__=="__main__":
    #! Runs the functions above and saves the csv in the same folder
    my_dict = csv_to_dict(data_csv)
    write_dict_to_csv(my_dict, output_csv)
