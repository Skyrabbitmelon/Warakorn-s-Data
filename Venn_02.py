import pandas as pd
import matplotlib.pyplot as plt
from matplotlib_venn import venn2
import os

# Get the path to the desktop
desktop = os.path.join(os.path.expanduser("~"), "Desktop")

# Load your data from the Excel sheet
file_path = os.path.join(desktop, 'Figure_1.xlsx')
data = pd.read_excel(file_path, sheet_name='Venn2')

# Count the number of cells activated by each stimulus
ws12_active = sum(data['WS-12'] == 1)
grp_active = sum(data['GRP'] == 1)

# Count the number of cells activated by both stimuli
both_active = sum((data['WS-12'] == 1) & (data['GRP'] == 1))

# Adjust counts for Venn diagram
only_ws12 = ws12_active - both_active
only_grp = grp_active - both_active

# Create the Venn diagram with custom colors
plt.figure(figsize=(10,6))
v = venn2(subsets=(only_ws12, only_grp, both_active), 
          set_labels=('WS-12', 'GRP'))

# Set custom colors
v.get_patch_by_id('10').set_color('#1f77b4')  # Blue for WS-12
v.get_patch_by_id('01').set_color('#d62728')  # Red for GRP
v.get_patch_by_id('11').set_color('#ff7f0e')  # Orange for overlap

# Adjust alpha for better visibility
v.get_patch_by_id('10').set_alpha(0.7)
v.get_patch_by_id('01').set_alpha(0.7)
v.get_patch_by_id('11').set_alpha(0.7)

# Add bold header
plt.text(0.5, 1.05, 'B', fontsize=20, fontweight='bold', ha='center', va='center', transform=plt.gca().transAxes)

# Calculate total cells and overlap percentage
total_cells = len(data)
overlap_percentage = (both_active / total_cells) * 100

# Add legend with cell counts and percentages
legend_elements = [
    plt.Rectangle((0,0),1,1, facecolor='#1f77b4', edgecolor='none', alpha=0.7),
    plt.Rectangle((0,0),1,1, facecolor='#d62728', edgecolor='none', alpha=0.7),
    plt.Rectangle((0,0),1,1, facecolor='#ff7f0e', edgecolor='none', alpha=0.7)
]
legend_labels = [
    f'WS-12 only (n={only_ws12})',
    f'GRP only (n={only_grp})',
    f'Both WS-12 & GRP (n={both_active}, {overlap_percentage:.1f}%)',
    f'Total cells: {total_cells}'
]
plt.legend(legend_elements, legend_labels, title='Stimulation Categories', loc='center left', bbox_to_anchor=(1, 0.5))

plt.tight_layout()
plt.show()