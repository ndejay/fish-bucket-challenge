#!/usr/bin/env python

import os
import sys

import numpy as np
import scripts.produce_diff as diffs
import scripts.interpolate_fish_positions as ifp
import matplotlib.pyplot as plt

from scripts.Image import Image
from scipy.misc import imread, imsave
from os.path import isfile, join
from skimage.color import rgb2gray

def _flip( (x, y) ):
    return (y, x)

if __name__ == "__main__":
    folder = sys.argv[1]
    output_file = sys.argv[2]

    onlyfiles = sorted([ f for f in os.listdir(folder) if isfile(join(folder,f)) and f.endswith(".png") ])
    imgs = map( lambda x : rgb2gray(imread(x)).astype(float), [ os.path.join(folder ,  "static_%04d.png" % nb) for nb in range(1,len(onlyfiles)+1) ] )

    # reverse them so we can start from the end
    baselined_diffs = diffs.get_all_baseline(imgs[0], imgs)

    print len(baselined_diffs)

    frames = []
    for i, b in enumerate(baselined_diffs):
        blobs = Image(b).make_blobs(2, 5, 0.02)
        bl = blobs.blobs
        print len(bl)
        frames.append(bl)

    pre_traj = [] # the skipped frames on the beginning.

    # keep pulling off the first element if it has no blobs
    while not len(frames[-1]):
        print "skipped a frame"
        pre_traj.append( (-1, -1, -1) )
        frames.pop(-1)

    traj = pre_traj + ifp.compute_trajectory(frames, ifp.maximum_outlier(frames[-1]))

    np.savetxt(output_file, traj, delimiter=',')

    #fig = plt.figure()
    #ax = fig.add_subplot(1, 1, 1)
    #ax.set_ylim(bottom=480, top=0)
    #ax.set_xlim(left=0, right=640)
    #ax.plot(*zip(*map(lambda x: _flip(x[:2]), traj)))
    #fig.savefig('data/asdf.png')
