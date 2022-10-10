from event.event import Event
import chapter.renderer as renderMenu
import entity.airplane.airplaneType as airplaneType

class EventPressKeyRight(Event):

    def __init__(self):
        super().__init__("Right")

    def func(self):
        menuRend = renderMenu.getRenderer()
        menuRend.setMenuCursor((menuRend.getMenuCursor() + 1) % len(airplaneType.getAirplanesTypes()))

class EventPressKeyLeft(Event):

    def __init__(self):
        super().__init__("Left")

    def func(self):
        menuRend = renderMenu.getRenderer()
        menuRend.setMenuCursor((menuRend.getMenuCursor() - 1) % len(airplaneType.getAirplanesTypes()))

class EventPressKeyReturn(Event):

    def __init__(self):
        super().__init__("Return")

    def func(self):
        menuRend = renderMenu.getRenderer()
        menuRend.menuEnter()
