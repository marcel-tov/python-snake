import turtle

class Screen:
    width=600
    height=width
    step=20

    def __init__(self):
        self.window = self.createWindow()

    def createWindow(self):
        window = turtle.Screen()
        window.title("Snake game")
        window.setup(self.width, self.height)
        window.tracer(0)

        return window

    def getMinMax(self):
        return self.width / 2

    def getMin(self):
        return -abs(self.getMinMax())

    def getMax(self):
        return self.getMinMax()