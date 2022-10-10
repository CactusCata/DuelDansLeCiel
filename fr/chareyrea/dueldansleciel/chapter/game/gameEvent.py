from event.event import Event
import chapter.renderer as renderer
import entity.bullet as bullet
import entity.player as player
import trajectories.trajectory as trajectory
from math import cos, sin, pi

trajectoriesName = ["virage a droite", "virage a gauche", "ligne droite", "glissade a droite", "glissade a gauche"]
trajectoriesSelectionKeyName = [('a', 'i'), ('e', 'p'), ('z', 'o'), ('d', 'm'), ('q', 'k')]
shootKeyName = ("space", "0")


def addPlayerTraj(player, trajName):
    player.addTrajectoryType(trajectory.getTrajectoryFromName(trajName))

def shootBullet(fromPlayer):
    airplane = fromPlayer.getAirplane()
    if airplane.canShoot() and renderer.getRenderer().gameState == 1:
        xBull = airplane.getX() + (airplane.getAirplaneType().getXDimension() + 1) * cos(airplane.getOrientation() * pi / 180 + pi / 2)
        yBull = airplane.getY() + (airplane.getAirplaneType().getYDimension() + 1) * sin(airplane.getOrientation() * pi / 180 + pi / 2)
        bullet.Bullet(xBull, yBull, airplane.getOrientation())
        airplane.shoot()

class EventPressKeyA(Event):
    def __init__(self):
        super().__init__(trajectoriesSelectionKeyName[0][0])

    def func(self):
        addPlayerTraj(player.getPlayer1(), trajectoriesName[0])

class EventPressKeyE(Event):
    def __init__(self):
        super().__init__(trajectoriesSelectionKeyName[1][0])

    def func(self):
        addPlayerTraj(player.getPlayer1(), trajectoriesName[1])

class EventPressKeyZ(Event):
    def __init__(self):
        super().__init__(trajectoriesSelectionKeyName[2][0])

    def func(self):
        addPlayerTraj(player.getPlayer1(), trajectoriesName[2])

class EventPressKeyD(Event):
    def __init__(self):
        super().__init__(trajectoriesSelectionKeyName[3][0])

    def func(self):
        addPlayerTraj(player.getPlayer1(), trajectoriesName[3])

class EventPressKeyQ(Event):
    def __init__(self):
        super().__init__(trajectoriesSelectionKeyName[4][0])

    def func(self):
        addPlayerTraj(player.getPlayer1(), trajectoriesName[4])

class EventPressKeySpace(Event):
    def __init__(self):
        super().__init__(shootKeyName[0])

    def func(self):
        shootBullet(player.getPlayer1())

 # Player 2 selection

class EventPressKeyI(Event):
    def __init__(self):
        super().__init__(trajectoriesSelectionKeyName[0][1])

    def func(self):
        addPlayerTraj(player.getPlayer2(), trajectoriesName[0])

class EventPressKeyP(Event):
    def __init__(self):
        super().__init__(trajectoriesSelectionKeyName[1][1])

    def func(self):
        addPlayerTraj(player.getPlayer2(), trajectoriesName[1])

class EventPressKeyO(Event):
    def __init__(self):
        super().__init__(trajectoriesSelectionKeyName[2][1])

    def func(self):
        addPlayerTraj(player.getPlayer2(), trajectoriesName[2])

class EventPressKeyM(Event):
    def __init__(self):
        super().__init__(trajectoriesSelectionKeyName[3][1])

    def func(self):
        addPlayerTraj(player.getPlayer2(), trajectoriesName[3])

class EventPressKeyK(Event):
    def __init__(self):
        super().__init__(trajectoriesSelectionKeyName[4][1])

    def func(self):
        addPlayerTraj(player.getPlayer2(), trajectoriesName[4])

class EventPressKeyZero(Event):
    def __init__(self):
        super().__init__(shootKeyName[1])

    def func(self):
        shootBullet(player.getPlayer2())
