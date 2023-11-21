# CSV Data Processor

This Python script processes CSV data and generates a new CSV file with specific calculations applied. It excludes rows with certain data types and performs aggregations based on columns.

## Usage

### On-Screen Setup:

1. **Categorization by Area:**
   - For multiple areas, ensure each material is assigned to the corresponding "area." Items will be categorized by area in the Category column.
   - All items with the same "Type" will be aggregated together, so name your types accordingly.

2. **Export CSV Format:**
   - Export CSV with the following columns: Type, Zone, Area, Class, Num, Name, Measurement, Num1, Type1, Num2, Type2, Num3, Type3.

3. **Headers in Output CSV:**
   - 'Category', 'Material', 'Amount', 'Unit', 'Linear', 'Unit', 'Other', 'Unit', 'Waste', 'Name', 'Total 1', 'Total 2', 'Total 3', 'Delivery'.

## Notes

- Ensure the input CSV file (`data.csv`) is present in the same directory as this script.
- The script performs specific calculations and transformations. Modify it as per your specific requirements.
- The output CSV file (`output.csv`) will be generated in the same directory as the script.