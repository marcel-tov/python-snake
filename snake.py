import turtle

from food import Food
from screen import Screen

class Snake:
    def create(self):
        self.snake = turtle.Turtle()
        self.snake.speed(0)
        self.snake.shape("square")
        self.snake.color("green")
        self.snake.penup()
        self.reset()

        return self.snake

    def reset(self):
        self.snake.home()
        self.snake.direction = "stop"
