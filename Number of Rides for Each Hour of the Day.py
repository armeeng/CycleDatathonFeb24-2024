import pandas as pd
import os
import calendar
import matplotlib.pyplot as plt

# Define the directory path where all CSV files are located
directory_path = "/Users/armeenghoorkhanian/Downloads/DataFiles"

# Initialize an empty DataFrame to store the combined data for the whole year
year_data = pd.DataFrame()

# Initialize a dictionary to store peak number of trips for each month
peak_trips_months = {}

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
        df_month['start_hour'] = df_month['started_at'].dt.hour

        # Compute number of rides for each hour of the day
        rides_per_hour = df_month['start_hour'].value_counts().sort_index()

        # Store number of rides for each hour of the day in the dictionary
        peak_trips_months[month_name] = rides_per_hour

# Convert the dictionary to a DataFrame and sort by month
peak_trips_df = pd.DataFrame(peak_trips_months)

# Plot histogram for the number of rides for each hour of the day for each month
plt.figure(figsize=(14, 8))
for month in peak_trips_df.columns:
    plt.plot(peak_trips_df.index, peak_trips_df[month], label=month)

plt.title("Number of Rides for Each Hour of the Day")
plt.xlabel("Hour of the Day")
plt.ylabel("Number of Rides")
plt.legend(loc="upper left")
plt.xticks(range(24), [f"{hour % 12 or 12} {'AM' if hour < 12 else 'PM'}" for hour in range(24)], fontsize=8)
plt.grid(True)
plt.show()
