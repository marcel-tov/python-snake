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
        x = self.getRandomX()
        y = self.getRandomY()

        self.food.goto(x, y)

    def getRandomX(self):
        random = -1
        step = self.screen.step
        min = self.screen.getMin()
        max = self.screen.getMax()

        while (random % step != 0):
            random = randint(min + (step / 2), max - step)

        return random

    def getRandomY(self):
        random = -1
        step = self.screen.step
        min = self.screen.getMin()
        max = self.screen.getMax()

        while (random % step != 0):
            random = randint(min + step, max - (step / 2))

        return random
