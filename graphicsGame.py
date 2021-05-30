import libs.cng as cng
import debug
from time import sleep
import airPlaneType
import trajectory
import trajectoryType
import player
import gameEvent
import bullet
import soundManager
import libs.utils.colorbar as colorbar
import libs.utils.screenProperties as screenProperties
from math import pi, cos, sin, atan

"""
gameState:
    - 0: Selection des 3 trajectoires des deux joueurs (activations des boutons de choix de trajectoire AEZDQ et IPOMK)
    - 1: Affichage des 3 trajectoires des deux joueurs (désactivations des des bouton de choix de traj)
    - 2: Victoire par l'un des joueurs
"""
gameState = 0

refreshTime = 0.01

menuDimensions = (screenProperties.getScreenWidth(), screenProperties.getScreenHeight())
airPlaneScale = 1.5


player1 = None
player2 = None
airPlanePlayer1Name = ""
airPlanePlayer2Name = ""
airPlanePlayer1Picture = None
airPlanePlayer2Picture = None
imgDefaultFont = None
bulletPicture = None

def initWindows():
    """
    Initialize Windows
    Select trajectories
    Draw airplanes's trajectories
    """
    global player1, player2
    player1 = player.Player(airPlaneType.getAirPlanesTypes()[airPlanePlayer1Name], menuDimensions[0] * 0.2, menuDimensions[1] * 0.5, 270)
    player2 = player.Player(airPlaneType.getAirPlanesTypes()[airPlanePlayer2Name], menuDimensions[0] * 0.8, menuDimensions[1] * 0.5, 90)
    cng.init_window("Duel dans le ciel - Game", menuDimensions[0], menuDimensions[1], True)
    cng.setIconApplicationPhoto("textures/symbols/icon_menu.png")
    cng.registerQuitHandler(closeWindowEvent)
    loadPictures()
    soundManager.playSound("sounds/Dragonforce-FuryoftheStorm.wav")

    while gameState != 2:
        gameTrajSelect()
        gameTrajDraw()
    gameEnded()

def closeWindowEvent():
    """
    Call when windows is closed (manually or asked)
    """
    debug.l("Window", "Closed graphicsGame windows")

