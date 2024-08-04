import pandas as pd
import matplotlib.pyplot as plt
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

# Create line graph
plt.figure(figsize=(20, 10))  # Adjusted figure size for better visibility

for stimulus in stimuli:
    plt.plot(data['Time (s)'], data[f'{stimulus}_normalized'], label=stimulus, linewidth=2)

plt.title('B', fontweight='bold', fontsize=16)
plt.xlabel('Time (s)', fontweight='bold', fontsize=14)
plt.ylabel('ΔF/F%', fontweight='bold', fontsize=14)

# Adjust x-axis ticks to show seconds
plt.xticks(range(0, 301, 60), fontweight='bold')
plt.yticks(fontweight='bold')

# Add a vertical line at stimulation onset (5 seconds) without the label
plt.axvline(x=150, color='red', linestyle='--', linewidth=2)

plt.legend(fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()

# Save the figure
plt.savefig(os.path.join(desktop, 'calcium_imaging_linegraph_WS12_GRP.png'), dpi=300, bbox_inches='tight')