
def cost(traveler, system):
    tr_per = traveler*0.07271
    system_per = system*0.242759
    return traveler+tr_per, system+system_per

print(cost(5.503, 19.851))

