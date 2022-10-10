import libs.cng as cng
import utils.debug as debug
import utils.screenProperties as screenProperties
import event.eventManager as eventManager
from chapter.menu.menuRenderer import MenuRenderer
import utils.timeGame as timeGame
import entity.player as player
import utils.calligraphy as calligraphy
import trajectories.trajectoryType as trajectoryType
from utils.graph.fpsGraph import FpsGraph
from utils.graph.renderCalculGraph import RenderCalculGraph
import utils.logger.logger as logger
import utils.report.timeReport as timeReport
from time import time, sleep

firstRenderer = None

def initWindows():
    global firstRenderer
    cng.init_window("Duel dans le ciel - Choix des avions", screenProperties.getWidth(), screenProperties.getHeight(), True)
    cng.setIconApplicationPhoto("../../../textures/symbols/icon_menu.png")
    firstRenderer = MenuRenderer()
    run()

def run():
    logs = logger.Logger()
    fpsGrph = FpsGraph()
    renderCalculGraph = RenderCalculGraph()

    lastTimeCheckedFps = time()
    lastTimeCheckedTicks = time()
    lastTimeBeforeRender = time()


    frames = 0

    renderer = firstRenderer

    while not cng.idle_dead():
        renderer.loadEntities()
        renderer.registerEvents()
        fpsGrph.rendererChange(renderer.getName())
        renderCalculGraph.rendererChange(renderer.getName())

        while not cng.idle_dead() and not renderer.isEnded():

            # Update each 1 / 60 sec
            refreshTime = 1 / 60
            currentTime = time()
            updateCount = 0
            timeRemaining = currentTime - lastTimeBeforeRender
            while timeRemaining > refreshTime:
                updateCount += 1
                timeRemaining -= refreshTime

            if updateCount != 0:
                lastTimeBeforeRender = currentTime

                renderCalculGraph.startCalculCounter()
                renderer.calcul(updateCount)
                renderCalculGraph.endCalculCounter()

                cng.clear_screen()

                renderCalculGraph.startRenderCounter()
                renderer.render(updateCount)
                renderCalculGraph.endRenderCounter()

                renderCalculGraph.addUpdateToGraph()
                cng.refresh()
                frames += 1

                if time() - lastTimeCheckedTicks >= 0.05:
                    timeGame.increaseTicks()
                    lastTimeCheckedTicks = time()

            if time() - lastTimeCheckedFps >= 1:
                fpsGrph.addFpsCount(timeGame.getFps())
                timeGame.setFps(frames)
                frames = 0
                lastTimeCheckedFps = time()

        eventManager.unregisterAllEvents()
        if not renderer.hasNext():
            break
        renderer = renderer.next()()

    debug.l("Logger", "Zip old files")
    logs.zipAllOldLogs()
    debug.l("Logger", "Zip ended")

    debug.l("Logger", "Create log...")
    logs.createLogFolder()
    renderCalculGraph.saveGraph(logger.LOG_FOLDER_NAME + '/' + logger.last_folder_name_created + '/' + "perf.png")
    fpsGrph.saveGraph(logger.LOG_FOLDER_NAME + '/' + logger.last_folder_name_created + '/' + "fps.png")
    debug.success("Logger", "Log successfully created")

if __name__ == "__main__":
    debug.setDebugMode(0)
    if not calligraphy.isWork():
        debug.error("calligraphy", "Calligraphy not working.")
        debug.error("calligraphy", "Application stopped")
        exit()

    calligraphy.loadCalligraphy('../../../calligraphy/retro_gaming.ttf', 'retro gaming', True)
    trajectoryType.initTrajectories()

    player.Player(1)
    player.Player(2)
    if debug.getDebugMode() == 2:
        timeReport.startGame(initWindows)
    else:
        initWindows()
