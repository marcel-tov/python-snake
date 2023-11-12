import turtle

class Snake:
    def __init__(self):
        self.snakeHead = self.createSnakeHead()

    def createSnakeHead(self):
        self.snakeHead = turtle.Turtle()
        self.snakeHead.speed(0)
        self.snakeHead.shape("square")
        self.snakeHead.color("green")
        self.snakeHead.penup()
        self.reset()

        return self.snakeHead

    def reset(self):
        self.snakeHead.home()
        self.snakeHead.direction = "stop"

    def getSnakeHead(self):
        return self.snakeHead
