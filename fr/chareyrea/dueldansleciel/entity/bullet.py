from entity.entity import Entity
from utils.imageLoader import ImageLoader

# All bullets alive are registered here
bullets = []

# bullet's picture dimension
xDimensionsTexture = 18
yDimensionsTexture = 10
picturePath = "../../../textures/gameplay/bullet.png"

imageLoaded = None

class Bullet(Entity):

    def __init__(self, x, y, orientation=0):
        super().__init__(getImageLoaded(), x, y, orientation)
        bullets.append(self)

    def kill(self):
        bullets.remove(self)

    def isKilled(self):
        return not self in bullets

def getImageLoaded():
    global imageLoaded
    if imageLoaded == None:
        imageLoaded = ImageLoader(picturePath, xDimensionsTexture, yDimensionsTexture)
    return imageLoaded
