import chapter.renderer as renderer
from utils.imageLoader import ImageLoader
import entity.player as player
import entity.bullet as bullet
import libs.cng as cng
import utils.debug as debug
import event.eventManager as eventManager
import chapter.game.gameEvent as gameEvent
import trajectories.trajectoryType as trajectoryType
from entity.entity import Entity
import utils.mathsUtils as mathsUtils
import utils.soundManager as soundManager
import utils.colorbar as colorbar
from chapter.win.winRenderer import WinRenderer
from time import time
from math import pi, cos, sin


class GameRenderer(renderer.Renderer):

    def __init__(self):
        super().__init__("Game Renderer")
        soundManager.playSound("../../../sounds/bethoveen_sonata.wav")
        self.ended = False
        self.gameState = 0
        self.trajPoint = 0
        self.backgroundImage = None
        self.airplanesPointsP1 = []
        self.airplanesPointsP2 = []

    def calculateAllPoints(self):

        self.trajPoint = 0

        player1 = player.getPlayer1()
        player2 = player.getPlayer2()

        airplaneP1 = player1.getAirplane()
        airplaneP2 = player2.getAirplane()
        #                      1st point P1         1st point P2           2nd point P1        2nd point P2
        # airplanePoints = [((x, y, orientation), (x, y, orientation)), ((x, y, orientation), (x, y, orientation))]
        self.airplanesPointsP1 = [(airplaneP1.getX(), airplaneP1.getY(), airplaneP1.getOrientation())]
        self.airplanesPointsP2 = [(airplaneP2.getX(), airplaneP2.getY(), airplaneP2.getOrientation())]
        pointCount = 1

        for plyr in {player1, player2}:
            airplane = plyr.getAirplane()

            airplanesPoints = self.airplanesPointsP1 if plyr == player1 else self.airplanesPointsP2
            oldPoint = [airplanesPoints[-1][0], airplanesPoints[-1][1]]
            for trajectoryCount in range(3):

                trajType =  plyr.getTrajectoryTypes()[trajectoryCount]

                t_abscisse = trajType.getInterval()

                airplaneX = airplanesPoints[-1][0]
                airplaneY = airplanesPoints[-1][1]
                airplaneAngle = (airplanesPoints[-1][2] * pi) / 180

                for i in range(trajectoryType.INTERVAL_COUNT):
                    # Calculating new coordinates for airplaines: x(t) and y(t)
                    f_x = trajType.walkX(t_abscisse[i])
                    f_y = trajType.walkY(t_abscisse[i])

                    rotated_f_x = f_x * cos(airplaneAngle) - f_y * sin(airplaneAngle)
                    rotated_f_y = f_x * sin(airplaneAngle) + f_y * cos(airplaneAngle)

                    x = rotated_f_x + airplaneX
                    y = rotated_f_y + airplaneY

                    angle = mathsUtils.calculAngle(oldPoint, [x, y], airplanesPoints[-1][2])
                    airplanesPoints.append((x, y, angle))
                    oldPoint = [x, y]

                    pointCount += 1

    def calcul(self, updateCount):

        player1 = player.getPlayer1()
        player2 = player.getPlayer2()

        airplaneP1 = player1.getAirplane()
        airplaneP2 = player2.getAirplane()

        if self.gameState == 0:
            return


        # draw trajectories
        elif self.gameState == 1:

            if airplaneP1.isDead() or airplaneP2.isDead():
                self.gameState = 2
                return

            # Update airplanes positions
            neededPoint = self.trajPoint + updateCount if self.trajPoint + updateCount < len(self.airplanesPointsP1) else len(self.airplanesPointsP1) - 1
            pointP1 = self.airplanesPointsP1[neededPoint]
            airplaneP1.setX(pointP1[0])
            airplaneP1.setY(pointP1[1])
            airplaneP1.setOrientation(pointP1[2])

            pointP2 = self.airplanesPointsP2[neededPoint]
            airplaneP2.setX(pointP2[0])
            airplaneP2.setY(pointP2[1])
            airplaneP2.setOrientation(pointP2[2])

            self.trajPoint = neededPoint

            if neededPoint == len(self.airplanesPointsP1) - 1:
                player1.clearTrajectoryList()
                player2.clearTrajectoryList()
                airplaneP1.refillAmmo()
                airplaneP2.refillAmmo()
                # kill all bullets
                bullet.bullets = []
                self.gameState = 0
                return

            # Calculating futur new bullets coordinates
            i = 0
            bulletAmount = len(bullet.bullets)
            while i < bulletAmount:
                bull = bullet.bullets[i]
                if bull.getX() < 0 or bull.getX() > renderer.screenWidth or bull.getY() < 0 or bull.getY() > renderer.screenHeight:
                    bull.kill()
                    i -= 1
                    bulletAmount -= 1
                bull.setX(bull.getX() + 5 * cos((bull.getOrientation() * pi / 180) + pi / 2))
                bull.setY(bull.getY() + 5 * sin((bull.getOrientation() * pi / 180) + pi / 2))
                i += 1

            # Calculating collisions between bullets and airplanes
            i = 0
            bulletAmount = len(bullet.bullets)
            while i < bulletAmount:
                bull = bullet.bullets[i]
                bullHitBox = bull.getHitBox()
                for plyr in {player1, player2}:
                    airplane = plyr.getAirplane()
                    airplaneHitBox = airplane.getHitBox()
                    for bCorner in bullHitBox:
                        if (airplaneHitBox[0][0] < bCorner[0] < airplaneHitBox[1][0] and
                            airplaneHitBox[0][1] < bCorner[1] < airplaneHitBox[2][1]):
                            airplane.addDamage(10)
                            if airplane.isDead():
                                self.gameState = 2
                                self.ended = True
                                return
                            bull.kill()
                            i -= 1
                            bulletAmount -= 1
                            break
                    if bull.isKilled():
                        break
                i += 1


        elif self.gameState == 2:
            return



    def render(self, drawCount):

        player1 = player.getPlayer1()
        player2 = player.getPlayer2()
        airplaneP1 = player1.getAirplane()
        airplaneP2 = player2.getAirplane()

        self.basicRender()

        # Trajectories choice
        if self.gameState == 0:

            if not (None in player1.getTrajectoryTypes()) and not(None in player2.getTrajectoryTypes()):
                self.gameState = 1
                self.calculateAllPoints()
                return

            cng.textFont(renderer.screenWidth * 0.25, renderer.screenHeight * 0.9, "Veuillez choisir 3 trajectoires", 25)

            debug.errorIf("Texte screen printer", "Le nombre de boutons n'est pas identique au nombre de trajectoire", len(gameEvent.trajectoriesName) != len(gameEvent.trajectoriesSelectionKeyName))
            for i in range(min(len(gameEvent.trajectoriesName), len(gameEvent.trajectoriesSelectionKeyName))):
                cng.textFont(renderer.screenWidth * 0.40, renderer.screenHeight * 0.85 - (20 * i), gameEvent.trajectoriesSelectionKeyName[i][0].upper() + '/' + gameEvent.trajectoriesSelectionKeyName[i][1].upper() + " : " + gameEvent.trajectoriesName[i], 15)

            for i in range(3):
                cng.current_color("black")
                cng.disc(renderer.screenWidth * (i + 1) * 0.1, renderer.screenHeight * 0.1, 20)
                cng.disc(renderer.screenWidth * (1 - ((i + 1) * 0.1)), renderer.screenHeight * 0.1, 20)

                cng.current_color("red" if player1.getTrajectoryTypes()[i] == None else "green")
                cng.disc(renderer.screenWidth * (i + 1) * 0.1, renderer.screenHeight * 0.1, 18)

                cng.current_color("red" if player2.getTrajectoryTypes()[i] == None else "green")
                cng.disc(renderer.screenWidth * (1 - ((i + 1) * 0.1)), renderer.screenHeight * 0.1, 18)

        elif self.gameState == 1:
            return

        elif self.gameState == 2:
            return




    def basicRender(self):
        self.backgroundImage.draw()

        player1 = player.getPlayer1()
        player2 = player.getPlayer2()

        airplaneP1 = player1.getAirplane()
        airplaneP2 = player2.getAirplane()

        cng.current_color("black")

        # Draw hitbox
        if debug.getDebugMode() == 2:
            # draw Air planes hitbox
            for airplane in {airplaneP1, airplaneP2}:
                hitbox = airplane.getHitBox()
                cng.rectangle(hitbox[0][0], hitbox[0][1], hitbox[2][0], hitbox[2][1])

            # bullets hitbox
            for bull in bullet.bullets:
                hitbox = bull.getHitBox()
                cng.rectangle(hitbox[0][0], hitbox[0][1], hitbox[2][0], hitbox[2][1])

        airplaneP1Image = airplaneP1.draw()
        airplaneP1.drawOrientation(airplaneP1Image)

        airplaneP2Image = airplaneP2.draw()
        airplaneP2.drawOrientation(airplaneP2Image)

        global cpims
        cpims = []
        for bull in bullet.bullets:
            imgBull = bull.draw()
            cpims.append(bull.drawOrientation(imgBull, bull.getOrientation() + 90)[1])

        #weather.render()
        #weather.tickUpdate()

        cng.textFont(renderer.screenWidth * 0.1, renderer.screenHeight * 0.9, "Joueur 1", 12)
        cng.textFont(renderer.screenWidth * 0.85, renderer.screenHeight * 0.9, "Joueur 2", 12)

        # Player 1 display health bar
        cng.box(renderer.screenWidth * 0.1, renderer.screenHeight * 0.85, renderer.screenWidth * 0.2, renderer.screenHeight * 0.8)
        cng.box(renderer.screenWidth * 0.8, renderer.screenHeight * 0.85, renderer.screenWidth * 0.9, renderer.screenHeight * 0.8)

        rgbHealth = colorbar.convertHealthToColor(airplaneP1.getAirplaneType().getMaxHealth(), airplaneP1.getHealth())
        cng.current_color(rgbHealth[0], rgbHealth[1], rgbHealth[2])
        cng.box(renderer.screenWidth * 0.81, renderer.screenHeight * 0.84, renderer.screenWidth * 0.89, renderer.screenHeight * 0.81)
        rgbHealth = colorbar.convertHealthToColor(airplaneP2.getAirplaneType().getMaxHealth(), airplaneP2.getHealth())
        cng.current_color(rgbHealth[0], rgbHealth[1], rgbHealth[2])
        cng.box(renderer.screenWidth * 0.11, renderer.screenHeight * 0.84, renderer.screenWidth * 0.19, renderer.screenHeight * 0.81)

        cng.current_color("black")
        cng.textFont(renderer.screenWidth * 0.1, renderer.screenHeight * 0.75, "Balles restantes: " + str(airplaneP1.getAmmo()), 11)
        cng.textFont(renderer.screenWidth * 0.8, renderer.screenHeight * 0.75, "Balles restantes: " + str(airplaneP2.getAmmo()), 11)

    def registerEvents(self):
        eventManager.registerKeyPressEvent(gameEvent.EventPressKeyA())
        eventManager.registerKeyPressEvent(gameEvent.EventPressKeyE())
        eventManager.registerKeyPressEvent(gameEvent.EventPressKeyZ())
        eventManager.registerKeyPressEvent(gameEvent.EventPressKeyD())
        eventManager.registerKeyPressEvent(gameEvent.EventPressKeyQ())
        eventManager.registerKeyPressEvent(gameEvent.EventPressKeyI())
        eventManager.registerKeyPressEvent(gameEvent.EventPressKeyP())
        eventManager.registerKeyPressEvent(gameEvent.EventPressKeyO())
        eventManager.registerKeyPressEvent(gameEvent.EventPressKeyM())
        eventManager.registerKeyPressEvent(gameEvent.EventPressKeyK())
        eventManager.registerKeyPressEvent(gameEvent.EventPressKeySpace())
        eventManager.registerKeyPressEvent(gameEvent.EventPressKeyZero())

    def loadEntities(self):
        debug.l("Picture", "Loading pictures...")

        self.backgroundImage = Entity(ImageLoader("../../../textures/gameplay/photo_aerienne.jpg", renderer.screenWidth, renderer.screenHeight), renderer.screenWidth // 2, renderer.screenHeight // 2)
        self.bulletImage = ImageLoader(bullet.picturePath, bullet.xDimensionsTexture, bullet.yDimensionsTexture)

        debug.success("Picture", "Pictures loaded successfully")


    def next(self):
        return WinRenderer

    def isEnded(self):
        return self.ended
