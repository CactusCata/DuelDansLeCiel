import event
import graphicsMenu
import airPlaneType

class EventPressKeyRight(event.Event):

    def __init__(self):
        event.Event.__init__(self, "Right")

    def func(self):
        graphicsMenu.setMenuCursor((graphicsMenu.menuCursor + 1) % len(airPlaneType.getAirPlanesTypes()))

class EventPressKeyLeft(event.Event):

    def __init__(self):
        event.Event.__init__(self, "Left")

    def func(self):
        graphicsMenu.setMenuCursor((graphicsMenu.menuCursor - 1) % len(airPlaneType.getAirPlanesTypes()))

class EventPressKeyReturn(event.Event):

    def __init__(self):
        event.Event.__init__(self, "Return")

    def func(self):
        graphicsMenu.setMenuEnter(True)
