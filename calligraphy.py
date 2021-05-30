import sys
import debug
if sys.version_info <= (3,9):
    debug.error("calligraphy", "Can't apply specific calligraphy before Python 3.9")
    debug.error("calligraphy", "Application closed.")
else:
    import pyglet

def loadCalligraphy(path, asName):
    pyglet.font.add_file(path)
    pyglet.font.load(asName)

def isWork():
    """
    Called at the beginning to stop the game if pyglet is not installed 
    """
    try:
        pyglet
        return True
    except NameError:
        return False
