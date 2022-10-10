ticks = 0
fps = 0

def getTicks():
    return ticks

def getFps():
    return fps

def increaseTicks():
    global ticks
    ticks += 1

def setFps(frames):
    global fps
    fps = frames
