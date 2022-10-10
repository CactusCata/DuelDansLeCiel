import libs.cng as cng
import utils.debug as debug

events = {"keyPress": [], "click": []}

def registerKeyPressEvent(event):
    """
    Register a key event
    """
    events["keyPress"] += [event]
    cng.assoc_key(event.getKeyName(), event.getFunction())

def registerSeveralsKeyPressEvents(*events):
    """
    Register severals key event
    """
    for e in events:
        registerKeyPressEvent(e)

def registerClickEvent(event):
    """
    Register a click event
    """
    events["click"] += [event]
    cng.assoc_button(event.getKeyName(), event.getFunction())

def registerSeveralsClickEvents(*events):
    """
    Register severals key event
    """
    for e in events:
        registerClickEvent(e)

def unregisterKeyPressEvent(event):
    """
    Unregister key event
    """
    if not event in events["keyPress"]:
        debug.warning("Event", "Couldn't unregisterEvent " + str(event))
    else:
        events["keyPress"].remove(event)
        cng.unassoc_key(event.getKeyName())

def unregisterClickEvent(event):
    """
    Unregister click event
    """
    if not event in events["click"]:
        debug.warning("Event", "Couldn't unregisterEvent " + str(event))
    else:
        events["click"].remove(event)
        cng.unassoc_key(event.getKeyName())

def unregisterAllEvents():
    """
    Unregister all events (click and key)
    """
    for keyPressEvent in events["keyPress"]:
        unregisterKeyPressEvent(keyPressEvent)
    for clickEvent in events["click"]:
        unregisterClickEvent(clickEvent)
