import entity

bullets = []

xDimensionsTexture = 12
yDimensionsTexture = 12
picturePath = "textures/gameplay/bullet.png"

class Bullet(entity.Entity):

    def __init__(self, x, y, orientation):
        super().__init__(x, y, orientation)
        bullets.append(self)

    def kill(self):
        bullets.remove(self)

    def isKilled(self):
        return not self in bullets
