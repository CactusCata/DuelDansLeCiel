import airPlane
import airPlaneType
import trajectoryType
import debug
import entity

class Player(entity.Entity):

    def __init__(self, airPlaneType, x, y, orientation):
        super().__init__(x, y, orientation)
        self.airPlane = airPlane.AirPlane(airPlaneType)
        self.trajectoryTypes = [None, None, None]

    def getAirPlane(self):
        return self.airPlane

    def __setTrajectoryType(self, index, trajType):
        if 0 > index > 3:
            debug.warning("Player trajectory adding", index + " is not correct. Index need to be between 0 and 2.")
        else:
            self.trajectoryTypes[index] = trajType

    def getTrajectoryTypes(self):
        return self.trajectoryTypes

    def addTrajectoryType(self, trajectoryType):
        if not None in self.getTrajectoryTypes():
            debug.warning("Player trajectory adding", "Trajectory list is full.")
            return

        for i in range(len(self.getTrajectoryTypes())):
            if self.getTrajectoryTypes()[i] == None:
                self.__setTrajectoryType(i, trajectoryType)
                break


    def clearTrajectoryList(self):
        self.__setTrajectoryType(0, None)
        self.__setTrajectoryType(1, None)
        self.__setTrajectoryType(2, None)
