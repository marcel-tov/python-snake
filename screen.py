import turtle

class Screen:
    width=600
    height=width
    step=20

    def createScreen(self):
        screen = turtle.Screen()
        screen.title("Snake game")
        screen.setup(width=self.width, height=self.height)
        screen.tracer(0) # Turns off the screen updates

        return screen

    def getMinMax(self):
        return (self.width / 2) - (self.step / 2)

    def getMin(self):
        return -abs(self.getMinMax())

    def getMax(self):
        return self.getMinMax()