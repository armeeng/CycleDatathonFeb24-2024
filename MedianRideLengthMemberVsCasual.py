import pandas as pd
import os
import matplotlib.pyplot as plt

# Define the directory path where all CSV files are located
directory_path = "/Users/armeenghoorkhanian/Downloads/DataFiles"

# Initialize empty lists to store ride durations for casual and member riders for each month
ride_durations_casual = {}
ride_durations_member = {}

# Iterate over each CSV file in the directory
for filename in os.listdir(directory_path):
    if filename.endswith(".csv"):
        # Construct the full path to the CSV file
        full_path = os.path.join(directory_path, filename)

        # Load the CSV file into a DataFrame
        df_month = pd.read_csv(full_path)

        # Convert started_at and ended_at columns to datetime
        df_month['started_at'] = pd.to_datetime(df_month['started_at'])
        df_month['ended_at'] = pd.to_datetime(df_month['ended_at'])

        # Calculate ride duration for each ride
        df_month['ride_duration'] = (df_month['ended_at'] - df_month['started_at']).dt.total_seconds() / 60  # Convert to minutes

        # Group ride durations by user type (casual or member) and month
        ride_durations_grouped = df_month.groupby([df_month['started_at'].dt.month_name(), 'member_casual'])['ride_duration'].median()

        # Update ride durations for casual and member riders for each month
        for month, user_type in ride_durations_grouped.index:
            if user_type == 'casual':
                if month in ride_durations_casual:
                    ride_durations_casual[month].append(ride_durations_grouped[month][user_type])
                else:
                    ride_durations_casual[month] = [ride_durations_grouped[month][user_type]]
            else:
                if month in ride_durations_member:
                    ride_durations_member[month].append(ride_durations_grouped[month][user_type])
                else:
                    ride_durations_member[month] = [ride_durations_grouped[month][user_type]]

# Calculate the median ride duration for casual and member riders for each month
median_ride_durations_casual = {month: sorted(durations)[len(durations) // 2] if durations else None for month, durations in ride_durations_casual.items()}
median_ride_durations_member = {month: sorted(durations)[len(durations) // 2] if durations else None for month, durations in ride_durations_member.items()}

# Create a DataFrame from the median ride durations
df_median_ride_durations = pd.DataFrame({'Casual': median_ride_durations_casual, 'Member': median_ride_durations_member})

# Plot the median ride duration for casual and member riders for each month
plt.figure(figsize=(10, 6))
df_median_ride_durations.plot(kind='bar', ax=plt.gca())
plt.title("Median Ride Duration by Month and User Type")
plt.xlabel("Month")
plt.ylabel("Median Ride Duration (minutes)")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
