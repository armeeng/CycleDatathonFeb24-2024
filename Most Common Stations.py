import pandas as pd
import os
from collections import Counter
import calendar
import matplotlib.pyplot as plt

# Define the directory path where all CSV files are located
directory_path = "/Users/armeenghoorkhanian/Downloads/DataFiles"

# Initialize empty lists to store the data
table_data = []

# Iterate over each CSV file in the directory
for filename in os.listdir(directory_path):
    if filename.endswith(".csv"):
        # Construct the full path to the CSV file
        full_path = os.path.join(directory_path, filename)

        # Load the CSV file into a DataFrame
        df_month = pd.read_csv(full_path)

        # Extract month from started_at column
        df_month['started_at'] = pd.to_datetime(df_month['started_at'])
        month_number = df_month['started_at'].dt.month[0]  # Get the month number
        month_name = calendar.month_name[month_number]  # Convert month number to month name

        # Compute the most common start/end stations for the month
        most_common_stations_month = Counter(df_month['start_station_name'].dropna()).most_common(1)
        most_common_station, most_common_station_visits = most_common_stations_month[0] if most_common_stations_month else ("No data", 0)

        # Append the data to the table_data list
        table_data.append([month_name, most_common_station, most_common_station_visits])

# Compute the total number of visits for each common station
common_station_visits = Counter(station for _, station, _ in table_data)

# Compute the most common start station for the whole year
most_common_station_year, most_common_station_year_visits = common_station_visits.most_common(1)[0] if common_station_visits else ("No data", 0)
table_data.append(["Whole Year", most_common_station_year, most_common_station_year_visits])

# Sort the table_data list by month name (excluding "Whole Year")
table_data_sorted = sorted(table_data[:-1], key=lambda x: list(calendar.month_name).index(x[0]))
table_data_sorted.append(table_data[-1])  # Append "Whole Year" to the sorted list

# Create a table as a DataFrame
df_table = pd.DataFrame(table_data_sorted, columns=["Month", "Most Common Station", "Total Visits"])

# Plot the table
fig, ax = plt.subplots(figsize=(10, 6))
ax.axis('off')  # Hide axes

# Hide the table plot axes
table = ax.table(cellText=df_table.values, colLabels=df_table.columns, loc='center')

# Set table font size
table.auto_set_font_size(False)
table.set_fontsize(12)

# Save the plot as a PNG image
plt.savefig("most_common_station_per_month.png", dpi=300)
plt.show()
