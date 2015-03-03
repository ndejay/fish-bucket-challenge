
class Image(object):
    img
    blobs = []

    def __init__(self, img, blobs = None):
        self.img = img
        if blobs != None:
            self.blobs = blobs

    def load(self, filename):
        self.img = skimage.io.imread(filename)

    def saveImage(self, filename):
        skimage.io.imsave(filename, img)

    def saveFig(self, filename):
        fig, ax = pyplot.matplotlib.subplots(1, 1)
        ax.imshow(self.image)
        for blob in blobs:
            y, x, r = blob
            c = plt.Circle((x, y), r, linewidth = 2, color = 'red')
            ax.add_patch(c)
        fig.savefig(filename) 

    def saveBlobs(self, filename):
	    numpy.savetxt(filename, self.blobs, delimiter = ",")

    def gray(self):
        return Image(skimage.color.rgb2gray(self.img))
    
    def inverse(self):
        return Image(1 - self.img)

    def blobs(self, max_sigma, threshold):
        blobs = skimage.feature.blob_dog(self.gray, max_sigma = max_sigma, threshold = threshold)
        blobs[:, 2] = blobs[:, 2] * sqrt(2)
        return Image(self.img, blobs)

    def __sub__(self, image):
        return Image(self.img - image.image)

# vim: set ts=4 sw=4 sts=4 et :
