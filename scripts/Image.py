from skimage.color import rgb2gray
from scipy.misc import imread, imsave
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
        a = fig.gca()
        a.set_frame_on(False)
        a.set_xticks([])
        a.set_yticks([])
        plt.axis('off')
        ax.set_frame_on(False)
        ax.imshow(self.img)
        for blob in self.blobs:
            y, x, r = blob
            c = plt.Circle((x, y), r, linewidth = 2, color = 'red')
            ax.add_patch(c)
        dpi = 100
        fig.set_size_inches(self.img.shape[0] / dpi, self.img.shape[1] / dpi)
        fig.savefig(filename, bbox_inches = 'tight', pad_inches= 0 )
        return self

    def saveBlobs(self, filename):
        np.savetxt(filename, self.blobs, delimiter = ",")
        return self

    def gray(self):
        return Image(rgb2gray(self.img))

    def inverse(self):
        return Image(1 - self.img)

    def make_blobs(self, min_sigma, max_sigma, threshold):
        try:
            blobs = blob_dog(self.img, min_sigma = min_sigma, max_sigma = max_sigma, threshold = threshold)
            blobs[:, 2] = blobs[:, 2] * sqrt(2)
            return Image(self.img, blobs)
        except:
            return self

    def __sub__(self, image):
        return Image(self.img- image.img)

    def __add__(Self, image):
        return Image((self.img+ image.img) / 2)

# vim: set ts=4 sw=4 sts=4 et :
