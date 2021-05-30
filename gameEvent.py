import event
import graphicsGame
import bullet
from math import cos, sin, pi

trajectoryList = ["virage a droite", "virage a gauche", "ligne droite", "glissade a droite", "glissade a gauche"]
buttons = [('a', 'i'), ('e', 'p'), ('z', 'o'), ('d', 'm'), ('q', 'k')]

class EventPressKeyA(event.Event):
    def __init__(self):
        event.Event.__init__(self, buttons[0][0])

    def func(self):
        graphicsGame.addSelectionnedTrajPlayer1(trajectoryList[0])

class EventPressKeyE(event.Event):
    def __init__(self):
        event.Event.__init__(self, buttons[1][0])

    def func(self):
        graphicsGame.addSelectionnedTrajPlayer1(trajectoryList[1])

class EventPressKeyZ(event.Event):
    def __init__(self):
        event.Event.__init__(self, buttons[2][0])

    def func(self):
        graphicsGame.addSelectionnedTrajPlayer1(trajectoryList[2])

class EventPressKeyD(event.Event):
    def __init__(self):
        event.Event.__init__(self, buttons[3][0])

    def func(self):
        graphicsGame.addSelectionnedTrajPlayer1(trajectoryList[3])

class EventPressKeyQ(event.Event):
    def __init__(self):
        event.Event.__init__(self, buttons[4][0])

    def func(self):
        graphicsGame.addSelectionnedTrajPlayer1(trajectoryList[4])

class EventPressKeySpace(event.Event):
    def __init__(self):
        event.Event.__init__(self, "space")

    def func(self):
        if graphicsGame.player1.getAirPlane().canShoot() and graphicsGame.gameState == 1:
            xBull = graphicsGame.player1.getX() + 90 * cos((graphicsGame.player1.getOrientation() * pi / 180) + pi / 2)
            yBull = graphicsGame.player1.getY() + 90 * sin((graphicsGame.player1.getOrientation() * pi / 180) + pi / 2)
            bullet.Bullet(xBull, yBull, graphicsGame.player1.getOrientation())
            graphicsGame.player1.getAirPlane().shoot()

 # Player 2 selection

class EventPressKeyI(event.Event):
    def __init__(self):
        event.Event.__init__(self, buttons[0][1])

    def func(self):
        graphicsGame.addSelectionnedTrajPlayer2(trajectoryList[0])

class EventPressKeyP(event.Event):
    def __init__(self):
        event.Event.__init__(self, buttons[1][1])

    def func(self):
        graphicsGame.addSelectionnedTrajPlayer2(trajectoryList[1])

class EventPressKeyO(event.Event):
    def __init__(self):
        event.Event.__init__(self, buttons[2][1])

    def func(self):
        graphicsGame.addSelectionnedTrajPlayer2(trajectoryList[2])

class EventPressKeyM(event.Event):
    def __init__(self):
        event.Event.__init__(self, buttons[3][1])

    def func(self):
        graphicsGame.addSelectionnedTrajPlayer2(trajectoryList[3])

class EventPressKeyK(event.Event):
    def __init__(self):
        event.Event.__init__(self, buttons[4][1])

    def func(self):
        graphicsGame.addSelectionnedTrajPlayer2(trajectoryList[4])

class EventPressKeyZero(event.Event):
    def __init__(self):
        event.Event.__init__(self, "0")

    def func(self):
        if graphicsGame.player2.getAirPlane().canShoot() and graphicsGame.gameState == 1:
            xBull = graphicsGame.player2.getX() + 50 * cos((graphicsGame.player2.getOrientation() * pi / 180) + pi / 2)
            yBull = graphicsGame.player2.getY() + 50 * sin((graphicsGame.player2.getOrientation() * pi / 180) + pi / 2)
            bullet.Bullet(xBull, yBull, graphicsGame.player2.getOrientation())
            graphicsGame.player2.getAirPlane().shoot()
