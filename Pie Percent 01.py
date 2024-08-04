import matplotlib.pyplot as plt
import numpy as np

# Data for the pie chart
labels = ['Mechanical', 'Cold Saline', 'Hot Saline', 'Polymodal']
sizes = [5, 14, 4, 7]  # Updated number of activated cells for each stimulation
total = sum(sizes)  # Total number of activated cells (30)

# Calculate percentages
percentages = [size / total * 100 for size in sizes]

# Colors for each slice
colors = ['#66c2a5', '#4e79a7', '#ff6b6b', 'grey']  # Added grey for polynomial

# Create the pie chart
fig, ax = plt.subplots(figsize=(12, 9))
wedges, texts = ax.pie(sizes, colors=colors, startangle=90, wedgeprops=dict(width=0.5))

# Add percentage labels outside the pie chart with leader lines
for i, p in enumerate(wedges):
    ang = (p.theta2 - p.theta1) / 2. + p.theta1
    y = np.sin(np.deg2rad(ang))
    x = np.cos(np.deg2rad(ang))
    horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
    connectionstyle = f"angle,angleA=0,angleB={ang}"
    kw = dict(xycoords='data', textcoords='data',
              arrowprops=dict(arrowstyle="-", color='gray', connectionstyle=connectionstyle),
              bbox=dict(boxstyle="round", fc="w"), zorder=0, va="center")
    ax.annotate(f'{percentages[i]:.1f}%\nn = {sizes[i]}', xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),
                horizontalalignment=horizontalalignment, fontsize=14, fontweight='bold', **kw)

# Add total number of cells in the center
ax.text(0, 0, f'Total\n{total}', ha='center', va='center', fontsize=16, fontweight='bold')

# Add title
plt.title("A", fontsize=18, fontweight='bold')

# Add legend with bold text and increased font size
plt.legend(wedges, labels,
           title="Stimulation Types",
           loc="center left",
           bbox_to_anchor=(1, 0, 0.5, 1),
           prop={'weight': 'bold', 'size': 12})

# Make the legend title bold
plt.setp(plt.gca().get_legend().get_title(), fontweight='bold')

# Adjust layout to prevent clipping of labels
plt.tight_layout()

# Show the plot
plt.show()

# Save the figure (optional)
# plt.savefig('activated_cells_pie_chart.png', dpi=300, bbox_inches='tight')
