import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# Get the path to the desktop
desktop = os.path.join(os.path.expanduser("~"), "Desktop")

# Load your data from the desktop, specifying the "Bar graph" sheet
file_path = os.path.join(desktop, 'Figure_1.xlsx')
data = pd.read_excel(file_path, sheet_name='Bar graph')

# Define the categories and their corresponding columns
categories = ['Cold', 'Hot', 'Mech']
group_prefixes = ['_1', '_2', '_3']

# Initialize lists to store means and 5 evenly spaced points
all_means = []
all_evenly_spaced_points = []

# Process each group
for prefix in group_prefixes:
    means = []
    evenly_spaced_points = []
    
    for category in categories:
        column_name = category.lower() + prefix
        if column_name not in data.columns:
            print(f"Warning: Column '{column_name}' not found. Skipping.")
            means.append(np.nan)
            evenly_spaced_points.append([])
            continue
        
        column_data = data[column_name].dropna()
        
        # Adjust the values by dividing by 10
        column_data = column_data / 100
        
        means.append(column_data.mean())
        
        # Calculate 5 evenly spaced points between min and max
        min_val = column_data.min()
        max_val = column_data.max()
        evenly_spaced = np.linspace(min_val, max_val, 5)
        evenly_spaced_points.append(evenly_spaced.tolist())
    
    all_means.append(means)
    all_evenly_spaced_points.append(evenly_spaced_points)

# Create the plot with subplots for each group
fig, axes = plt.subplots(1, 3, figsize=(18, 6), sharey=True)

# Define the titles for each subplot
titles = ['Mechanical', 'Cold', 'Hot']

# Set the dot color to black
dot_color = 'black'  # Black color for the dots

# Determine the maximum value across all means and points for setting y-axis limit
max_value = max(max(means) for means in all_means)
for points in all_evenly_spaced_points:
    for point_list in points:
        if point_list:
            max_value = max(max_value, max(point_list))

# Set y-axis limit with some padding
y_max_limit = max_value * 1.1  # Add 10% padding to the top

for i, (means, evenly_spaced_points) in enumerate(zip(all_means, all_evenly_spaced_points)):
    ax = axes[i]
    bars = ax.bar(categories, means, alpha=0.7, color='skyblue')
    
    # Add evenly spaced points
    for j, points in enumerate(evenly_spaced_points):
        x = np.full(5, j)  # Create 5 x-coordinates at the same position
        ax.scatter(x, points, color=dot_color, alpha=0.6, s=30)  # Change color here
    
    ax.set_title(titles[i], fontsize=16, fontweight='bold')
    if i == 0:  # Only set y-label for the first subplot
        ax.set_ylabel('Δ F/F0 %', fontsize=14)
    
    ax.set_ylim(0, y_max_limit)  # Set y-axis limit based on calculated max value
    
    ax.tick_params(axis='y', which='both', left=True, labelleft=True)  # Show y-axis labels
    ax.tick_params(axis='x', labelsize=12)  # Increase x-axis label font size

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()

# Save the figure (optional)
# plt.savefig(os.path.join(desktop, 'bar_graph_with_evenly_spaced_points_delta_f_f0_percentage.png'), dpi=300, bbox_inches='tight')