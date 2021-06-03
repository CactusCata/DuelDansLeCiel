import calligraphy
import debug
import eventManager
import graphicsMenu
import menuEvent
import graphicsGame
import gameEvent
import trajectoryType
import player

if __name__ == "__main__":
    debug.setDebugMode(1)
    if not calligraphy.isWork():
        debug.error("calligraphy", "Calligraphy not working.")
        debug.error("calligraphy", "Application stopped")
        exit()

    calligraphy.loadCalligraphy('calligraphy/retro_gaming.ttf', 'retro gaming', True)
    trajectoryType.initTrajectories()

    player.Player(1)
    player.Player(2)

    eventManager.registerSeveralsKeyPressEvents(menuEvent.EventPressKeyRight(), menuEvent.EventPressKeyLeft(), menuEvent.EventPressKeyReturn())
    graphicsMenu.initWindows()
    eventManager.unregisterAllEvents()

    eventManager.registerSeveralsKeyPressEvents(gameEvent.EventPressKeyA(), gameEvent.EventPressKeyE(), gameEvent.EventPressKeyZ(),
        gameEvent.EventPressKeyD(), gameEvent.EventPressKeyQ(), gameEvent.EventPressKeyI(), gameEvent.EventPressKeyP(), gameEvent.EventPressKeyO(),
        gameEvent.EventPressKeyM(), gameEvent.EventPressKeyK(), gameEvent.EventPressKeySpace(), gameEvent.EventPressKeyZero())
    graphicsGame.initWindows()
    eventManager.unregisterAllEvents()
