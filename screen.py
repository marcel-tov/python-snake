import turtle

class Screen:
    width=600
    height=600
    step=20

    def createScreen(self):
        screen = turtle.Screen()
        screen.title("Snake game")
        screen.setup(width=self.width, height=self.height)
        screen.tracer(0) # Turns off the screen updates

        return screen