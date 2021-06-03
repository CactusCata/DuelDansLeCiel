import airPlaneType
from time import time
import entity

class AirPlane(entity.Entity):
    """
    Represent the airplane which is drawned on the windows
    """

    def __init__(self, x, y, orientation, airPlaneType):
        super().__init__(x, y, orientation)
        self.airPlaneType = airPlaneType
        self.health = airPlaneType.getMaxHealth()
        self.lastShootTimestamp = 0
        self.refillAmmo()

    def getAirPlaneType(self):
        return self.airPlaneType

    def getHealth(self):
        return self.health

    def __setHealth(self, health):
        self.health = health

    def addDamage(self, damage):
        if self.getHealth() - damage <= 0:
            self.__setHealth(0)
        else:
            self.__setHealth(self.getHealth() - damage)

    def refillAmmo(self):
        self.setAmmo(self.getAirPlaneType().getMaxAmmo())

    def setAmmo(self, ammo):
        self.ammo = ammo

    def getAmmo(self):
        return self.ammo

    def shoot(self):
        """
        Update last time shoot and reduce ammo
        """
        self.lastShootTimestamp = time()
        self.setAmmo(self.getAmmo() - 1)

    def canShoot(self):
        return time() - self.lastShootTimestamp > self.getAirPlaneType().getShootFrequency() and self.getAmmo() != 0

    def kill(self):
        # What Is Dead May Never Die
        if not self.isDead():
            self.__setHealth(0)

    def isDead(self):
        return self.getHealth() == 0
