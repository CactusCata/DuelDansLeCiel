import winsound
from utils.stoppableThread import StoppableThread

def playSound(soundPath):
    """
    Play a sound in another thread
    """
    T = StoppableThread(target=winsound.PlaySound, args=(soundPath, winsound.SND_FILENAME|winsound.SND_LOOP|winsound.SND_ASYNC))
    T.start()
