#this plot is an example of the dream version of a plot to show time distribution for processes (EXPLORATORY, NOT THE PLOT USED IN DELIVERABLES)
#plot to show signficant IO time -> motivation of DART-NUOPC Cap
#https://www.tutorialspoint.com/execute_matplotlib_online.php

import matplotlib.pyplot as plt
import numpy as np

# from JSON (matches profiling display so use this directly)
activity_data = {
    "main_thread": {
        "CPU": [50, 45, 55, 60],
        "File I/O": [20, 25, 18, 15],
        "MPI": [10, 10, 12, 10],
        "Wait Time": [20, 20, 15, 15]
    }
}

# the average percentage of time for each activity
activities = ["CPU", "File I/O", "MPI", "Wait Time"]
average_times = {activity: np.mean(times) for activity, times in activity_data["main_thread"].items()}

# Data for the pie chart
labels = list(average_times.keys())
sizes = list(average_times.values())
colors = ['green', '#f18930', '#5A4FCF', '#C0C0C0']

fig, ax = plt.subplots(figsize=(10, 7))

# plot the pie chart (without labels for now)
wedges, texts, autotexts = ax.pie(sizes, labels=None, colors=colors, autopct='',
                                  startangle=140, pctdistance=0.85)

# annotate percentages manually to ensure they are in the center of each segment
for i, wedge in enumerate(wedges):
    ang = (wedge.theta2 - wedge.theta1) / 2. + wedge.theta1
    y = np.sin(np.deg2rad(ang)) * 0.7  # Adjust the factor to position text closer to center
    x = np.cos(np.deg2rad(ang)) * 0.7  # adjust the factor to position text closer to center
    percentage = f'{sizes[i]:.1f}%'
    ax.text(x, y, percentage, horizontalalignment='center', verticalalignment='center', fontsize=16, fontweight='bold')

# Draw straight lines connecting the labels to their segments
for i, (wedge, label) in enumerate(zip(wedges, labels)):
    ang = (wedge.theta2 - wedge.theta1) / 2. + wedge.theta1
    y = np.sin(np.deg2rad(ang)) * 0.95  # Adjusted to overlap slightly with the segment
    x = np.cos(np.deg2rad(ang)) * 0.95  # Adjusted to overlap slightly with the segment
    xtext = np.cos(np.deg2rad(ang)) * 1.3
    ytext = np.sin(np.deg2rad(ang)) * 1.3
    horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
    ax.annotate(label, xy=(x, y), xytext=(xtext, ytext),
                horizontalalignment=horizontalalignment, 
                arrowprops=dict(arrowstyle="-", color='black'),
                fontsize=15.6, fontweight='bold', color='black')

# instead of ax.text that gives default, the title wasnt in the center...
#...use fig.text to manually control the position of the center
fig.text(0.55, 0.94, 'Time Distribution of Processes in MOM6 Model', ha='center', fontsize=20, color='#1a658f', fontweight='bold')

# subplot parameters to add more space at the top n bottom so figures stay in frame
fig.subplots_adjust(top=0.85, bottom=0.1)

fig.patch.set_facecolor('white')

plt.show()
