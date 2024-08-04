import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import os

# Get the path to the desktop
desktop = os.path.join(os.path.expanduser("~"), "Desktop")

# Load your data from the desktop, specifying Sheet1
data = pd.read_excel(os.path.join(desktop, 'Figure_1.xlsx'), sheet_name='Sheet1')

# Identify the stimulus columns
stimuli = ['VF4.0g', 'Cold Saline', 'Hot Saline']

# Calculate ΔF/F% for each stimulus separately
for stimulus in stimuli:
    # Calculate F0 for each stimulus independently
    F0 = data[stimulus].iloc[:50].mean()  # Average of first 5 seconds (assuming 10 frames per second)
    # Calculate ΔF/F% for each stimulus
    data[f'{stimulus}_normalized'] = (data[stimulus] - F0) / F0 * 100

# Melt the dataframe to long format for heatmap
heatmap_data = data.melt(id_vars=['Time (s)'], 
                         value_vars=[f'{s}_normalized' for s in stimuli],
                         var_name='Stimulus', value_name='ΔF/F%')

# Create heatmap
plt.figure(figsize=(15, 8))
heatmap = sns.heatmap(heatmap_data.pivot(index='Stimulus', columns='Time (s)', values='ΔF/F%'),
                      cmap='viridis', cbar_kws={'label': 'ΔF/F%'})

plt.title('A', fontweight='bold', fontsize=16)
plt.xlabel('Time (s)', fontweight='bold', fontsize=14)
plt.ylabel('Stimulus', fontweight='bold', fontsize=14)

# Adjust x-axis ticks to show seconds
plt.xticks(np.arange(0, 151, 30), np.arange(0, 15.1, 3), fontweight='bold')  # Tick every 3 seconds

# Add a vertical line at stimulation onset (5 seconds)
plt.axvline(x=50, color='red', linestyle='--', linewidth=2)
plt.text(50, plt.ylim()[1] * 1.01, 'Stimulation Onset', color='black', rotation=90, va='bottom')

# Modify y-axis labels
plt.yticks(ticks=[0.5, 1.5, 2.5], labels=stimuli, fontweight='bold')

plt.tight_layout()
plt.show()

# Save the figure
plt.savefig(os.path.join(desktop, 'calcium_imaging_heatmap.png'), dpi=300, bbox_inches='tight')