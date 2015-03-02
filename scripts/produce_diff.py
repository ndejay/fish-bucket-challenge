#usage: python produce_diff.py foldername
from os import listdir
from os.path import isfile, join
import sys
import os
import numpy as np

from scipy.misc import imread, imsave
from scipy.linalg import norm
from scipy import sum, average



def to_grayscale(arr):
    "If arr is a color image (3D array), convert it to grayscale (2D array)."
    if len(arr.shape) == 3:
        return average(arr, -1)  # average over the last axis (color channels)
    else:
        return arr


folder = sys.argv[1]


# read images as 2D arrays (convert to grayscale for simplicity)
onlyfiles = [ f for f in os.listdir(folder) if isfile(join(folder,f)) and f.endswith(".png") ]
imgs = map( lambda x : to_grayscale(imread(x)).astype(float), [ os.path.join(folder ,  "%04d.png" % nb) for nb in range(1,len(onlyfiles)+1) ] )


def compare_images(img1, img2):
    diff = img1 - img2  # elementwise for scipy arrays
    diff[diff <= 0 ] = 0
    return diff 

diffs=[]
for i in range(0,len(imgs)-1):
	diffs.append( compare_images(imgs[i], imgs[i+1]))

all_stuff = np.max(diffs, axis=0)
all_stuff = all_stuff #/ np.max(all_stuff)
print folder



#imsave("results/out%04d.png" % nb  ,diff)
imsave("results/sum_%s.png" % folder.split('/')[-1] ,all_stuff)