def loadPictures():
    """
    Load pictures
    """
    debug.l("Picture", "Loading pictures...")
    global imgDefaultFont, airPlanePlayer1Picture, airPlanePlayer2Picture, bulletPicture
    imgDefaultFont = cng.image("textures/gameplay/photo_aerienne.jpg", menuDimensions[0], menuDimensions[1])

    airPlanePlayer1Type = player1.getAirPlane().getAirPlaneType()
    airPlanePlayer1Picture = cng.image(airPlanePlayer1Type.getPath(), airPlanePlayer1Type.getXDimension() // airPlaneScale, airPlanePlayer1Type.getYDimension() // airPlaneScale)

    airPlanePlayer2Type = player2.getAirPlane().getAirPlaneType()
    airPlanePlayer2Picture = cng.image(airPlanePlayer2Type.getPath(), airPlanePlayer2Type.getXDimension() // airPlaneScale, airPlanePlayer2Type.getYDimension() // airPlaneScale)

    bulletPicture = cng.image(bullet.picturePath, bullet.xDimensionsTexture, bullet.yDimensionsTexture)
    
    debug.success("Picture", "Pictures loaded successfully")

def gameBasicDraw():
    """
    Minimum to draw on the screen
    """
    if cng.idle_dead():
        debug.l("Game", "Game closed")
        exit()
    cng.clear_screen()
    cng.image_draw(menuDimensions[0] // 2, menuDimensions[1] // 2, imgDefaultFont)

    # Draw hitbox
    if debug.getDebugMode() == 2:
        # draw Air planes hitbox
        for player in {player1, player2}:
            airPlaneTextureDim = (player.getAirPlane().getAirPlaneType().getXDimension(), player.getAirPlane().getAirPlaneType().getYDimension())
            cng.rectangle(player.getX() - 0.5 * airPlaneTextureDim[0], player.getY() - 0.5 * airPlaneTextureDim[1], player.getX() + 0.5 * airPlaneTextureDim[0], player.getY() + 0.5 * airPlaneTextureDim[1])

        # bullets hitbox
        for bull in bullet.bullets:
            cng.rectangle(bull.getX() - 0.5 * bullet.xDimensionsTexture, bull.getY() - 0.5 * bullet.yDimensionsTexture, bull.getX() + 0.5 * bullet.xDimensionsTexture, bull.getY() + 0.5 * bullet.yDimensionsTexture)


    imgP1 = cng.image_draw(player1.getX(), player1.getY(), airPlanePlayer1Picture)
    imgP2 = cng.image_draw(player2.getX(), player2.getY(), airPlanePlayer2Picture)
    cng.image_rotate(airPlanePlayer1Picture, imgP1, player1.getOrientation())
    cng.image_rotate(airPlanePlayer2Picture, imgP2, player2.getOrientation())

    for bull in bullet.bullets:
        imgBull = cng.image_draw(bull.getX(), bull.getY(), bulletPicture)
        #cng.image_rotate(bulletPicture, imgBull, bull.getOrientation())

    # Player 1 display infos
    cng.textFont(menuDimensions[0] * 0.1, menuDimensions[1] * 0.9, "Joueur 1", "retro gaming", 12)

    # Player 1 display health bar
    cng.current_color("black")
    cng.box(menuDimensions[0] * 0.1, menuDimensions[1] * 0.85, menuDimensions[0] * 0.2, menuDimensions[1] * 0.8)
    rgbHealth = colorbar.convertHealthToColor(player1.getAirPlane().getAirPlaneType().getMaxHealth(), player1.getAirPlane().getHealth())
    cng.current_color(rgbHealth[0], rgbHealth[1], rgbHealth[2])
    cng.box(menuDimensions[0] * 0.11, menuDimensions[1] * 0.84, menuDimensions[0] * 0.19, menuDimensions[1] * 0.81)
    cng.current_color("black")

    cng.textFont(menuDimensions[0] * 0.1, menuDimensions[1] * 0.75, "Balles restantes: " + str(player1.getAirPlane().getAmmo()), "retro gaming", 11)

    # Player 2 display infos
    cng.textFont(menuDimensions[0] * 0.85, menuDimensions[1] * 0.9, "Joueur 2", "retro gaming", 12)

    # Player 2 display health bar
    cng.box(menuDimensions[0] * 0.8, menuDimensions[1] * 0.85, menuDimensions[0] * 0.9, menuDimensions[1] * 0.8)
    rgbHealth = colorbar.convertHealthToColor(player2.getAirPlane().getAirPlaneType().getMaxHealth(), player2.getAirPlane().getHealth())
    cng.current_color(rgbHealth[0], rgbHealth[1], rgbHealth[2])
    cng.box(menuDimensions[0] * 0.81, menuDimensions[1] * 0.84, menuDimensions[0] * 0.89, menuDimensions[1] * 0.81)
    cng.current_color("black")

    cng.textFont(menuDimensions[0] * 0.8, menuDimensions[1] * 0.75, "Balles restantes: " + str(player2.getAirPlane().getAmmo()), "retro gaming", 11)


def gameTrajSelect():
    """
    Trajectory selection
    """
    global gameState
    while gameState == 0:

        if not (None in player1.getTrajectoryTypes()) and not(None in player2.getTrajectoryTypes()):
            gameState = 1
            break

        gameBasicDraw()
        cng.textFont(menuDimensions[0] * 0.25, menuDimensions[1] * 0.9, "Veuillez choisir 3 trajectoires", "retro gaming", 25)

        debug.errorIf("Texte screen printer", "Le nombre de boutons n'est pas identique au nombre de trajectoire", len(gameEvent.trajectoryList) != len(gameEvent.buttons))
        for i in range(min(len(gameEvent.trajectoryList), len(gameEvent.buttons))):
            cng.textFont(menuDimensions[0] * 0.40, menuDimensions[1] * 0.85 - (20 * i), gameEvent.buttons[i][0].upper() + '/' + gameEvent.buttons[i][1].upper() + " : " + gameEvent.trajectoryList[i], "retro gaming", 15)

        for i in range(3):
            cng.current_color("black")
            cng.disc(menuDimensions[0] * (i + 1) * 0.1, menuDimensions[1] * 0.1, 20)
            cng.disc(menuDimensions[0] * (1 - ((i + 1) * 0.1)), menuDimensions[1] * 0.1, 20)

            cng.current_color("red" if player1.getTrajectoryTypes()[i] == None else "green")

            cng.disc(menuDimensions[0] * (i + 1) * 0.1, menuDimensions[1] * 0.1, 18)

            cng.current_color("red" if player2.getTrajectoryTypes()[i] == None else "green")

            cng.disc(menuDimensions[0] * (1 - ((i + 1) * 0.1)), menuDimensions[1] * 0.1, 18)
            cng.current_color("black")

        cng.refresh()
        sleep(refreshTime)

def calculAngle(oldPoint, newPoint):
    """
    Compute orientation of airplane in degree
    """
    if newPoint[0] - oldPoint[0] != 0:
        a = (newPoint[1] - oldPoint[1]) / (newPoint[0] - oldPoint[0])
        b = newPoint[1] - a * newPoint[0]
        if a != 0:
            x_base = -b / a
            angle = atan(newPoint[1] / (newPoint[0] - x_base))
            if newPoint[0] > oldPoint[0]:
                angle -= pi / 2
            else:
                angle += pi / 2
            angle = (angle * 360) / (2 * pi) % 360
            return angle
    return 0

def gameTrajDraw():
    """
    Draw trajectories on the screen
    """
    global gameState
    for trajectoryCount in range(3):

        if player1.getAirPlane().isDead() or player2.getAirPlane().isDead():
            gameState = 2
            break

        gameBasicDraw()

        x_abscisseP1 = player1.getTrajectoryTypes()[trajectoryCount].getInterval()
        x_abscisseP2 = player2.getTrajectoryTypes()[trajectoryCount].getInterval()

        airPlaneXP1 = player1.getX()
        airPlaneYP1 = player1.getY()
        airPlaneXP2 = player2.getX()
        airPlaneYP2 = player2.getY()
        airPlaneAngleP1 = (player1.getOrientation() * pi) / 180
        airPlaneAngleP2 = (player2.getOrientation() * pi) / 180

        oldPointP1 = [player1.getX(), player1.getY()]
        oldPointP2 = [player2.getX(), player2.getY()]

        for i in range(trajectoryType.INTERVAL_COUNT):

            # Calculating new coordinates for airplaines
            f_x_P1 = player1.getTrajectoryTypes()[trajectoryCount].walkX(x_abscisseP1[i])
            f_y_P1 = player1.getTrajectoryTypes()[trajectoryCount].walkY(x_abscisseP1[i])
            f_x_P2 = player2.getTrajectoryTypes()[trajectoryCount].walkX(x_abscisseP2[i])
            f_y_P2 = player2.getTrajectoryTypes()[trajectoryCount].walkY(x_abscisseP2[i])

            rotated_f_x_P1 = f_x_P1 * cos(airPlaneAngleP1) - f_y_P1 * sin(airPlaneAngleP1)
            rotated_f_y_P1 = f_x_P1 * sin(airPlaneAngleP1) + f_y_P1 * cos(airPlaneAngleP1)
            rotated_f_x_P2 = f_x_P2 * cos(airPlaneAngleP2) - f_y_P2 * sin(airPlaneAngleP2)
            rotated_f_y_P2 = f_x_P2 * sin(airPlaneAngleP2) + f_y_P2 * cos(airPlaneAngleP2)

            player1.setX(rotated_f_x_P1 + airPlaneXP1)
            player1.setY(rotated_f_y_P1 + airPlaneYP1)
            player2.setX(rotated_f_x_P2 + airPlaneXP2)
            player2.setY(rotated_f_y_P2 + airPlaneYP2)

            newPointP1 = (player1.getX(), player1.getY())
            newPointP2 = (player2.getX(), player2.getY())

            player1.setOrientiation(calculAngle(oldPointP1, newPointP1))
            player2.setOrientiation(calculAngle(oldPointP2, newPointP2))
            oldPointP1 = [newPointP1[0], newPointP1[1]]
            oldPointP2 = [newPointP2[0], newPointP2[1]]

            # Calculating new bullet coordinates
            i = 0
            bulletAmount = len(bullet.bullets)
            while i < bulletAmount:
                bull = bullet.bullets[i]
                if bull.getX() < 0 or bull.getX() > menuDimensions[0] or bull.getY() < 0 or bull.getY() > menuDimensions[1]:
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
                bullCorners = {
                    (bull.getX() - 0.5 * bullet.xDimensionsTexture, bull.getY() - 0.5 * bullet.yDimensionsTexture),
                    (bull.getX() + 0.5 * bullet.xDimensionsTexture, bull.getY() - 0.5 * bullet.yDimensionsTexture),
                    (bull.getX() - 0.5 * bullet.xDimensionsTexture, bull.getY() + 0.5 * bullet.yDimensionsTexture),
                    (bull.getX() + 0.5 * bullet.xDimensionsTexture, bull.getY() + 0.5 * bullet.yDimensionsTexture)}

                for player in {player1, player2}:
                    airPlaneTextureDim = (player.getAirPlane().getAirPlaneType().getXDimension(), player.getAirPlane().getAirPlaneType().getYDimension())
                    for bCorner in bullCorners:
                        if (player.getX() - 0.5 * airPlaneTextureDim[0] < bCorner[0] < player.getX() + 0.5 * airPlaneTextureDim[0] and
                        player.getY() - 0.5 * airPlaneTextureDim[1] < bCorner[1] < player.getY() + 0.5 * airPlaneTextureDim[1]):
                            player.getAirPlane().addDamage(10)
                            if player.getAirPlane().isDead():
                                gameState = 2
                                return
                            bull.kill()
                            i -= 1
                            bulletAmount -= 1
                            break
                    if bull.isKilled():
                        break
                i += 1

            gameBasicDraw()
            cng.refresh()
            sleep(refreshTime)

        cng.refresh()
        sleep(refreshTime)
    player1.clearTrajectoryList()
    player2.clearTrajectoryList()
    player1.getAirPlane().refillAmmo()
    player2.getAirPlane().refillAmmo()
    # kill all bullets
    bullet.bullets = []

    if gameState != 2:
        gameState = 0


def gameEnded():
    """
    End game state
    """
    gameBasicDraw()
    print("game ended")

def addSelectionnedTrajPlayer1(trajName):
    """
    Add trajectory
    """
    player1.addTrajectoryType(trajectory.trajectoryTypes[trajName])

def addSelectionnedTrajPlayer2(trajName):
    """
    add trajectory
    """
    player2.addTrajectoryType(trajectory.trajectoryTypes[trajName])

def initPlayer1AirPlane(airPlaneName):
    global airPlanePlayer1Name
    airPlanePlayer1Name = airPlaneName

def initPlayer2AirPlane(airPlaneName):
    global airPlanePlayer2Name
    airPlanePlayer2Name = airPlaneName
