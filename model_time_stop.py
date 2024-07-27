#plot in python to get visuals for motivation of the DART-NUOPC cap project
#https://www.tutorialspoint.com/execute_matplotlib_online.php

import matplotlib.pyplot as plt

# data from Helen
model_runs = ['1 day', '2 days', '5 days', '10 days']
times = [102, 136, 164, 206]

# time cost per day
time_costs_per_day = [times[0], times[1] / 2, times[2] / 5, times[3] / 10]

# plot
plt.figure(figsize=(10, 6))
plt.plot(model_runs, time_costs_per_day, marker='o', linestyle='-', color='b', label='MOM6 Time Cost per Day')
plt.xlabel('Model Run Length until Stopping', fontsize=15, fontweight='bold', labelpad=13)
plt.ylabel('Time Cost per Day (s)', fontsize=15, fontweight='bold', labelpad=13)
plt.title('Time Cost of Model Stopping ', fontsize=20, fontweight='bold', pad=20)
plt.xticks(fontsize=13)
plt.yticks(fontsize=13)
plt.grid(True)
plt.legend()

# adjust layout to fit everything in
plt.tight_layout(pad=3.0)
plt.subplots_adjust(top=0.85)

plt.show()
