from utils.graph.functionInfo import FunctionInfo
from utils.graph.function import Function
from utils.graph.point import Point
from utils.graph.graph import Graph

class FpsGraph(Graph):

    def __init__(self):
        super().__init__("Temps (s)", "Fps")
        self.functionFps = Function(FunctionInfo("Fps", "blue"))
        super().addFunction(self.functionFps)
        self.count = 0

    def addFpsCount(self, fpsAmount):
        self.functionFps.addPoint(Point(self.count, fpsAmount))
        self.count += 1

    def rendererChange(self, rendererName):
        super().addVerticalLine(self.count, "red", rendererName)
