# CSV Data Processor

This Python script processes CSV data and generates a new CSV file with specific calculations applied. It excludes rows with certain data types and performs aggregations based on columns C, D, H, J, and L.

## Usage

### On-Screen Setup:

- For multiple areas, ensure each material is assigned to the corresponding "area". Items will be categorized by area in the Category column. All items with the same "Type" will be aggregated together, so name your types accordingly.
- Export CSV as folows: Type, Zone, Area, Class, Num, Name, Measurement, Num1, Type1, Num2, Type2, Num3, Type3

1. **Set Up File Paths:**
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
    # Runs the functions above and saves the CSV in the same folder
    my_dict = csv_to_dict(data_csv)
    write_dict_to_csv(my_dict, output_csv)
```

## Notes

- Ensure the input CSV file (`data.csv`) is present in the same directory as this script.
- The script performs specific calculations and transformations. Modify as per your specific requirements.
- The output CSV file (`output.csv`) will be generated in the same directory as the script.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
