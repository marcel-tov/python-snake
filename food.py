import turtle
from random import randint
from screen import Screen

class Food:
    def __init__(self, screen: Screen):
        self.screen = screen

        self.food = turtle.Turtle()
        self.food.speed(0)
        self.food.shape("square")
        self.food.color("red")
        self.food.penup()
        self.food.goto(0, 0)
        self.food.direction = "stop"

    def move_to_random(self):
        x = self.get_random_x()
        y = self.get_random_y()

        self.food.goto(x, y)

    def get_random_x(self):
        step = self.screen.step
        min_screen = self.screen.get_min()
        max_screen = self.screen.get_max()

        return self.get_random(min_screen + (step / 2), max_screen - step)

    def get_random_y(self):
        step = self.screen.step
        min_screen = self.screen.get_min()
        max_screen = self.screen.get_max()

        return self.get_random(min_screen + step, max_screen - (step / 2))

    def get_random(self, min_screen, max_screen):
        random = -1
        step = self.screen.step

        while random % step != 0:
            random = randint(min_screen, max_screen)

        return random
