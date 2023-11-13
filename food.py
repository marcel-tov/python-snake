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
        step = self.screen.step
        min_screen = self.screen.getMin()
        max_screen = self.screen.getMax()

        return self.getRandom(min_screen + (step / 2), max_screen - step)

    def getRandomY(self):
        step = self.screen.step
        min_screen = self.screen.getMin()
        max_screen = self.screen.getMax()

        return self.getRandom(min_screen + step, max_screen - (step / 2))

    def getRandom(self, min_screen, max_screen):
        random = -1
        step = self.screen.step

        while (random % step != 0):
            random = randint(min_screen, max_screen)

        return random
