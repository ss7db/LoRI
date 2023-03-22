import matplotlib.pyplot as plt
import numpy as np



labels = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9, 1]
nav = [5.064814814814815, 5.064814814814815, 5.064814814814815]
#systemweight = 
sInf = [12.006481481481481, 12.006481481481481
x = np.arange(len(labels))  # the label locations
width = 0.2  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, sInf, width, label='Strategic Information Design')
rects2 = ax.bar(x + width/2, nav, width, label='Navigation System')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Costs')
ax.set_title('Costs by method')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()

plt.show()