import turtle

class Food:
    def __init__(self):
        self.food = turtle.Turtle()
        self.food.speed(0)
        self.food.shape("square")
        self.food.color("red")
        self.food.penup()
        self.food.goto(0, 0)
        self.food.direction = "stop"
