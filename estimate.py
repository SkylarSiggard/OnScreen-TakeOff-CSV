import csv
import os
import math
import time

# Set up file paths
script_dir = os.path.dirname(os.path.abspath(__file__))
data_csv = os.path.join(script_dir, 'data.csv')
output_csv = os.path.join(script_dir, 'output.csv')

# List of excluded data types
excluded_types = {'Old', 'old', 'Attachment', 'Attachments', 'Skip'} 

def csv_to_dict(filename):
    result_dict = {}
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if not any(type in row for type in excluded_types):
                    try:
                        column_c, column_h, column_d, column_i, column_k, column_m = (
                            row[2], row[7], row[3], int(row[8]), int(row[10]), int(row[12])
                        )
                        result_dict.setdefault(column_c, {}).setdefault(column_h, {}).setdefault(column_d, [0, 0, 0])
                        result_dict[column_c][column_h][column_d][0] += column_i
                        result_dict[column_c][column_h][column_d][1] += column_k
                        result_dict[column_c][column_h][column_d][2] += column_m
                    except (ValueError, IndexError) as e:
                        print(f"Error processing row: {row[5]}. {type(e).__name__}: {e}, make sure only Area, Zone, and Type are being exported")
                        time.sleep(0.5)
    except FileNotFoundError:
        print(f"File not found: data.csv")
        time.sleep(2)
    except Exception as e:
        print(f"An unexpected error occurred: {type(e).__name__}: {e}")
        time.sleep(2)
    
    return result_dict

def write_dict_to_csv(dictionary, csv_filename):
    # Headers of CSV 
    fieldnames = ['Area', 'Zone', 'Type', 'Amount 1', 'Unit', 'Amount 2', 'Unit', 'Amount 3', 'Unit', 'Waste', 'Name', 'Unit', 'Total 1', 'Total 2', 'Total 3', 'Delivery', 'Pricing']
    
    try:
        with open(csv_filename, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for category_c, categories_h in dictionary.items():
                for category_h, materials in categories_h.items():
                    for material, amount in materials.items():
                        # Calculate waste
                        waste = 1.10
                        # What is added to CSV for each row
                        row = {
                            'Area': category_c,
                            'Zone': category_h,
                            'Type': material,
                            'Amount 1': amount[0],
                            'Unit': 'SF',
                            'Amount 2': amount[1],
                            'Unit': 'LF',
                            'Amount 3': amount[2],
                            'Unit': 'EA',
                            'Waste': f'{round((waste-1)*100)}%',
                            'Name': material,
                            'Unit': '',
                            'Total 1': math.ceil((amount[0]*waste)/10)*10,
                            'Total 2': math.ceil((amount[1]*waste)/10)*10,
                            'Total 3': math.ceil((amount[2]*waste)/10)*10,
                            'Delivery': round((amount[0]*waste)/200, 2),
                            'Pricing': ''
                        }
                        writer.writerow(row)
    except Exception as e:
        print(f"Error writing to CSV: {type(e).__name__}: {e}")
        time.sleep(2)

if __name__ == "__main__":
    try:
        # Runs the functions above and saves the csv in the same folder
        my_dict = csv_to_dict(data_csv)
        write_dict_to_csv(my_dict, output_csv)
        
        print("\n" + "=" * 20)
        print("     DONE")
        print("=" * 20)
        time.sleep(0.5)
    except KeyboardInterrupt:
        print("\nScript execution interrupted.")
    except Exception as e:
        print(f"An unexpected error occurred: {type(e).__name__}: {e}")
        time.sleep(2)