import utils.debug as debug

class Event:
    """
    Mother class of KeyEvent and ClickEvent
    """

    def __init__(self, keyName):
        self.keyName = keyName

    def getKeyName(self):
        return self.keyName

    def func(self):
        """
        Function which is executed when event is called
        """
        debug.warn("Event function", "This event with key " + getKeyName() + " wasn't initialized")

    def getFunction(self):
        return self.func
