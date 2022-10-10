import chapter.renderer as renderer
import utils.soundManager as soundManager
import entity.player as player
from entity.entity import Entity
from utils.imageLoader import ImageLoader
import utils.debug as debug
import libs.cng as cng

class WinRenderer(renderer.Renderer):

    def __init__(self):
        super().__init__("Win Renderer")
        soundManager.playSound("../../../sounds/win.wav")
        if player.getPlayer1().getAirplane().isDead():
            self.playerWon = player.getPlayer2()
            self.playerNumber = 2
        else:
            self.playerWon = player.getPlayer1()
            self.playerNumber = 1
        airplanePlayerWon = self.playerWon.getAirplane()
        airplanePlayerWon.setX(renderer.screenWidth * 0.5)
        airplanePlayerWon.setY(renderer.screenHeight * 0.5)
        airplanePlayerWon.setOrientation(0)

    def loadEntities(self):
        debug.l("Picture", "Loading pictures...")

        self.backgroundImage = Entity(ImageLoader("../../../textures/gameplay/win_background.png", renderer.screenWidth, renderer.screenHeight), renderer.screenWidth // 2, renderer.screenHeight // 2)

        debug.success("Picture", "Pictures loaded successfully")

    def registerEvents(self):
        return None

    def render(self, drawCount):

        self.backgroundImage.draw()

        cng.textFontProportion("Félicitation au joueur " + str(self.playerNumber), 0.5, 0.1, (0.5, 0.8))
        self.playerWon.getAirplane().draw()

    def calcul(self, updateCount):
        return None

    def next(self):
        return None

    def isEnded(self):
        return False
