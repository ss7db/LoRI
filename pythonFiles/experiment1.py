import random
import SInf

x = [i / 100 for i in range(0,110,10)]
sys_cost_with_diff_motives = []
for i in x:
    sys_cost_with_diff_motives.append(SInf.activeInactive(i)[1])
    print(sys_cost_with_diff_motives, i)

print(sys_cost_with_diff_motives)

