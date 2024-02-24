import pandas as pd
import os
import matplotlib.pyplot as plt

# Define the directory path where all CSV files are located
directory_path = "/Users/armeenghoorkhanian/Downloads/DataFiles"

# Initialize empty dictionaries to store the total number of rides for each month and user type
total_rides_per_month = {}

# Define the order of months
months_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

# Iterate over each CSV file in the directory
for filename in os.listdir(directory_path):
    if filename.endswith(".csv"):
        # Construct the full path to the CSV file
        full_path = os.path.join(directory_path, filename)

        # Load the CSV file into a DataFrame
        df_month = pd.read_csv(full_path)

        # Extract month from started_at column
        df_month['started_at'] = pd.to_datetime(df_month['started_at'])
        df_month['month'] = df_month['started_at'].dt.month_name()

        # Group the data by month and member_casual column, then count the number of rides for each group
        rides_per_month = df_month.groupby(['month', 'member_casual']).size().unstack(fill_value=0)

        # Update the total number of rides for each month and user type
        for month, rides in rides_per_month.iterrows():
            if month in total_rides_per_month:
                total_rides_per_month[month] += rides
            else:
                total_rides_per_month[month] = rides

# Convert the dictionary to a DataFrame
total_rides_df = pd.DataFrame(total_rides_per_month).T

# Convert the month names to a categorical data type with specified order
total_rides_df.index = pd.CategoricalIndex(total_rides_df.index, categories=months_order, ordered=True)

# Sort the DataFrame by the index (months)
total_rides_df = total_rides_df.sort_index()

# Plot the total number of rides for each month and user type
plt.figure(figsize=(10, 6))
total_rides_df.plot(kind='bar', stacked=True, ax=plt.gca())
plt.title("Total Number of Rides by Month and User Type")
plt.xlabel("Month")
plt.ylabel("Total Number of Rides")
plt.xticks(rotation=45, ha='right')
plt.legend(title="User Type")
plt.tight_layout()
plt.show()
