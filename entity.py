import debug

class Entity():

    def __init__(self, x, y, orientation):
        self.x = x
        self.y = y
        self.orientation = orientation

    def setX(self, x):
        self.x = x

    def getX(self):
        return self.x

    def setY(self, y):
        self.y = y

    def getY(self):
        return self.y

    def setOrientiation(self, orientation):
        self.orientation = orientation % 360

    def getOrientation(self):
        return self.orientation

    def __str__(self):
     return "x:" + str(self.x) + " y:" + str(self.y) + " angle:" + str(self.orientation) 
