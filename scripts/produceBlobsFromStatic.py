#!/usr/bin/env python
from matplotlib import pyplot as plt
from skimage import data
from skimage.feature import blob_dog, blob_log, blob_doh
from math import sqrt
from skimage.color import rgb2gray
import skimage
import os
import csv
import numpy as np
from skimage.feature import match_template

path = "/Users/wireless/git/fish-bucket-challenge/data/results_base/22022015 F7B18 HS 60 No Tg_10.avi/"
file_list = os.listdir("%s" % path)
#template = data.imread("/Users/wireless/git/fish-bucket-challenge/data/hand.png")

MIN_SIGMA = 4
MAX_SIGMA = 5
THRESHOLD = 0.04

for image_filename in file_list[1:]:
	print image_filename
	image = data.imread("%s/%s" % (path, image_filename))
	image_gray =  rgb2gray(image)
	max_sigma = 5
	fig, ax = plt.subplots(1, 1)
	blobs_dog = blob_dog(image_gray, min_sigma = MIN_SIGMA, max_sigma=MAX_SIGMA, threshold=THRESHOLD)
	blobs_dog[:, 2] = blobs_dog[:, 2] * sqrt(2)
	ax.imshow(image)#, interpolation = 'nearest')dd
	for blob in blobs_dog:
		y, x, r = blob
		c = plt.Circle((x, y), r, linewidth=2, color='red')
		ax.add_patch(c)
	#np.savetxt('/Users/wireless/git/fish-bucket-challenge/data/nd_diffs+blobs/%s_blobs.csv' % image_filename, blobs_dog, delimiter = ",")
	fig.savefig("%s/blob_%s" % (path, image_filename))
