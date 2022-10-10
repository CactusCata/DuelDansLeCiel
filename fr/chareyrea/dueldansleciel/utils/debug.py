import utils.messagecolor as messagecolor

"""
debugMode:
    - 0: aucun output
    - 1: tous les output sauf les warning
    - 2: tous les output / enable hitbox
"""
debugMode = 2

infoLabel = messagecolor.GRAY_LABEL_CHAR
infoColor = messagecolor.buildColor("white")
successLabel = messagecolor.GREEN_LABEL_CHAR
successColor = messagecolor.buildColor("green")
warningLabel = messagecolor.ORANGE_LABEL_CHAR
warningColor = messagecolor.buildColor("yellow")
errorLabel = messagecolor.RED_LABEL_CHAR
errorColor = messagecolor.buildColor("red")

def setDebugMode(debugModeA):
    global debugMode
    debugMode = debugModeA

def sendMessage(label, group, color, message):
    if debugMode == 1 or debugMode == 2:
        print(label + '[' + group.upper() + ']' + messagecolor.RESET_CHAR + color + ': ' + str(message) + messagecolor.RESET_CHAR)

def l(group, message):
    """
    log message
    """
    sendMessage(infoLabel, group, infoColor, message)

def lIf(group, message, condition):
    if condition:
        l(group, message)

def success(group, message):
    """
    success message
    """
    sendMessage(successLabel, group, successColor, message)

def successIf(group, message, condition):
    if condition:
        success(group, message, condition)

def warning(group, message):
    """
    warning message
    """
    if debugMode == 2:
        sendMessage(warningLabel, group, warningColor, message)

def warningIf(group, message, condition):
    if condition:
        warning(group, message)

def error(group, message):
    """
    error message
    """
    sendMessage(errorLabel, group, errorColor, message)

def errorIf(group, message, condition):
    if condition:
        error(group, message)

def setDebugMode(mode):
    global debugMode
    debugMode = mode

def getDebugMode():
    return debugMode
