#the plot used for deliverables to show bottlenecks

import matplotlib.pyplot as plt
import numpy as np

activity_data = {
    "main_thread": {
        "File I/O \nDART-CESM": 19.5,
        "Total CPU, MPI, \nOther I/O processes \nand Wait Time": 80.5
    }
}

# Extract  data
labels = list(activity_data["main_thread"].keys())
sizes = list(activity_data["main_thread"].values())
colors = ['#f18930', 'green']

fig, ax = plt.subplots(figsize=(10,7))

# Plot pie chart
wedges, texts, autotexts = ax.pie(sizes, labels=None, colors=colors, autopct='',
                                  startangle=315, pctdistance=0.85)

# Annotate percentages manually, make them in the center of each segment
for i, wedge in enumerate(wedges):
    ang = (wedge.theta2 - wedge.theta1) / 2. + wedge.theta1
    y = np.sin(np.deg2rad(ang)) * 0.35  # Adjust the factor to position text closer to center
    x = np.cos(np.deg2rad(ang)) * 0.55  # Adjust the factor to position text closer to center
    percentage = f'{sizes[i]:.1f}%'
    ax.text(x, y, percentage, horizontalalignment='center', verticalalignment='center', fontsize=16, fontweight='bold')

# Draw straight lines connecting the labels to their segments
for i, (wedge, label) in enumerate(zip(wedges, labels)):
    ang = (wedge.theta2 - wedge.theta1) / 2. + wedge.theta1
    y = np.sin(np.deg2rad(ang)) * 0.95  # Adjusted to overlap slightly with the segment
    x = np.cos(np.deg2rad(ang)) * 0.95  # same
    xtext = np.cos(np.deg2rad(ang)) * 1.35
    ytext = np.sin(np.deg2rad(ang)) * 1.3
    horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
    ax.annotate(label, xy=(x, y), xytext=(xtext, ytext),
                horizontalalignment=horizontalalignment, 
                arrowprops=dict(arrowstyle="-", color='black'),
                fontsize=16.5, fontweight='bold', color='black',multialignment='center')

# Instead of ax.text that gives default, the title wasn't in the center...
# ...use fig.text to manually control the position of the center
fig.text(0.5, 0.85, 'Time Distribution of Processes in MOM6 Model', ha='center', fontsize=22, color='#1a658f', fontweight='bold')

# Subplot parameters to add more space at the top and bottom so figures stay in frame
fig.subplots_adjust(top=0.85, bottom=0.1, left=0.25, right=0.9)

fig.patch.set_facecolor('white')

plt.show()
