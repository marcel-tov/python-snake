import turtle

class Screen:
    def createScreen(self):
        screen = turtle.Screen()
        screen.title("Snake game")
        screen.setup(width=600, height=600)
        screen.tracer(0) # Turns off the screen updates

        return screen
