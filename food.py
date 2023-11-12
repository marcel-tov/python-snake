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

    def moveToRandom(self):
        x = self.getRandom()
        y = self.getRandom()

        self.food.goto(x, y)

    def getRandom(self):
        random = -1
        step = self.screen.step

        while (random % step != 0):
            random = randint(self.screen.getMin() + step, self.screen.getMax() - step)

        return random
