import matplotlib.pyplot as plt
import numpy as np



labels = [1,2,3,4]
nav = [0.0011279582977294922, 0.002007007598876953, 0.002805948257446289, 0.0027680397033691406]
#systemweight = 
sInf = [0.24670171737670898, 0.41092681884765625, 2.2496159076690674, 909.9852938652039]
x = np.arange(len(labels))  # the label locations
width = 0.2  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, sInf, width, label='LoRI')
rects2 = ax.bar(x + width/2, nav, width, label='SSSP')

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