# libraries
import numpy as np
import matplotlib.pyplot as plt
 
# set width of bars
barWidth = 0.20
 
# set heights of bars
# compas_sex = [-0.135, -0.27, -0.08]
# auditor_sex = [-0.05, 0.12, -0.003]
# compas_race = [-0.132, -0.26, -0.09]
# auditor_race = [-0.02, 0.08, 0.09]

# adult_sex = [-0.196, 0.45, 0.01]
# auditor_sex = [0.02, 0.01, 0.01]
# adult_race = [-0.103, 0.22, -0.06]
# auditor_race = [-0.05, 0.01, 0.01]

navTrav = [5.502777777777778]
nav_trav_v_3 = [3.8249749455768565]
#navSys = [23.001234567901236, 23.001234567901236, 23.001234567901236, 23.001234567901236, 23.001234567901236]
navSys = [23.001234567901236]
nav_sys_v_3 = [23.262720097146314]

#sInfTrav = [4.666666666666667, 5.084722222222222, 5.502777777777777, 5.920833333333334, 6.338888888888889]
sInfTrav = [5.502777777777778]
sInf_trav_v_3 = [4.397785545536799]
#sInfSys = [19.850864197530864, 19.850864197530864, 19.850864197530864, 19.850864197530864, 19.850864197530864]
sInfSys = [19.850864197530864]
sInf_sys_v_3 = [19.995451092117737]
# Set position of bar on X axis
r1 = np.arange(len(navSys))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
r4 = [x + barWidth for x in r3]
 
# Make the plot
plt.bar(r1, sInf_trav_v_3, color='#768fff', width=barWidth, edgecolor='white', label='Traveler cost: LoRI')
plt.bar(r2, nav_trav_v_3, color='#2962ff', width=barWidth, edgecolor='white', label='Traveler cost: SSSP')
plt.bar(r3, sInf_sys_v_3, color='#ff867c', width=barWidth, edgecolor='white', label='System cost: LoRI')
plt.bar(r4, nav_sys_v_3, color='#d50000', width=barWidth, edgecolor='white', label='System cost: SSSP')

ax = plt.gca()
for container in ax.containers:
    plt.bar_label(container, fontsize = 15)
# Add xticks on the middle of the group bars
plt.xlabel('Agents Costs', fontweight='bold', fontsize = 20)
plt.xticks([],[])
# plt.xticks([r + barWidth + 0.1 for r in range(len(navSys))], ['Statistical Parity', 'Equal Opportunity', 'Calibration'])
plt.axhline(0, color='black', linewidth = 0.50)

# lst = [-0.13, -0.05, -0.13, -0.02, 0.15, 0.02, 0.15, 0.06, 0.08, 0.003, 0.1, -0.09]
# for index, value in enumerate(lst):
#     plt.text(x = value-0.5 , y = index+0.1, s = str(value))
# for i, v in enumerate(lst):
#     plt.text(lst[i] - 0.25, v + 0.01, str(v))
# Create legend & Show graphic
# plt.title('Traveler Costs')
plt.legend(loc = 2, prop = {'size': 15})
plt.show()