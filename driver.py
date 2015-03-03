#!/usr/bin/env python

import os
import sys

import scripts.produce_diff as diffs
import scripts.interpolate_fish_positions as ifp
import matplotlib.pyplot as plt

from scripts.Image import Image
from skimage.io import imread, imsave
from os.path import isfile, join

if __name__ == "__main__":
    folder = sys.argv[1]

    onlyfiles = [ f for f in os.listdir(folder) if isfile(join(folder,f)) and f.endswith(".png") ]
    imgs = map( lambda x : diffs.to_grayscale(imread(x)).astype(float), [ os.path.join(folder ,  "%04d.png" % nb) for nb in range(1,len(onlyfiles)+1) ] )

    # reverse them so we can start from the end
    baselined_diffs = list(reversed(diffs.get_all_baseline(imgs[0], imgs)))

    print len(baselined_diffs)

    frames = []
    for b in baselined_diffs[1:]:
        print b
        imsave('data/wat.png', b)
        bl = Image(b).make_blobs(3, 0.1).blobs
        print bl
        frames.append(bl)
        break

    # keep pulling off the first element if it has no blobs
    while not len(frames[0]):
        frames.pop(0)

    traj = ifp.compute_trajectory(frames, ifp.maximum_outlier(frames[0]))

    print list(reversed(traj))
