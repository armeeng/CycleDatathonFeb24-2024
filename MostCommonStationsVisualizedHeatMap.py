import pandas as pd
import os
from collections import Counter

# Define the directory path where all CSV files are located
directory_path = "/Users/armeenghoorkhanian/Downloads/DataFiles"

# Initialize an empty Counter object to store the occurrence of each station
station_counter = Counter()

# Initialize an empty dictionary to store latitude and longitude for each station
station_locations = {}

# Iterate over each CSV file in the directory
for filename in os.listdir(directory_path):
    if filename.endswith(".csv"):
        # Construct the full path to the CSV file
        full_path = os.path.join(directory_path, filename)

        # Load the CSV file into a DataFrame
        df = pd.read_csv(full_path)

        # Update station occurrence counts
        station_counter.update(df['start_station_name'])

        # Extract station locations
        for index, row in df.iterrows():
            start_station_name = row['start_station_name']
            if start_station_name not in station_locations:
                station_locations[start_station_name] = (row['start_lat'], row['start_lng'])

# Create a DataFrame for station occurrences
station_occurrences = pd.DataFrame(list(station_counter.items()), columns=['Station', 'Occurrences'])

# Add latitude and longitude columns to the DataFrame
station_occurrences['Latitude'] = station_occurrences['Station'].map(lambda x: station_locations[x][0] if x in station_locations else None)
station_occurrences['Longitude'] = station_occurrences['Station'].map(lambda x: station_locations[x][1] if x in station_locations else None)

# Save the DataFrame as a CSV file
output_file_path = "/Users/armeenghoorkhanian/Downloads/station_occurrences.csv"
station_occurrences.to_csv(output_file_path, index=False)

print("CSV file saved successfully.")
