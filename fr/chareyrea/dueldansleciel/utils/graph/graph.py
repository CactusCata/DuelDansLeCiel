from matplotlib import pyplot as plt

class Graph:

    def __init__(self, xAbscisseName=None, yAbscisseName=None):
        self.functions = set()
        self.verticalsLines = set()
        self.xAbscisseName = xAbscisseName
        self.yAbscisseName = yAbscisseName

    def saveGraph(self, asName):

        for f in self.functions:

            info = f.getFunctionInfo()
            points = f.getPoints()

            abscisse = []
            ordonnee = []

            for p in points:
                abscisse.append(p.getX())
                ordonnee.append(p.getY())

            plt.plot(abscisse, ordonnee, info.getColor(), label=info.getLegend())

        for vertLine in self.verticalsLines:
            plt.axvline(x=vertLine[0]).set_color(vertLine[1])
            if vertLine[2] != None:
                plt.text(vertLine[0], 0, vertLine[2], rotation=90)

        plt.legend(loc="upper left")

        if self.xAbscisseName != None:
            plt.xlabel(self.xAbscisseName)
        if self.yAbscisseName != None:
            plt.ylabel(self.yAbscisseName)

        plt.grid()
        plt.savefig(asName)
        plt.close()

    def addFunction(self, *functions):
        for f in functions:
            self.functions.add(f)

    def addVerticalLine(self, x, color="black", legend=None):
        """
        legend param can be equal to None.
        If is legend equal to None, he will not displayed
        """
        self.verticalsLines.add((x, color, legend))
