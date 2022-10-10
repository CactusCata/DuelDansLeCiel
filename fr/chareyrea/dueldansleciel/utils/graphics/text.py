import libs.cng as cng
import utils.screenProperties as screenProperties
import utils.calligraphy as calligraphy

class Text:

    def __init__(self, x, y, text, textSize, fontName=None):
        """
        if x|y E ]0,1[, he will be considered as a
        proportion of screen's dimensions
        """
        self.x = x * screenProperties.getWidth() if (x > 0 and x < 1) else x
        self.y = y * screenProperties.getHeight() if (y > 0 and y < 1) else y
        self.text = text
        self.textSize = textSize
        self.fontName = fontName if fontName != None else calligraphy.DEFAULT_FONT_NAME

    def draw(self):
        cng.textFont(self.x, self.y, self.text, self.fontSize, self.fontName)

def generateTextFontProportion(text, x, y, placementProportion, screenDimensions = (0, 0), fontName = None):
    if screenDimensions == (0, 0):
        screenDimensions = (screenProperties.getWidth(), screenProperties.getHeight())
    screenWidth = screenDimensions[0]
    screenHeight = screenDimensions[1]
    betterFontSizeWidth = calligraphy.getBetterFontSize(text, screenWidth, pxProportion)
    textPxWidth = calligraphy.getTextSize(text, betterFontSizeWidth)[0]
    return Text(placementProportion[0] * screenWidth - textPxWidth // 1.5, screenHeight * placementProportion[1], text, betterFontSizeWidth, fontName)
