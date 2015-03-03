#usage: python produce_diff.py foldername
#or this: ls ../data/frames/jerrington.me\:15000/ | while read i ; do echo $i ; mkdir -p ../results_base/"$i"; python produce_diff.py "../data/frames/jerrington.me:15000/$i" ; done
from os import listdir
from os.path import isfile, join
import sys
import os
import numpy as np

from scipy.misc import imread, imsave
from scipy import average



def to_grayscale(arr):
    "If arr is a color image (3D array), convert it to grayscale (2D array)."
    if len(arr.shape) == 3:
        return average(arr, -1)  # average over the last axis (color channels)
    else:
        return arr

def get_one_baseline(base_img, other_img):
    diff = base_img - other_img  # elementwise for scipy arrays
    diff[diff <= 0 ] = 0
    return diff

def get_all_baseline(base_img, other_imgs):
    return map(lambda x : get_one_baseline(base_img, x), other_imgs )


if __name__ == "__main__":
    folder = sys.argv[1]
    # read images as 2D arrays (convert to grayscale for simplicity)
    onlyfiles = [ f for f in os.listdir(folder) if isfile(join(folder,f)) and f.endswith(".png") ]
    imgs = map( lambda x : to_grayscale(imread(x)).astype(float), [ os.path.join(folder ,  "%04d.png" % nb) for nb in range(1,len(onlyfiles)+1) ] )
    diffs = []
    for i in range(0,len(imgs)-1):
        diffs.append( get_one_baseline(imgs[0], imgs[i]))
        imsave("../results_base/%s/out%04d.png" % (os.path.basename(folder),i)  ,diffs[-1])
    all_stuff = np.max(diffs, axis=0)
    all_stuff = all_stuff #/ np.max(all_stuff)
    print folder
    imsave("../results_base/%s/sum.png" % os.path.basename(folder) ,all_stuff)



