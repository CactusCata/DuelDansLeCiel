import entity.airplane.airplaneType as airplaneType
import entity.player as player
from entity.entity import Entity
from chapter.renderer import Renderer
import chapter.menu.menuEvent as menuEvent
from chapter.game.gameRenderer import GameRenderer
import event.eventManager as eventManager
import utils.soundManager as soundManager
import utils.screenProperties as screenProperties
import utils.timeGame as timeGame
import utils.debug as debug
from utils.imageLoader import ImageLoader
import libs.cng as cng

class MenuRenderer(Renderer):

    def __init__(self):
        super().__init__("Menu Renderer")
        soundManager.playSound("../../../sounds/symph.wav")
        self.playerSelection = 1
        self.menuCursor = 0
        self.returnkey = False

    def calcul(self, updateCount):
        if self.returnkey:
            airplaneTp = airplaneType.getAirplanesTypes()[self.menuCursor]
            airplaneImage = ImageLoader(airplaneTp.getPath(), airplaneTp.getXDimension() * 0.7, airplaneTp.getYDimension() * 0.7)
            if self.playerSelection == 1:
                player.getPlayer1().associateAirplane(airplaneImage, screenProperties.getWidth() * 0.2, screenProperties.getHeight() * 0.5, 270, airplaneTp)
            elif self.playerSelection == 2:
                player.getPlayer2().associateAirplane(airplaneImage, screenProperties.getWidth() * 0.8, screenProperties.getHeight() * 0.5, 90, airplaneTp)
            self.returnkey = False
            if self.playerSelection < 2:
                self.playerSelection += 1


        if timeGame.getTicks() % 20 >= 20 // 2:
            airplaneTargetX = self.airplaneImages[self.menuCursor].getX()
            self.arrowUpImage.setX(airplaneTargetX)
            self.arrowUpImage.setY(screenProperties.getHeight() * 0.4)
            self.arrowDownImage.setX(airplaneTargetX)
            self.arrowDownImage.setY(screenProperties.getHeight() * 0.6)

    def render(self, updateCount):
        t = self.backgroundImage.draw()
        cng.textFontProportion("Duel dans le ciel", 0.5, 0.1, (0.5, 0.8))
        cng.textFontProportion("Player " + str(self.playerSelection) + ": choisissez un avion :", 0.2, 0.05, (0.5, 0.65))

        for airplane in self.airplaneImages:
            airplane.draw()

        if timeGame.getTicks() % 20 >= 20 // 2:
            self.arrowUpImage.draw()
            self.arrowDownImage.draw()

    def loadEntities(self):
        debug.l("Picture", "Loading pictures...")
        self.backgroundImage = Entity(ImageLoader("../../../textures/menu/default_font.jpg", screenProperties.getWidth(), screenProperties.getHeight()), screenProperties.getWidth() // 2, screenProperties.getHeight() // 2)
        self.arrowUpImage = Entity(ImageLoader("../../../textures/symbols/arrow_up.png"))
        self.arrowDownImage = Entity(ImageLoader("../../../textures/symbols/arrow_down.png"))

        airplanesDistancepx = 150
        startPixelDrawning = screenProperties.getWidth() - len(airplaneType.getAirplanesTypes()) * airplanesDistancepx
        airplaneScale = 0.7
        airplaneCount = 0
        self.airplaneImages = []
        for airplane in airplaneType.getAirplanesTypes():
            self.airplaneImages.append(Entity(ImageLoader(airplane.getPath(), airplane.getXDimension() // airplaneScale, airplane.getYDimension() // airplaneScale), startPixelDrawning / 2 + (airplaneCount + 0.5) * airplanesDistancepx, screenProperties.getHeight() // 2))
            airplaneCount += 1

        debug.success("Picture", "Pictures loaded successfully")

    def registerEvents(self):
        eventManager.registerKeyPressEvent(menuEvent.EventPressKeyRight())
        eventManager.registerKeyPressEvent(menuEvent.EventPressKeyLeft())
        eventManager.registerKeyPressEvent(menuEvent.EventPressKeyReturn())

    def isEnded(self):
        return player.getPlayer2().getAirplane() != None

    def next(self):
        return GameRenderer

    def setMenuCursor(self, index):
        self.menuCursor = index

    def getMenuCursor(self):
        return self.menuCursor

    def menuEnter(self):
        self.returnkey = True
