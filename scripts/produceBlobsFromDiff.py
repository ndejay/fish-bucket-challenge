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

file_list = os.listdir("/Users/wireless/git/fish-bucket-challenge/data/nd_diffs/")
template = data.imread("/Users/wireless/git/fish-bucket-challenge/data/hand.png")

#i = 0
for image_filename in file_list:
	#print i
	#i += 1
	#if i != 19:
  #	continue
	print image_filename
	image = data.imread("/Users/wireless/git/fish-bucket-challenge/data/nd_diffs/%s" % image_filename)
	image_gray = rgb2gray(image)
	# MATCH FROM TEMPLATE
	result = match_template(image_gray, template)
	ij = np.unravel_index(np.argmax(result), result.shape)
	x, y = ij[::-1]
	fig, ax = plt.subplots(1, 1)
	hcoin, wcoin = template.shape
	rect = plt.Rectangle((x, y), wcoin, hcoin, edgecolor='r', facecolor='none')
	ax.add_patch(rect)
	# /MATCH FROM TEMPLATE
	max_sigma = 3
	#blobs_log = blob_log(image_gray, max_sigma=max_sigma, num_sigma=10, threshold=.1)
	# Compute radii in the 3rd column.
	#blobs_log[:, 2] = blobs_log[:, 2] * sqrt(2)
	# blobs_list = 
	#blobs_doh = blob_doh(image_gray, min_sigma=1, max_sigma=max_sigma, threshold=.01)
	blobs_dog = blob_dog(image_gray, max_sigma=max_sigma, threshold=.1)
	blobs_dog[:, 2] = blobs_dog[:, 2] * sqrt(2)
	ax.imshow(image)#, interpolation = 'nearest')
	fig.suptitle(np.max(result))
	for blob in blobs_dog:
		y, x, r = blob
		c = plt.Circle((x, y), r, linewidth=2, color='red')
		ax.add_patch(c)
	#np.savetxt('/Users/wireless/git/fish-bucket-challenge/data/nd_diffs+blobs/%s_blobs.csv' % image_filename, blobs_dog, delimiter = ",")
	fig.savefig("/Users/wireless/git/fish-bucket-challenge/data/nd_diffs+blobs/%s" % image_filename)
