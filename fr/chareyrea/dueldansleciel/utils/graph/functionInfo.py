class FunctionInfo:

    def __init__(self, name, color="black", legend=None):
        self.name = name
        self.color = color
        self.legend = name if legend == None else legend

    def getName(self):
        return self.name

    def getColor(self):
        return self.color

    def getLegend(self):
        return self.legend
