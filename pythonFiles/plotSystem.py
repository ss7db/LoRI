from wsgiref.simple_server import sys_version
import matplotlib.pyplot as plt
import numpy as np
#new
navMixed = [23.262720097146314]*11
sInfMixed = [12.5, 13.550105820105822, 14.60021164021164, 15.650317460317462, 16.700423280423284, 17.7505291005291, 18.800634920634923, 19.850740740740743, 20.900846560846563, 21.950952380952373, 23.001058201058203]
sInf0 = [12.5, 13.550154320987652, 14.60030864197531, 15.650462962962962, 16.700617283950624, 17.750771604938272, 18.80092592592592, 19.851080246913583, 20.901234567901234, 21.951388888888882, 23.001543209876544]
sInf025 = [12.5, 13.550105820105822, 14.60021164021164, 15.650317460317462, 16.700423280423284, 17.7505291005291, 18.800634920634923, 19.850740740740743, 20.900846560846563, 21.950952380952373, 23.001058201058203]
sInf050 = [12.5, 13.550105820105822, 14.60021164021164, 15.650317460317462, 16.700423280423284, 17.7505291005291, 18.800634920634923, 19.850740740740743,20.900846560846563, 21.950952380952373, 23.001058201058203 ]
sInf075 = []
nav_version_3 = [23.262720097146314]*11
sinf_version_3 = [12.5, 13.570778727445376, 14.6415574548908, 15.712336182336186, 16.7831149097816, 17.853893637226975, 18.92467236467236, 19.995451092117737, 21.06622981956317, 22.137008547008556, 23.20778727445393]
labels = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]

#old,
#nav = [23.00138888888889]*11
#systemweight = 
#sInf = [12.5, 13.550092592592593, 14.600185185185186, 15.650277777777777, 16.700370370370372, 17.750462962962963, 18.800555555555555, 19.850648148148146, 20.900740740740744, 21.95083333333333, 23.000925925925927]
x = np.arange(len(labels))  # the label locations
width = 0.4  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x + width/2, sinf_version_3, width, label='LoRI')
plt.plot(nav_version_3, linestyle='-', marker='o', color='green', label='SSSP')
# plt.plot(sInfMixed, linestyle='-', marker='o', color='brown', label='SInf Mixed')
# plt.plot(sInf0, linestyle='-', marker='o', color='red', label='SInf 0')
# plt.plot(sInf025, linestyle='-', marker='o', color='blue', label='SInf 025')
# plt.plot(sInf050, linestyle='-', marker='o', color='yellow', label='SInf 050')



# rects2 = ax.bar(x + width/2, nav, width, label='Navigation System')
plt.legend()
# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('System Cost' , fontsize = 20)
ax.set_xlabel('System Motive', fontsize = 20)
# ax.set_title('Costs by method')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend(prop = {'size': 21})

ax.bar_label(rects1, padding=3, fontsize = 18)
# plt.ylabel(23.008333333333333)
# ax.bar_label(rects2, padding=3)

fig.tight_layout()

plt.show()