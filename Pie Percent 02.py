import matplotlib.pyplot as plt
import numpy as np

# Data for the pie chart
labels = ['WS-12', 'GRP', 'WS-12 & GRP sensitive']
sizes = [6, 2, 4]  # Updated number of activated cells for each stimulation
total = sum(sizes)  # Total number of activated cells (12)

# Calculate percentages
percentages = [size / total * 100 for size in sizes]

# Colors for each slice (softer, less intense colors)
colors = ['#A8D8FF', '#FFB3BA', '#FFFFB3']  # Light blue for WS-12, Light pink for GRP, Light yellow for Polymodal

# Create the pie chart
fig, ax = plt.subplots(figsize=(12, 9), facecolor='#F0F0F0')  # Light gray background
wedges, texts = ax.pie(sizes, colors=colors, startangle=90, wedgeprops=dict(width=0.5, edgecolor='white'))

# Add labels with cell counts and percentages outside the pie chart
for i, wedge in enumerate(wedges):
    ang = (wedge.theta2 + wedge.theta1) / 2
    y = np.sin(np.deg2rad(ang))
    x = np.cos(np.deg2rad(ang))
    ax.annotate(f'n = {sizes[i]}\n({percentages[i]:.1f}%)', xy=(x, y), 
                xytext=(1.35*np.sign(x), 1.4*y),
                horizontalalignment='center', fontsize=14, fontweight='bold',
                bbox=dict(boxstyle="square,pad=0.3", fc='white', ec="black", alpha=0.7))

# Add total number of cells in the center
ax.text(0, 0, f'Total\n{total}', ha='center', va='center', fontsize=16, fontweight='bold', color='#333333')

# Add title
plt.title("B", fontsize=18, fontweight='bold', color='#333333')

# Add legend without n and percentage
plt.legend(wedges, labels,
           title="Stimulation Types",
           loc="center left",
           bbox_to_anchor=(1, 0, 0.5, 1),
           prop={'weight': 'bold', 'size': 12})

# Make the legend title bold
plt.setp(plt.gca().get_legend().get_title(), fontweight='bold')

# Remove axes
ax.axis('equal')
plt.axis('off')

# Adjust layout to prevent clipping of labels
plt.subplots_adjust(left=0.1, right=0.7, top=0.9, bottom=0.1)

# Show the plot
plt.show()

# Save the figure (optional)
# plt.savefig('activated_cells_pie_chart.png', dpi=300, bbox_inches='tight')