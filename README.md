# CSV Data Processor

This Python script processes CSV data and generates a new CSV file with specific calculations applied. It excludes rows with certain data types and performs aggregations based on columns C, D, H, J, and L.

## Usage

1. **Set up file paths:**
   - `script_dir`: Directory containing the script.
   - `data_csv`: Path to the input CSV file.
   - `output_csv`: Path to the output CSV file.

2. **Excluded Data Types:**
   - Modify the `excluded_types` set to exclude specific data types from processing.

3. **Functions:**

   - `csv_to_dict(filename)`: Converts the input CSV file into a dictionary, performing aggregations.

   - `write_dict_to_csv(dictionary, csv_filename)`: Writes the processed data dictionary to a new CSV file.

4. **Headers in Output CSV:**
   - 'Category', 'Material', 'Amount', 'Unit', 'Linear', 'Unit', 'Other', 'Unit', 'Waste', 'Name', 'Total 1', 'Total 2', 'Total 3', 'Delivery'.

## Example

```python
import csv
import os
import math

# ... (rest of the code remains the same)

if __name__=="__main__":
    # Runs the functions above and saves the csv in the same folder
    my_dict = csv_to_dict(data_csv)
    write_dict_to_csv(my_dict, output_csv)
```

## Notes

- Ensure the input CSV file (`data.csv`) is present in the same directory as this script.
- The script performs specific calculations and transformations. Modify as per your specific requirements.
- The output CSV file (`output.csv`) will be generated in the same directory as the script.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
