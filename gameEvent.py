import event
import graphicsGame
import bullet
import player
import trajectory
from math import cos, sin, pi

trajectoryNames = ["virage a droite", "virage a gauche", "ligne droite", "glissade a droite", "glissade a gauche"]
buttons = [('a', 'i'), ('e', 'p'), ('z', 'o'), ('d', 'm'), ('q', 'k')]

class EventPressKeyA(event.Event):
    def __init__(self):
        super().__init__(buttons[0][0])

    def func(self):
        player.getPlayer1().addTrajectoryType(trajectory.getTrajectoryFromName(trajectoryNames[0]))

class EventPressKeyE(event.Event):
    def __init__(self):
        super().__init__(buttons[1][0])

    def func(self):
        player.getPlayer1().addTrajectoryType(trajectory.getTrajectoryFromName(trajectoryNames[1]))

class EventPressKeyZ(event.Event):
    def __init__(self):
        super().__init__(buttons[2][0])

    def func(self):
        player.getPlayer1().addTrajectoryType(trajectory.getTrajectoryFromName(trajectoryNames[2]))

class EventPressKeyD(event.Event):
    def __init__(self):
        super().__init__(buttons[3][0])

    def func(self):
        player.getPlayer1().addTrajectoryType(trajectory.getTrajectoryFromName(trajectoryNames[3]))

class EventPressKeyQ(event.Event):
    def __init__(self):
        super().__init__(buttons[4][0])

    def func(self):
        player.getPlayer1().addTrajectoryType(trajectory.getTrajectoryFromName(trajectoryNames[4]))

class EventPressKeySpace(event.Event):
    def __init__(self):
        super().__init__("space")

    def func(self):
        airPlaneP1 = graphicsGame.player.getPlayer1().getAirPlane()
        if airPlaneP1.canShoot() and graphicsGame.gameState == 1:
            xBull = airPlaneP1.getX() + 81 * cos((airPlaneP1.getOrientation() * pi / 180) + pi / 2)
            yBull = airPlaneP1.getY() + 81 * sin((airPlaneP1.getOrientation() * pi / 180) + pi / 2)
            bullet.Bullet(xBull, yBull, airPlaneP1.getOrientation())
            airPlaneP1.shoot()

 # Player 2 selection

class EventPressKeyI(event.Event):
    def __init__(self):
        super().__init__(buttons[0][1])

    def func(self):
        player.getPlayer2().addTrajectoryType(trajectory.getTrajectoryFromName(trajectoryNames[0]))

class EventPressKeyP(event.Event):
    def __init__(self):
        super().__init__(buttons[1][1])

    def func(self):
        player.getPlayer2().addTrajectoryType(trajectory.getTrajectoryFromName(trajectoryNames[1]))

class EventPressKeyO(event.Event):
    def __init__(self):
        super().__init__(buttons[2][1])

    def func(self):
        player.getPlayer2().addTrajectoryType(trajectory.getTrajectoryFromName(trajectoryNames[2]))

class EventPressKeyM(event.Event):
    def __init__(self):
        super().__init__(buttons[3][1])

    def func(self):
        player.getPlayer2().addTrajectoryType(trajectory.getTrajectoryFromName(trajectoryNames[3]))

class EventPressKeyK(event.Event):
    def __init__(self):
        super().__init__(buttons[4][1])

    def func(self):
        player.getPlayer2().addTrajectoryType(trajectory.getTrajectoryFromName(trajectoryNames[4]))

class EventPressKeyZero(event.Event):
    def __init__(self):
        super().__init__("0")

    def func(self):
        airPlaneP2 = graphicsGame.player.getPlayer2().getAirPlane()
        if airPlaneP2.canShoot() and graphicsGame.gameState == 1:
            xBull = airPlaneP2.getX() + 81 * cos((airPlaneP2.getOrientation() * pi / 180) + pi / 2)
            yBull = airPlaneP2.getY() + 81 * sin((airPlaneP2.getOrientation() * pi / 180) + pi / 2)
            bullet.Bullet(xBull, yBull, airPlaneP2.getOrientation())
            airPlaneP2.shoot()
