from skimage.color import rgb2gray
from skimage.io import imread
from skimage.io import imsave
from skimage.feature import blob_dog
from math import sqrt
import matplotlib.pyplot as plt
import numpy as np

class Image(object):
    img   = []
    blobs = []

    def __init__(self, img = [], blobs = None):
        self.img = img
        if blobs != None:
            self.blobs = blobs

    def load(self, filename):
        self.img = imread(filename)
        return self

    def saveImage(self, filename):
        imsave(filename, self.img)
        return self

    def saveFig(self, filename):
        fig, ax = plt.subplots(1, 1)
        ax.imshow(self.img)
        for blob in self.blobs:
            y, x, r = blob
            c = plt.Circle((x, y), r, linewidth = 2, color = 'red')
            ax.add_patch(c)
        fig.savefig(filename)
        return self

    def saveBlobs(self, filename):
        np.savetxt(filename, self.blobs, delimiter = ",")
        return self

    def gray(self):
        return Image(rgb2gray(self.img))

    def inverse(self):
        return Image(1 - self.img)

    def blobs(self, max_sigma, threshold):
        blobs = blob_dog(self.gray().img, max_sigma = max_sigma, threshold = threshold)
        blobs[:, 2] = blobs[:, 2] * sqrt(2)
        return Image(self.img, blobs)

    def __sub__(self, image):
        return Image(self.img- image.img)

    def __add__(Self, image):
        return Image((self.img+ image.img) / 2)

# vim: set ts=4 sw=4 sts=4 et :
