import pandas as pd
import os
from collections import Counter
import calendar
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Define the directory path where all CSV files are located
directory_path = "/Users/armeenghoorkhanian/Downloads/DataFiles"

# Initialize an empty list to store all start station names
start_stations = []

# Iterate over each CSV file in the directory
for filename in os.listdir(directory_path):
    if filename.endswith(".csv"):
        # Construct the full path to the CSV file
        full_path = os.path.join(directory_path, filename)

        # Load the CSV file into a DataFrame
        df_month = pd.read_csv(full_path)

        # Extract start station names
        start_stations.extend(df_month['start_station_name'].dropna())

# Combine start station names with multiple words
start_stations_combined = [' '.join(station.split(' & ')) for station in start_stations]

# Count the frequency of each start station
station_counts = Counter(start_stations_combined)

# Generate word cloud from frequencies
wordcloud = WordCloud(width=800, height=400, background_color='white')
wordcloud.generate_from_frequencies(station_counts)

# Plot the word cloud
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.title('Word Cloud of Start Stations')
plt.axis('off')
plt.show()
