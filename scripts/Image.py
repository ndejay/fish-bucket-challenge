from skimage.color import rgb2gray
from skimage.io import imread
from skimage.io import imsave
from skimage.feature import blob_dog
import matplotlib.pyplot as plt
import numpy as np

class Image(object):
    img = []
    blobs = []

    def __init__(self, img, blobs = None):
        self.img = img
        if blobs != None:
            self.blobs = blobs

    def load(self, filename):
        self.img = imread(filename)

    def saveImage(self, filename):
        imsave(filename, self.img)

    def saveFig(self, filename):
        fig, ax = plt.subplots(1, 1)
        ax.imshow(self.image)
        for blob in blobs:
            y, x, r = blob
            c = plt.Circle((x, y), r, linewidth = 2, color = 'red')
            ax.add_patch(c)
        fig.savefig(filename)

    def saveBlobs(self, filename):
	    np.savetxt(filename, self.blobs, delimiter = ",")

    def gray(self):
        return Image(rgb2gray(self.img))

    def inverse(self):
        return Image(1 - self.img)

    def blobs(self, max_sigma, threshold):
        blobs = blob_dog(self.gray, max_sigma = max_sigma, threshold = threshold)
        blobs[:, 2] = blobs[:, 2] * sqrt(2)
        self.blobs = blobs

    def __sub__(self, image):
        return Image(self.img - image.image)

# vim: set ts=4 sw=4 sts=4 et :
