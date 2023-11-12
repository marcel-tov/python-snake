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
        x = randint(self.screen.getMin(), self.screen.getMax())
        y = randint(self.screen.getMin(), self.screen.getMax())

        self.food.goto(x, y)