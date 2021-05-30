import airPlane
import airPlaneType
import trajectoryType
import debug
import entity

class Player(entity.Entity):
    """
    A player represent an user, his class contains
    the airplane that he control and trajectories chosen
    """

    def __init__(self, airPlaneType, x, y, orientation):
        """
        x, y : position in pixel in windows screen
        orientation: in degrees (0 to 360)
        """
        super().__init__(x, y, orientation)
        self.airPlane = airPlane.AirPlane(airPlaneType)
        self.trajectoryTypes = [None, None, None]

    def getAirPlane(self):
        """
        return user's airplane
        """
        return self.airPlane

    def __setTrajectoryType(self, index, trajType):
        """
        index: the order in which trajType will be played (1 to 3 inclued)
        """
        if 0 > index > 3:
            debug.warning("Player trajectory adding", index + " is not correct. Index need to be between 0 and 2.")
        else:
            self.trajectoryTypes[index] = trajType

    def getTrajectoryTypes(self):
        """
        return all trajectoryTypes
        """
        return self.trajectoryTypes

    def addTrajectoryType(self, trajectoryType):
        """
        add one trajectoryType to trajectoryType list
        """
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
