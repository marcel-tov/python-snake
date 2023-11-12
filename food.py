import turtle
from random import randint
from screen import Screen

class Food:
    food: turtle

    def __init__(self, screen: Screen):
        self.screen = screen

    def __init__(self):
        self.food = turtle.Turtle()
        self.food.speed(0)
        self.food.shape("square")
        self.food.color("red")
        self.food.penup()
        self.food.goto(0, 0)
        self.food.direction = "stop"

    def moveToRandom(self):
        x = randint(-290, 290)
        y = randint(-290, 290)

        self.food.goto(x, y)