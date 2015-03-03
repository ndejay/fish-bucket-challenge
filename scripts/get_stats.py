import math

import numpy as np

def get_speeds(pos):
    """Give non normalized distance"""
    dist = lambda x1,y1,x2,y2 : math.sqrt((float(x2)-float(x1))**2 + (float(y2)-float(y1))**2)
    speeds = []
    for i in range(len(pos)-1):
        speeds.append(dist(pos[i][0],pos[i][1],pos[i+1][0],pos[i+1][1]))
    return speeds
   
def get_avg_speed(pos):
    speeds = get_speeds(pos)
    return np.sum(speeds)/len(speeds)

if __name__ == "__main__":
    data = np.loadtxt("../data/points/dataresults_base22022015 F7B18 HS 60 No Tg_1.avi5",delimiter = ',')
    print get_speeds(data) 
    print get_avg_speed(data)
