from math import atan, pi

def calculAngle(oldPoint, newPoint, defaultAngle):
    """
    Compute orientation of airplane in degree
    defaultAngle is gived if the angle can't be calculated
    is equals to airPlaneOrientation
    """
    try:
        a = (newPoint[1] - oldPoint[1]) / (newPoint[0] - oldPoint[0])
        b = newPoint[1] - a * newPoint[0]
        x_base = -b / a
        angle = atan(newPoint[1] / (newPoint[0] - x_base))
        if newPoint[0] > oldPoint[0]:
            angle -= pi / 2
        else:
            angle += pi / 2
        angle = ((angle * 180) / pi) % 360
        return angle
    except ZeroDivisionError:
        return defaultAngle
