import pandas as pd
import os
import dash
from dash import dcc, html

# Define the directory path where all CSV files are located
directory_path = "/Users/armeenghoorkhanian/Downloads/DataFiles"

# Initialize an empty list to store DataFrames for each CSV file
dataframes = []

# Iterate over each CSV file in the directory
for filename in os.listdir(directory_path):
    if filename.endswith(".csv"):
        # Construct the full path to the CSV file
        full_path = os.path.join(directory_path, filename)

        # Read the CSV file into a DataFrame and append it to the list
        df = pd.read_csv(full_path)
        dataframes.append(df)

# Concatenate all DataFrames into a single DataFrame
combined_df = pd.concat(dataframes, ignore_index=True)

# Initialize Dash app
app = dash.Dash(__name__)

# Define layout
app.layout = html.Div([
    html.H1("Bike Sharing Dashboard"),
    # Add your visualizations here using dcc.Graph
])

# Define callback functions to update plots (if needed)

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
