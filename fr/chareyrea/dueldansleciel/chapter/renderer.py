import utils.debug as debug
import utils.screenProperties as screenProperties

renderer = None
screenWidth = screenProperties.getWidth()
screenHeight = screenProperties.getHeight()

class Renderer:

    def __init__(self, name):
        global renderer
        renderer = self
        self.name = name

    def getName(self):
        return self.name

    def calcul(self, updateCount):
        debug.warn("render", "Renderer wasn't initialized")

    def render(self, updateCount):
        debug.warn("render", "Renderer wasn't initialized")

    def registerEvents(self):
        debug.warn("render", "Renderer wasn't initialized")

    def loadEntities(self):
        return None

    def next(self):
        """
        return next renderer
        """
        return None

    def isEnded(self):
        """
        Allow app to end actual renderer
        """
        return True

    def hasNext(self):
        return self.next() != None

def getRenderer():
    return renderer
