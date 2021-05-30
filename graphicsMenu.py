import libs.cng as cng
import debug
import airPlaneType
from time import sleep
import graphicsGame
import soundManager
import libs.utils.screenProperties as screenProperties

refreshTime = 0.01

menuCursor = 0 # select air plane menu (0 to 3)
menuEnter = False

menuDimensions = (screenProperties.getScreenWidth(), screenProperties.getScreenHeight())
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
    cng.init_window("Duel dans le ciel - Choix des avions", menuDimensions[0], menuDimensions[1], True)
    cng.setIconApplicationPhoto("textures/symbols/icon_menu.png")
    cng.registerQuitHandler(closeWindowEvent)
    loadPictures()
    soundManager.playSound("sounds/symph.wav")
    graphicsGame.initPlayer1AirPlane(playerAirSelection(1))
    graphicsGame.initPlayer2AirPlane(playerAirSelection(2))
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

    imgDefaultFont = cng.image("textures/menu/default_font.jpg", menuDimensions[0], menuDimensions[1])
    for airPlane in airPlaneType.getAirPlanesTypes().values():
        airPlanePictures += [cng.image(airPlane.getPath(), airPlane.getXDimension() // airPlaneScale, airPlane.getYDimension() // airPlaneScale)]
        airPlanesNames += [airPlane.getName()]
    arrowUpPicture = cng.image("textures/symbols/arrow_up.png")
    arrowDownPicture = cng.image("textures/symbols/arrow_down.png")
    
    debug.success("Picture", "Pictures loaded successfully")

def playerAirSelection(playerNumber):
    """
    Draw on the screen airplanes' pictures (the system is adapted for more or less airPlane)
    Continue while airPlane was not picked
    """
    minDistBetweenAirPlane = 150
    airPlaneCoordinates = [-1] * len(airPlanePictures)

    # Calculating air planes coordinates
    if len(airPlanePictures) % 2 == 1:
        for i in range((len(airPlanePictures) // 2) + 1):
            arrayIndex = (len(airPlanePictures) - ((len(airPlanePictures) // 2) + 1))
            airPlaneCoordinates[arrayIndex - i] = (menuDimensions[0] // 2 - (minDistBetweenAirPlane * i), menuDimensions[1] // 2)
            airPlaneCoordinates[arrayIndex + i] = (menuDimensions[0] // 2 + (minDistBetweenAirPlane * i), menuDimensions[1] // 2)
    else:
        for i in range(1, (len(airPlanePictures) // 2) + 1):
            arrayIndex = (len(airPlanePictures) - (len(airPlanePictures) // 2))
            airPlaneCoordinates[arrayIndex - i] = (menuDimensions[0] // 2 - int(minDistBetweenAirPlane * (i - 0.5)), menuDimensions[1] // 2)
            airPlaneCoordinates[arrayIndex + i - 1] = (menuDimensions[0] // 2 + int(minDistBetweenAirPlane * (i - 0.5)), menuDimensions[1] // 2)

    ticks = 0
    while not menuEnter:
        if cng.idle_dead():
            debug.l("Game", "Game closed")
            exit()
        cng.clear_screen()
        cng.image_draw(menuDimensions[0] // 2, menuDimensions[1] // 2, imgDefaultFont)
        cng.textFont(menuDimensions[0] * 0.3, menuDimensions[1] * 0.85, "Duel dans le ciel", "retro gaming", 35)
        cng.textFont(menuDimensions[0] * 0.31, menuDimensions[1] * 0.75, "Player " + str(playerNumber) + ": choisissez un avion :", "retro gaming", 18)

        for i in range(len(airPlanePictures)):
            cng.image_draw(airPlaneCoordinates[i][0], airPlaneCoordinates[i][1], airPlanePictures[i])

        if ticks % 40 >= 40 // 2:
            cng.image_draw(airPlaneCoordinates[0][0] + (minDistBetweenAirPlane * menuCursor), (menuDimensions[1] // 2)* 1.2, arrowDownPicture)
            cng.image_draw(airPlaneCoordinates[0][0] + (minDistBetweenAirPlane * menuCursor), (menuDimensions[1] // 2)* 0.8, arrowUpPicture)
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
