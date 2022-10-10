class AirplaneType:

    def __init__(self, name, path, dimX, dimY, maxHealth, maxAmmo, shootFrequency):
        self.name = name
        self.path = path
        self.dimX = dimX
        self.dimY = dimY
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

    def getMaxAmmo(self):
        return self.maxAmmo

    def getMaxHealth(self):
        return self.maxHealth

    def getShootFrequency(self):
        return self.shootFrequency

def getAirplaneTypeFromName(airPlaneName):
    return getAirPlanesTypes()[airPlaneName]

def getAirplanesTypes():
    return [AirplaneType("albatros", "../../../textures/gameplay/albatros.png", 80, 80, 60, 20, 0.2),
        AirplaneType("fokker", "../../../textures/gameplay/fokker.png", 80, 80, 50, 10, 0.15),
        AirplaneType("sopwith", "../../../textures/gameplay/sopwith.png", 80, 80, 40, 50, 0.1),
        AirplaneType("spad", "../../../textures/gameplay/spad.png", 80, 80, 100, 5, 0.02)]
