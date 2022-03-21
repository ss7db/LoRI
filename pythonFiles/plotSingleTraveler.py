import matplotlib.pyplot as plt
import numpy as np



labels = [1,2,3]
nav = [2.0037037037037035, 3.0055555555555555, 5.0092592592592595]
#systemweight = 
sInf = [2.0018518518518515, 3.0027777777777773, 5.004629629629629]
x = np.arange(len(labels))  # the label locations
width = 0.2  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, sInf, width, label='Strategic Information Design')
rects2 = ax.bar(x + width/2, nav, width, label='Navigation System')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Traveler Costs')
ax.set_title('Traveler Costs by method')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()

plt.show()