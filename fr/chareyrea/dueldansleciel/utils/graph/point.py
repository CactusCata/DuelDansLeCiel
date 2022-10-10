class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def copy(self):
        return Point(self.getX(), self.getY())

    def __str__(self):
        return "x: " + str(self.getX()) + " y: " + str(self.getY())
