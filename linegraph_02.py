import pandas as pd
import matplotlib.pyplot as plt
import os

# Get the path to the desktop
desktop = os.path.join(os.path.expanduser("~"), "Desktop")

# Load your data from the desktop, specifying Sheet1
data = pd.read_excel(os.path.join(desktop, 'Figure_1.xlsx'), sheet_name='Sheet1')

# Identify the stimulus columns and assign colors
stimuli = {
    'VF4.0g': 'green',
    'Cold Saline': 'blue',
    'Hot Saline': 'red'
}

# Calculate ΔF/F% for each stimulus
for stimulus in stimuli.keys():
    F0 = data[stimulus].iloc[:10].mean()  # Average of first 10 data points (1 second)
    data[f'{stimulus}_normalized'] = (data[stimulus] - F0) / F0 * 100

# Create line graph
plt.figure(figsize=(15, 8))

for stimulus, color in stimuli.items():
    plt.plot(data['Time (s)'], data[f'{stimulus}_normalized'], label=stimulus, color=color, linewidth=2)

plt.title('A', fontweight='bold', fontsize=16)
plt.xlabel('Time (s)', fontweight='bold', fontsize=14)
plt.ylabel('ΔF/F%', fontweight='bold', fontsize=14)

# Adjust x-axis ticks to show seconds
plt.xticks(range(0, 16, 3), fontweight='bold')
plt.yticks(fontweight='bold')

# Add a vertical line at stimulation onset (5 seconds)
plt.axvline(x=5, color='red', linestyle='--', linewidth=2)
plt.text(5, plt.ylim()[1], 'Stimulation Onset', color='black', rotation=90, va='bottom')

plt.legend(fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()

# Save the figure
plt.savefig(os.path.join(desktop, 'calcium_imaging_linegraph.png'), dpi=300, bbox_inches='tight')