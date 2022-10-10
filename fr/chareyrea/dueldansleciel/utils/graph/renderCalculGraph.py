from utils.graph.functionInfo import FunctionInfo
from utils.graph.function import Function
from utils.graph.point import Point
from utils.graph.graph import Graph
from time import time, time_ns

class RenderCalculGraph(Graph):

    def __init__(self):
        super().__init__("Update", "% d'utilisation")
        self.functionRender = Function(FunctionInfo("Render %", "blue"))
        self.functionCalcul = Function(FunctionInfo("Calcul %", "cyan"))
        super().addFunction(self.functionRender)
        super().addFunction(self.functionCalcul)
        self.timeRenderStart = 0
        self.timeRender = 0
        self.timeCalculStart = 0
        self.timeCalcul = 0
        self.count = 0
        self.skipped = False

    def startRenderCounter(self):
        if not self.skipped:
            self.timeRenderStart = time_ns()

    def endRenderCounter(self):
        self.timeRender = time_ns() - self.timeRenderStart

    def startCalculCounter(self):
        if not self.skipped:
            self.timeCalculStart = time_ns()

    def endCalculCounter(self):
        self.timeCalcul = time_ns() - self.timeCalculStart

    def addUpdateToGraph(self):
        if self.timeRender != 0 and self.timeCalcul != 0:
            p1 = Point(self.count, self.timeRender / (self.timeRender + self.timeCalcul))
            p2 = Point(self.count, self.timeCalcul / (self.timeRender + self.timeCalcul))
            self.functionRender.addPoint(p1)
            self.functionCalcul.addPoint(p2)
            self.skipped = False
        else:
            self.skipped = True
        self.count += 1

    def rendererChange(self, rendererName):
        super().addVerticalLine(self.count, "red", rendererName)
