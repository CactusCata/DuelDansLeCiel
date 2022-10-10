from trajectories.trajectory import Trajectory
import chapter.game.gameEvent as gameEvent
from math import sin, cos, tan, atan, pi

# Represent the amount of drawning steps in a trajectoryType
INTERVAL_COUNT = 50

class VirageDroite(Trajectory):
    def __init__(self):
        super().__init__(gameEvent.trajectoriesName[0], intervalNegative(pi - 0.01, (2 * pi) / 3, INTERVAL_COUNT))

    def walkX(self, x_abscisse):
        return 260 * cos(x_abscisse) + 260

    def walkY(self, x_abscisse):
        return 230 * sin(x_abscisse)

class VirageGauche(Trajectory):
    def __init__(self):
        super().__init__(gameEvent.trajectoriesName[1], intervalPositive(0, pi / 3, INTERVAL_COUNT))

    def walkX(self, x_abscisse):
        return 260 * cos(x_abscisse) - 260

    def walkY(self, x_abscisse):
        return 230 * sin(x_abscisse)

class Ligne(Trajectory):
    def __init__(self):
        super().__init__(gameEvent.trajectoriesName[2], intervalPositive(0, 1, INTERVAL_COUNT))

    def walkX(self, x_abscisse):
        return x_abscisse

    def walkY(self, x_abscisse):
        return x_abscisse * 150

class GlissageDroite(Trajectory):
    def __init__(self):
        super().__init__(gameEvent.trajectoriesName[3], intervalPositive(tan(-1), tan(1), INTERVAL_COUNT))

    def walkX(self, x_abscisse):
        return atan(x_abscisse) * 50 + 50

    def walkY(self, x_abscisse):
        return x_abscisse * 64.2 + 100

class GlissageGauche(Trajectory):
    def __init__(self):
        super().__init__(gameEvent.trajectoriesName[4], intervalPositive(tan(-1), tan(1), INTERVAL_COUNT))

    def walkX(self, x_abscisse):
        return atan(x_abscisse) * 50 + 50

    def walkY(self, x_abscisse):
        return -(x_abscisse * 64.2 + 100)

def initTrajectories():
    """
    This initialization allows to register all differents
    trajectoryType
    """
    VirageDroite()
    VirageGauche()
    GlissageDroite()
    GlissageGauche()
    Ligne()

def intervalPositive(start, end, time):
    array = []
    pas = (end - start) / time
    while start < end:
        array += [start]
        start += pas
    return array

def intervalNegative(start, end, time):
    array = []
    pas = (start - end) / time
    while end < start:
        array += [start]
        start -= pas
    return array
