#!/usr/bin/env python

import os
import sys

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

    onlyfiles = sorted([ f for f in os.listdir(folder) if isfile(join(folder,f)) and f.endswith(".png") ])
    imgs = map( lambda x : rgb2gray(imread(x)).astype(float), [ os.path.join(folder ,  "%04d.png" % nb) for nb in range(1,len(onlyfiles)+1) ] )

    # reverse them so we can start from the end
    baselined_diffs = diffs.get_all_baseline(imgs[0], imgs)

    print len(baselined_diffs)

    frames = []
    for i, b in enumerate(baselined_diffs[1:]):
        imsave('data/dump' + str(i) + '.png', b)
        blobs = Image(b).make_blobs(4, 5, 0.04)
        bl = blobs.blobs
        print len(bl)

        frames.append(bl)

    # keep pulling off the first element if it has no blobs
    while not len(frames[-1]):
        print "skipped a frame"
        frames.pop(-1)

    traj = ifp.compute_trajectory(frames, ifp.maximum_outlier(frames[-1]))

    print traj

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.set_ylim(bottom=480, top=0)
    ax.set_xlim(left=0, right=640)
    ax.plot(*zip(*map(lambda x: _flip(x[:2]), traj)))
    fig.savefig('data/asdf.png')
