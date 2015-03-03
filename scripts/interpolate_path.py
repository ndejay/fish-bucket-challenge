#!/usr/bin/env python

import numpy as np
import sys

def interpolate(dat):
    out = []
    for i in range(len(dat)):
        x,y,r = dat[i]
        if x == -1:
            print i, len(dat)
            if i == 0 or i == len(dat) -1 :
                out.append([-1,-1,-1])
                continue
            if dat[i-1][0] == -1 or dat[i+1][0] == -1 :
                out.append([-1,-1,-1])
                continue
            out.append([(dat[i-1][0] + dat[i+1][0])/2.,(dat[i-1][1] + dat[i+1][1])/2. ,r])
        else:
            out.append([x, y, r])

    return out

if __name__ == "__main__":
    file_path = sys.argv[1]
    file_out_path = sys.argv[2]
    dat = np.loadtxt(file_path, delimiter = ',')

    out = interpolate(dat)

    np.savetxt(file_out_path, out, delimiter =',')
