import sys
import utils.debug
if sys.version_info <= (3,9):
    debug.error("calligraphy", "Can't apply specific calligraphy before Python 3.9")
    debug.error("calligraphy", "Application closed.")
else:
    import pyglet
from PIL import ImageFont

DEFAULT_FONT_NAME = None
DEFAULT_FONT_FILE = None

def loadCalligraphy(path, asName, defaultFont):
    pyglet.font.add_file(path)
    pyglet.font.load(asName)
    if defaultFont:
        global DEFAULT_FONT, DEFAULT_FONT_FILE
        DEFAULT_FONT = asName
        DEFAULT_FONT_FILE = path

def isWork():
    """
    Called at the beginning to stop the game if pyglet is not installed
    """
    try:
        pyglet
        return True
    except NameError:
        return False

def getTextSize(text, fontSize, fontPath = None):
    if fontPath == None:
        fontPath = DEFAULT_FONT_FILE
    font = ImageFont.truetype(fontPath, fontSize, encoding="unic")
    size = font.getsize(text)
    return size

def getBetterFontSize(text, screenWidth, proportionWidth):
    """
    text: text which will be written
    screenWidth: x lenght screen
    proportion: text need to fit the width screen proportion needed (between 0 and 1)
    """
    minmax = [1, 100]
    mid = -1
    pixelAmountReached = screenWidth * proportionWidth
    while minmax[0] <= minmax[1]:
        mid = abs(minmax[0] + minmax[1]) // 2
        pixelText = getTextSize(text, mid)[0]
        if pixelText == pixelAmountReached:
            return mid
        elif pixelText < pixelAmountReached:
            minmax[0] = mid + 1
        else:
            minmax[1] = mid - 1
    return mid
