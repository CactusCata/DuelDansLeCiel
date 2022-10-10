def convertHealthToColor(maxHealth, health):
    """
    return a triplet which represent (R, G, B) structure
    and convert the ration between health on maxHealth
    to get a color between red (0%) and green (100%)
    """
    x = ((maxHealth - health) * 255 * 2) // maxHealth
    R = x if x <= 255 else 255
    G = 255 * 2 - x if x > 255 else 255
    return (R, G, 0)
