import libs.cng as cng
import debug
import airPlaneType
import player
from time import sleep
import graphicsGame
import soundManager
import calligraphy
import libs.utils.screenProperties as screenProperties

refreshTime = 0.01

menuCursor = 0 # select air plane menu (0 to 3)
menuEnter = False

screenDimensions = (screenProperties.getScreenWidth(), screenProperties.getScreenHeight())
airPlaneScale = 0.7

imgDefaultFont = None
airPlanePictures = []
airPlanesNames = []
arrowUpPicture = None
arrowDownPicture = None

def initWindows():
    """
    - Windows setup
    - Picture loading
    - Sound starting
    - AirPlane choice (P1/P2)
    """
    cng.init_window("Duel dans le ciel - Choix des avions", screenDimensions[0], screenDimensions[1], True)
    cng.setIconApplicationPhoto("textures/symbols/icon_menu.png")
    cng.registerQuitHandler(closeWindowEvent)
    loadPictures()
    soundManager.playSound("sounds/symph.wav")

    airplaneTypeP1 = airPlaneType.getAirPlaneTypeFromName(playerAirplaneSelection(1))
    airplaneTypeP2 = airPlaneType.getAirPlaneTypeFromName(playerAirplaneSelection(2))

    player.getPlayer1().associateAirPlane(screenDimensions[0] * 0.2, screenDimensions[1] * 0.5, 270, airplaneTypeP1)
    player.getPlayer2().associateAirPlane(screenDimensions[0] * 0.8, screenDimensions[1] * 0.5, 90, airplaneTypeP2)

    cng.__quitter()

def closeWindowEvent():
    """
    Call when windows is closed (manually or asked)
    """
    debug.l("Window", "Closed graphicsMenu windows")

def loadPictures():
    """
    Pictures loading
    """
    global imgDefaultFont, airPlanePictures, airPlanesNames, arrowUpPicture, arrowDownPicture
    debug.l("Picture", "Loading pictures...")

    imgDefaultFont = cng.image("textures/menu/default_font.jpg", screenDimensions[0], screenDimensions[1])
    for airPlane in airPlaneType.getAirPlanesTypes().values():
        airPlanePictures += [cng.image(airPlane.getPath(), airPlane.getXDimension() // airPlaneScale, airPlane.getYDimension() // airPlaneScale)]
        airPlanesNames += [airPlane.getName()]
    arrowUpPicture = cng.image("textures/symbols/arrow_up.png")
    arrowDownPicture = cng.image("textures/symbols/arrow_down.png")

    debug.success("Picture", "Pictures loaded successfully")

def playerAirplaneSelection(playerNumber):
    """
    Draw on the screen airplanes' pictures (the system is adapted for more or less airPlane)
    Continue while airPlane was not picked
    """
    # Calculating air planes coordinates
    airPlaneCoordinates = []
    minDistBetweenAirPlane = 150
    airplaneAmount = len(airPlanePictures)
    R = screenDimensions[0] - airplaneAmount * minDistBetweenAirPlane
    for i in range(airplaneAmount):
        airPlaneCoordinates += [(R / 2 + (i + 0.5) * minDistBetweenAirPlane, screenDimensions[1] // 2)]

    ticks = 0
    while not menuEnter:
        if cng.idle_dead():
            debug.l("Game", "Game closed")
            exit()

        cng.clear_screen()

        cng.image_draw(screenDimensions[0] // 2, screenDimensions[1] // 2, imgDefaultFont)
        cng.textFontProportion("Duel dans le ciel", 0.5, 0.1, (0.5, 0.8))
        cng.textFontProportion("Player " + str(playerNumber) + ": choisissez un avion :", 0.2, 0.05, (0.5, 0.65))

        for i in range(airplaneAmount):
            cng.image_draw(airPlaneCoordinates[i][0], airPlaneCoordinates[i][1], airPlanePictures[i])

        if ticks % 40 >= 40 // 2:
            cng.image_draw(airPlaneCoordinates[menuCursor][0], (screenDimensions[1] // 2) * 1.2, arrowDownPicture)
            cng.image_draw(airPlaneCoordinates[menuCursor][0], (screenDimensions[1] // 2) * 0.8, arrowUpPicture)
        # if ticks % 200 == 199: # condition pour effectuer un changement tous les n (n = 200 ici) ticks
        cng.refresh()
        sleep(refreshTime)
        ticks += 1
    cng.clear_screen()
    setMenuEnter(False)
    airPlaneSelected = airPlanesNames[menuCursor]
    setMenuCursor(0)
    return airPlaneSelected

def setMenuCursor(menuCursorValue):
    """
    Link the event class with this one
    to draw arrow selection on the correct airPlane
    """
    global menuCursor
    menuCursor = menuCursorValue

def setMenuEnter(menuEnterValue):
    """
    Link the event class with this one
    to select an airplane
    """
    global menuEnter
    menuEnter = menuEnterValue
