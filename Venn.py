import pandas as pd
import matplotlib.pyplot as plt
from matplotlib_venn import venn3
import os

# Get the path to the desktop
desktop = os.path.join(os.path.expanduser("~"), "Desktop")

# Load your data from the Excel sheet
file_path = os.path.join(desktop, 'Figure_1.xlsx')
data = pd.read_excel(file_path, sheet_name='Venn')

# Count the number of cells activated by each stimulus
mechanical_active = sum(data['Mechanical'] == 1)
cold_active = sum(data['Cold'] == 1)
hot_active = sum(data['Hot'] == 1)

# Count the number of cells activated by combinations of stimuli
mechanical_and_cold = sum((data['Mechanical'] == 1) & (data['Cold'] == 1))
mechanical_and_hot = sum((data['Mechanical'] == 1) & (data['Hot'] == 1))
cold_and_hot = sum((data['Cold'] == 1) & (data['Hot'] == 1))
all_three = sum((data['Mechanical'] == 1) & (data['Cold'] == 1) & (data['Hot'] == 1))

# Adjust counts for Venn diagram
only_mechanical = mechanical_active - mechanical_and_cold - mechanical_and_hot + all_three
only_cold = cold_active - mechanical_and_cold - cold_and_hot + all_three
only_hot = hot_active - mechanical_and_hot - cold_and_hot + all_three
mechanical_and_cold_only = mechanical_and_cold - all_three
mechanical_and_hot_only = mechanical_and_hot - all_three
cold_and_hot_only = cold_and_hot - all_three

# Create the Venn diagram with custom colors
plt.figure(figsize=(12, 8))
v = venn3(subsets=(only_mechanical, only_cold, mechanical_and_cold_only, only_hot, mechanical_and_hot_only, cold_and_hot_only, all_three), 
          set_labels=('Mechanical', 'Cold', 'Hot'))

# Set custom colors
v.get_patch_by_id('100').set_color('#00FF00')  # Green for Mechanical
v.get_patch_by_id('010').set_color('#0000FF')  # Blue for Cold
v.get_patch_by_id('001').set_color('#FF0000')  # Red for Hot
v.get_patch_by_id('110').set_color('#00FFFF')  # Cyan for Mechanical & Cold
v.get_patch_by_id('101').set_color('#FFFF00')  # Yellow for Mechanical & Hot
v.get_patch_by_id('011').set_color('#FF00FF')  # Magenta for Cold & Hot
v.get_patch_by_id('111').set_color('#FFFFFF')  # White for all three

# Adjust alpha and edge color for better visibility
for patch_id in ['100', '010', '001', '110', '101', '011', '111']:
    patch = v.get_patch_by_id(patch_id)
    if patch:
        patch.set_alpha(0.7)
        patch.set_edgecolor('black')
        patch.set_linewidth(2)

# Add bold header
plt.text(0.5, 1.05, 'A', fontsize=20, fontweight='bold', ha='center', va='center', transform=plt.gca().transAxes)

# Calculate percentages and total cells
total_cells = len(data)
overlap_percentage = (all_three / total_cells) * 100

# Add legend with cell counts and percentages
legend_elements = [
    plt.Rectangle((0,0),1,1, facecolor='#00FF00', edgecolor='black', alpha=0.7),  # Mechanical
    plt.Rectangle((0,0),1,1, facecolor='#0000FF', edgecolor='black', alpha=0.7),  # Cold
    plt.Rectangle((0,0),1,1, facecolor='#FF0000', edgecolor='black', alpha=0.7),  # Hot
    plt.Rectangle((0,0),1,1, facecolor='#00FFFF', edgecolor='black', alpha=0.7),  # Mechanical & Cold
    plt.Rectangle((0,0),1,1, facecolor='#FFFF00', edgecolor='black', alpha=0.7),  # Mechanical & Hot
    plt.Rectangle((0,0),1,1, facecolor='#FF00FF', edgecolor='black', alpha=0.7),  # Cold & Hot
    plt.Rectangle((0,0),1,1, facecolor='#FFFFFF', edgecolor='black', alpha=0.7)   # All three
]
legend_labels = [
    f'Mechanical only (n={only_mechanical})',
    f'Cold only (n={only_cold})',
    f'Hot only (n={only_hot})',
    f'Mechanical & Cold (n={mechanical_and_cold_only})',
    f'Mechanical & Hot (n={mechanical_and_hot_only})',
    f'Cold & Hot (n={cold_and_hot_only})',
    f'All three (n={all_three})',
    f'Total cells: {total_cells}',
    f'Three stimuli overlap: {overlap_percentage:.1f}%'
]
plt.legend(legend_elements, legend_labels, title='Stimulation Categories', loc='center left', bbox_to_anchor=(1, 0.5))

plt.tight_layout()
plt.show()