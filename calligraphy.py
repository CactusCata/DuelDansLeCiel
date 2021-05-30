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
    try:
        pyglet
        return True
    except NameError:
        return False
