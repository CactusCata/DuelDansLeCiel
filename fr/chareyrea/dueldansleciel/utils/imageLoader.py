import libs.cng as cng

class ImageLoader():

    def __init__(self, path, dimX=None, dimY=None):
        self.path = path
        self.dimX = dimX
        self.dimY = dimY
        self.load()

    def load(self):
        """
        Picture is just loader now, if you want to draw it,
        you need to call draw function
        """
        self.img = cng.image(self.path, self.getDimX(), self.getDimY())

    def getImageLoaded(self):
        return self.img

    def getDimX(self):
        return self.dimX

    def getDimY(self):
        return self.dimY
