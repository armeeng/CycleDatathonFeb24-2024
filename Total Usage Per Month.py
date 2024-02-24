import pandas as pd
import os
import calendar
import matplotlib.pyplot as plt

# Define the directory path where all CSV files are located
directory_path = "/Users/armeenghoorkhanian/Downloads/DataFiles"

# Initialize a dictionary to store the total number of rides for each month
total_rides_per_month = {}

# Iterate over each CSV file in the directory
for filename in os.listdir(directory_path):
    if filename.endswith(".csv"):
        # Construct the full path to the CSV file
        full_path = os.path.join(directory_path, filename)

        # Load the CSV file into a DataFrame
        df_month = pd.read_csv(full_path)

        # Extract month from started_at column
        df_month['started_at'] = pd.to_datetime(df_month['started_at'])
        month_name = df_month['started_at'].dt.month[0]  # Get the month number
        month_name = calendar.month_name[month_name]  # Convert month number to month name

        # Compute total number of rides for the month
        total_rides_month = len(df_month)

        # Add total number of rides for the month to the dictionary
        if month_name in total_rides_per_month:
            total_rides_per_month[month_name] += total_rides_month
        else:
            total_rides_per_month[month_name] = total_rides_month

# Convert the dictionary to a DataFrame
total_rides_df = pd.DataFrame(list(total_rides_per_month.items()), columns=['Month', 'Total Rides'])

# Sort the DataFrame by month
total_rides_df['Month'] = pd.Categorical(total_rides_df['Month'], categories=calendar.month_name[1:], ordered=True)
total_rides_df = total_rides_df.sort_values(by='Month')

# Plot total number of rides for each month
plt.figure(figsize=(10, 6))
plt.bar(total_rides_df['Month'], total_rides_df['Total Rides'], color='skyblue', edgecolor='black')
plt.title("Total Number of Rides for Each Month", fontsize=16)
plt.xlabel("Month", fontsize=14)
plt.ylabel("Total Number of Rides", fontsize=14)
plt.xticks(rotation=45, ha='right', fontsize=12)
plt.yticks(fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
