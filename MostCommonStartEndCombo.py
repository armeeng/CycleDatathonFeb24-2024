import pandas as pd
import os

# Define the directory path where all CSV files are located
directory_path = "/Users/armeenghoorkhanian/Downloads/DataFiles"

# Initialize an empty DataFrame to store the most common start-to-end combination for each month
most_common_combinations_per_month = {}

# Iterate over each CSV file in the directory
for filename in os.listdir(directory_path):
    if filename.endswith(".csv"):
        # Construct the full path to the CSV file
        full_path = os.path.join(directory_path, filename)

        # Load the CSV file into a DataFrame
        df_month = pd.read_csv(full_path)

        # Filter out rows where either the start or end station name is empty
        df_month = df_month[(df_month['start_station_name'] != '') & (df_month['end_station_name'] != '')]

        # Group the data by start station name and end station name, then count the occurrences
        combinations_count = df_month.groupby(['start_station_name', 'end_station_name']).size()

        # Sort the results by the count of combinations in descending order
        most_common_combination = combinations_count.idxmax()

        # Store the most common combination for the month
        most_common_combinations_per_month[filename[:-4]] = (most_common_combination, combinations_count[most_common_combination])

# Print the most common start-to-end combination for each month
for month, (combination, count) in most_common_combinations_per_month.items():
    print(f"Month: {month}, Most Common Combination: {combination}, Count: {count}")
