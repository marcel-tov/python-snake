import turtle
from screen import Screen

class Control:
    directionDown = "down"
    directionUp = "up"
    directionLeft = "left"
    directionRight = "right"

    def __init__(self, head, screen: Screen):
        self.head = head
        self.screen = screen

    def addKeyboardBindings(self, window: turtle):
        window.listen()
        window.onkeypress(self.goUp, "w")
        window.onkeypress(self.goDown, "s")
        window.onkeypress(self.goLeft, "a")
        window.onkeypress(self.goRight, "d")

    def goUp(self):
        if self.head.direction != self.directionDown:
            self.head.direction = self.directionUp

    def goDown(self):
        if self.head.direction != self.directionUp:
            self.head.direction = self.directionDown

    def goLeft(self):
        if self.head.direction != self.directionRight:
            self.head.direction = self.directionLeft

    def goRight(self):
        if self.head.direction != self.directionLeft:
            self.head.direction = self.directionRight

    def move(self):
        if self.head.direction == self.directionUp:
            y = self.head.ycor()
            self.head.sety(y + self.screen.step)

        if self.head.direction == self.directionDown:
            y = self.head.ycor()
            self.head.sety(y - self.screen.step)

        if self.head.direction == self.directionLeft:
            x = self.head.xcor()
            self.head.setx(x - self.screen.step)

        if self.head.direction == self.directionRight:
            x = self.head.xcor()
            self.head.setx(x + self.screen.step)
