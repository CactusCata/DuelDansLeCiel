def convertHealthToColor(maxHealth, health):
    x = ((maxHealth - health) * 255 * 2) // maxHealth
    R = x if x <= 255 else 255
    G = 255 * 2 - x if x > 255 else 255
    return (R, G, 0)
