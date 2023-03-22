import matplotlib.pyplot as plt
import numpy as np



labels = [0]

#navTrav = [4.666666666666667, 5.084722222222222, 5.502777777777777, 5.920833333333334,6.338888888888889]
navTrav = [1.26219394]
#navSys = [23.001234567901236, 23.001234567901236, 23.001234567901236, 23.001234567901236, 23.001234567901236]
navSys = [23.001234567901236]

#sInfTrav = [4.666666666666667, 5.084722222222222, 5.502777777777777, 5.920833333333334, 6.338888888888889]
sInfTrav = [5.502777777777778]

#sInfSys = [19.850864197530864, 19.850864197530864, 19.850864197530864, 19.850864197530864, 19.850864197530864]
sInfSys = [19.850864197530864]

bidiTrav = [1.26219394]



x = np.arange(len(labels))  # the label locations
width = 0.2  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, sInfTrav, width, label='Traveler Cost: LoRI')
rects2 = ax.bar(x + width/2, navTrav, width, label='Traveler Cost: SSSP')
rects3 = ax.bar(x + width, sInfSys, width, label='System Cost: LoRI')
rects4 = ax.bar(x + width+width/2, navSys, width, label='System Cost: SSSP')


# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Cost')
# ax.set_xlabel('')
# ax.set_title('Cost for different methods')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)
ax.bar_label(rects3, padding=3)
ax.bar_label(rects4, padding=3)

fig.tight_layout()

plt.show()