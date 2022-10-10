import platform

screensize = (1000, 600)

if platform.system() == "Windows":
    import ctypes
    user32 = ctypes.windll.user32
    screensize = (user32.GetSystemMetrics(0), user32.GetSystemMetrics(1))
elif platform.system() == "Linux":
    import subprocess
    p = subprocess.Popen(['xrandr'], stdout=subprocess.PIPE)
    p2 = subprocess.Popen(['grep', '*'], stdin=p.stdout, stdout=subprocess.PIPE)
    p.stdout.close()
    resolution_string, junk = p2.communicate()
    resolution = resolution_string.split()[0]
    width, height = resolution.split('x')
    screensize = (width, height)


def getWidth():
    return screensize[0]

def getHeight():
    return screensize[1]
