import debug

trajectoryTypes = {}

class Trajectory:
    """
    Mother class of all sub class in trajectoryType
    """

    def __init__(self, name, interval):
        self.name = name
        self.interval = interval
        trajectoryTypes[name] = self

    def getName(self):
        return self.name

    def walkX(self, x_abscisse):
        debug.warn("Trajectory", "This trajectory wasn't initialized")
        return 0

    def walkY(self, x_abscisse):
        debug.warn("Trajectory", "This trajectory wasn't initialized")
        return 0

    def getInterval(self):
        return self.interval
