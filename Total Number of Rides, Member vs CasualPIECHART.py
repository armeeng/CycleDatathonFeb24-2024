import pandas as pd
import os
import matplotlib.pyplot as plt

# Define the directory path where all CSV files are located
directory_path = "/Users/armeenghoorkhanian/Downloads/DataFiles"

# Initialize variables to store the total number of rides for casual and member users
total_casual_rides = 0
total_member_rides = 0

# Iterate over each CSV file in the directory
for filename in os.listdir(directory_path):
    if filename.endswith(".csv"):
        # Construct the full path to the CSV file
        full_path = os.path.join(directory_path, filename)

        # Load the CSV file into a DataFrame
        df_month = pd.read_csv(full_path)

        # Count the number of casual and member rides in the current month
        total_casual_rides += df_month[df_month['member_casual'] == 'casual'].shape[0]
        total_member_rides += df_month[df_month['member_casual'] == 'member'].shape[0]

# Create a pie chart
labels = ['Casual Rides', 'Member Rides']
sizes = [total_casual_rides, total_member_rides]
colors = ['#ff9999', '#66b3ff']  # Light red and light blue
explode = (0.1, 0)  # explode the 1st slice (Casual Rides)

plt.figure(figsize=(10, 6))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title("Proportion of Casual Rides vs. Member Rides for the Whole Year", fontsize=16)
plt.show()
