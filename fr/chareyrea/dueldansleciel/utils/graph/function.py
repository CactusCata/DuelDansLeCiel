class Function:

    def __init__(self, functionInfo):
        self.functionInfo = functionInfo
        self.points = []

    def addPoint(self, *point):
        for p in point:
            self.points.append(p)

    def getPoints(self):
        return self.points

    def getFunctionInfo(self):
        return self.functionInfo
