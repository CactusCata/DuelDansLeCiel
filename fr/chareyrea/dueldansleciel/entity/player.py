from entity.airplane.airplane import Airplane
import entity.airplane.airplaneType as airplaneType
import trajectories.trajectoryType as trajectoryType
import utils.debug as debug

player1 = None
player2 = None

def getPlayer1():
    return player1

def getPlayer2():
    return player2

class Player:
    """
    A player represent an user, his class contains
    the airplane that he control and trajectories chosen
    """

    def __init__(self, playerNumber):
        """
        x, y : position in pixel in windows screen
        orientation: in degrees (0 to 360)
        """
        if playerNumber == 1:
            global player1
            player1 = self
        elif playerNumber == 2:
            global player2
            player2 = self
        else:
            debug.error("instanciate player", "player number is not allowed (need to be 1 or 2)")
            exit()
        self.trajectoryTypes = [None, None, None]
        self.airplane = None

    def associateAirplane(self, imageLoader, x, y, orientation, airplaneType):
        self.airplane = Airplane(imageLoader, x, y, orientation, airplaneType)

    def getAirplane(self):
        """
        return user's airplane
        """
        return self.airplane

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
