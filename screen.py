import turtle

class Screen:
    width=600
    height=width
    step=20

    def __init__(self):
        self.window = self.create_window()

    def create_window(self):
        window = turtle.Screen()
        window.title("Snake game")
        window.setup(self.width, self.height)
        window.tracer(0)

        return window

    def get_min_max(self):
        return self.width / 2

    def get_min(self):
        return -abs(self.get_min_max())

    def get_max(self):
        return self.get_min_max()
