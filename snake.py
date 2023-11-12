import turtle

class Snake:
    def create(self):
        snake = turtle.Turtle()
        snake.speed(0)
        snake.shape("square")
        snake.color("green")
        snake.penup()
        snake.home()
        snake.direction = "stop"

        return snake
