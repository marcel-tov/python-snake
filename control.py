import turtle
from screen import Screen

class Control:
    directionDown = "down"
    directionUp = "up"
    directionLeft = "left"
    directionRight = "right"

    def __init__(self, snakeHead: turtle.Turtle, screen: Screen):
        self.snakeHead = snakeHead
        self.screen = screen

    def addKeyboardBindings(self, window: turtle):
        window.listen()
        window.onkeypress(self.goUp, "w")
        window.onkeypress(self.goDown, "s")
        window.onkeypress(self.goLeft, "a")
        window.onkeypress(self.goRight, "d")

    def goUp(self):
        if self.snakeHead.direction != self.directionDown:
            self.snakeHead.direction = self.directionUp

    def goDown(self):
        if self.snakeHead.direction != self.directionUp:
            self.snakeHead.direction = self.directionDown

    def goLeft(self):
        if self.snakeHead.direction != self.directionRight:
            self.snakeHead.direction = self.directionLeft

    def goRight(self):
        if self.snakeHead.direction != self.directionLeft:
            self.snakeHead.direction = self.directionRight

    def move(self):
        if self.snakeHead.direction == self.directionUp:
            y = self.snakeHead.ycor()
            self.snakeHead.sety(y + self.screen.step)

        if self.snakeHead.direction == self.directionDown:
            y = self.snakeHead.ycor()
            self.snakeHead.sety(y - self.screen.step)

        if self.snakeHead.direction == self.directionLeft:
            x = self.snakeHead.xcor()
            self.snakeHead.setx(x - self.screen.step)

        if self.snakeHead.direction == self.directionRight:
            x = self.snakeHead.xcor()
            self.snakeHead.setx(x + self.screen.step)
