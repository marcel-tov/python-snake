import turtle
from screen import Screen

class Control:
    directionDown = "down"
    directionUp = "up"
    directionLeft = "left"
    directionRight = "right"

    def __init__(self, snake: turtle.Turtle, screen: Screen):
        self.snake = snake
        self.screen = screen

    def addKeyboardBindings(self, window: turtle):
        window.listen()
        window.onkeypress(self.goUp, "w")
        window.onkeypress(self.goDown, "s")
        window.onkeypress(self.goLeft, "a")
        window.onkeypress(self.goRight, "d")

    def goUp(self):
        if self.snake.direction != self.directionDown:
            self.snake.direction = self.directionUp

    def goDown(self):
        if self.snake.direction != self.directionUp:
            self.snake.direction = self.directionDown

    def goLeft(self):
        if self.snake.direction != self.directionRight:
            self.snake.direction = self.directionLeft

    def goRight(self):
        if self.snake.direction != self.directionLeft:
            self.snake.direction = self.directionRight

    def move(self):
        if self.snake.direction == self.directionUp:
            y = self.snake.ycor()
            self.snake.sety(y + self.screen.step)

        if self.snake.direction == self.directionDown:
            y = self.snake.ycor()
            self.snake.sety(y - self.screen.step)

        if self.snake.direction == self.directionLeft:
            x = self.snake.xcor()
            self.snake.setx(x - self.screen.step)

        if self.snake.direction == self.directionRight:
            x = self.snake.xcor()
            self.snake.setx(x + self.screen.step)
