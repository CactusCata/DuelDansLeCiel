import os # Those 2 lines are present for an obscure reason which make that work
os.system("")

textColor = {"black": 30, "red": 31, "green": 32, "yellow": 33, "blue": 34, "purple": 35, "cyan": 46, "white": 37}
backgroundColor = {"black": 40, "red": 41, "green": 42, "yellow": 43, "blue": 44, "purple": 45, "cyan": 46, "white": 47}
textStyle = {"no_effect": 0, "bold": 1, "underline": 2, "neg1": 3, "neg2": 5}

GRAY_LABEL_CHAR = "\033[7m"
RED_LABEL_CHAR = "\033[41m"
GREEN_LABEL_CHAR = "\033[42m"
ORANGE_LABEL_CHAR = "\033[43m"
RESET_CHAR = "\033[0m"

def buildColor(colorName, backGroundColorName = "black", textStyleName = "no_effect"):
    colorName = colorName.lower()
    backGroundColorName = backGroundColorName.lower()
    textStyleName = textStyleName.lower()

    if not(colorName in textColor):
        print(buildColor("red", backGroundColorName="black", textStyleName="bold") + "ColorName isn't correct, select one of them:", str(textColor.keys()) + RESET_CHAR)
        raise ValueError
        return
    if not(backGroundColorName in backgroundColor):
        print(buildColor("red", backGroundColorName="black", textStyleName="bold") + "BackgroundColorName isn't correct, select one of them:", str(backgroundColor.keys()) + RESET_CHAR)
        raise ValueError
        return
    if not(textStyleName in textStyle):
        print(buildColor("red", backGroundColorName="black", textStyleName="bold") + "TextStyleName isn't correct, select one of them:", str(textStyle.keys()) + RESET_CHAR)
        raise ValueError
        return

    return "\033[%d;%d;%dm" % (textStyle[textStyleName], textColor[colorName], backgroundColor[backGroundColorName])
