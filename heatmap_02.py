import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import os

# Get the path to the desktop
desktop = os.path.join(os.path.expanduser("~"), "Desktop")

# Load your data from the desktop, specifying Sheet2
data = pd.read_excel(os.path.join(desktop, 'Figure_1.xlsx'), sheet_name='Sheet2')

# Identify the stimulus columns
stimuli = ['WS-12', 'GRP']

# Calculate ΔF/F% for each stimulus
for stimulus in stimuli:
    F0 = data[stimulus].iloc[:10].mean()  # Average of first 10 data points (1 second)
    data[f'{stimulus}_normalized'] = (data[stimulus] - F0) / F0 * 100

# Melt the dataframe to long format for heatmap
heatmap_data = data.melt(id_vars=['Time (s)'], 
                         value_vars=[f'{s}_normalized' for s in stimuli],
                         var_name='Stimulus', value_name='Value')

# Create heatmap
plt.figure(figsize=(20, 6))  # Adjusted figure size for the longer time scale
heatmap = sns.heatmap(heatmap_data.pivot(index='Stimulus', columns='Time (s)', values='Value'),
                      cmap='viridis', cbar_kws={'label': 'ΔF/F%'})

plt.title('B', fontweight='bold')
plt.xlabel('Time (s)', fontweight='bold')
plt.ylabel('Stimulus', fontweight='bold')

# Adjust x-axis ticks to show seconds
plt.xticks(np.arange(0, 301, 60), np.arange(0, 301, 60))  # Tick every 60 seconds

# Add a vertical line at stimulation onset (5 seconds) without the label
plt.axvline(x=150, color='red', linestyle='--', linewidth=2)

# Modify y-axis labels
plt.yticks(ticks=[0.5, 1.5], labels=stimuli, fontweight='bold')

plt.tight_layout()
plt.show()

# Save the figure
plt.savefig(os.path.join(desktop, 'calcium_imaging_heatmap_WS12_GRP.png'), dpi=300, bbox_inches='tight')