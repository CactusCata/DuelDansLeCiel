import libs.cng as cng

class Entity():
    """
    Represent a bullet or an airplane
    """

    def __init__(self, imageLoaded, x=0, y=0, orientation=0):
        self.x = x
        self.y = y
        self.orientation = orientation
        self.imageLoaded = imageLoaded

    def setX(self, x):
        self.x = x

    def getX(self):
        return self.x

    def setY(self, y):
        self.y = y

    def getY(self):
        return self.y

    def setOrientation(self, orientation):
        self.orientation = orientation % 360

    def getOrientation(self):
        return self.orientation

    def draw(self):
        """
        return imgDrawnPID
        """
        return cng.image_draw(self.getX(), self.getY(), self.imageLoaded.getImageLoaded())

    # Override entity function
    def drawOrientation(self, imgDrawnPID, orientation=-1):
        """
        imgDrawnPID : result of draw(...)
        """
        if orientation == -1:
            orientation = self.getOrientation()
        return cng.image_rotate(self.imageLoaded.getImageLoaded(), imgDrawnPID, orientation)

    def getHitBox(self):
        """
        reprensent the box:
        +--------+
        |0      1|
        |        |
        |2      3|
        +--------+
        """
        return ((self.getX() - 0.5 * self.imageLoaded.getDimX(), self.getY() - 0.5 * self.imageLoaded.getDimY()),
            (self.getX() + 0.5 * self.imageLoaded.getDimX(), self.getY() - 0.5 * self.imageLoaded.getDimY()),
            (self.getX() + 0.5 * self.imageLoaded.getDimX(), self.getY() + 0.5 * self.imageLoaded.getDimY()),
            (self.getX() - 0.5 * self.imageLoaded.getDimX(), self.getY() + 0.5 * self.imageLoaded.getDimY()))


    def __str__(self):
     return "x:" + str(self.x) + " y:" + str(self.y) + " angle:" + str(self.orientation)
