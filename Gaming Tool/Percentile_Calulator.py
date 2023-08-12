
'''
Percentile calculation function
'''
import numpy as np
from Test import FPS
from tabulate import tabulate

def calculate_percentile(data_frame, column_name, percentile):
    # Extract the column data
    column_data = data_frame[column_name]

    # Calculate the specified percentile using numpy
    calculated_percentile = np.percentile(column_data, percentile)

    return calculated_percentile


# Example usage
# Assuming 'df' is your DataFrame containing a column 'Frametime'
# Replace 95 with the desired percentile value
percentile_values_str = input("Enter the percentile values (comma-separated): ")
percentile_values = [float(x) for x in percentile_values_str.split(',')]


results = calculate_percentile(FPS, 'MsBetweenPresents', percentile_values)

percentile_table = []
for i, percentile in enumerate(percentile_values):
    percentile_table.append([f"P{percentile}FPS", results[i]])


table_headers = ["Percentile", "Value"]
table = tabulate(percentile_table, headers=table_headers, tablefmt="fancy_grid")

print(table)

