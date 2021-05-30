from trajectory import trajectoryTypes as traj
import debug

class AirPlaneType:

    def __init__(self, name, path, dimX, dimY, trajectories, maxHealth, maxAmmo, shootFrequency):
        self.name = name
        self.path = path
        self.dimX = dimX
        self.dimY = dimY
        self.trajectories = trajectories
        self.maxHealth = maxHealth
        self.maxAmmo = maxAmmo
        self.shootFrequency = shootFrequency

    def getName(self):
        return self.name

    def getPath(self):
        return self.path

    def getXDimension(self):
        return self.dimX

    def getYDimension(self):
        return self.dimY

    def getTrajectories(self):
        return self.trajectories

    def getMaxAmmo(self):
        return self.maxAmmo

    def getMaxHealth(self):
        return self.maxHealth

    def getShootFrequency(self):
        return self.shootFrequency

def getAirPlanesTypes():
    return {
        "albatros": AirPlaneType("albatros", "textures/gameplay/albatros.png", 80, 80, [traj["virage a droite"], traj["virage a gauche"]], 60, 20, 0.2),
        "fokker": AirPlaneType("fokker", "textures/gameplay/fokker.png", 80, 80, [traj["virage a droite"]], 50, 10, 0.15),
        "sopwith": AirPlaneType("sopwith", "textures/gameplay/sopwith.png", 80, 80, [traj["virage a droite"]], 40, 50, 0.1),
        "spad": AirPlaneType("spad", "textures/gameplay/spad.png", 80, 80, [traj["virage a droite"]], 100, 5, 0.02)
    }
