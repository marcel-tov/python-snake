from screen import Screen
from snake import Snake

class Control:
    directionDown = "down"
    directionUp = "up"
    directionLeft = "left"
    directionRight = "right"

    def __init__(self, snake: Snake, screen: Screen):
        self.snake = snake
        self.screen = screen
        self.addKeyboardBindings()

    def addKeyboardBindings(self):
        self.screen.getWindow().listen()
        self.screen.getWindow().onkeypress(self.goUp, "w")
        self.screen.getWindow().onkeypress(self.goDown, "s")
        self.screen.getWindow().onkeypress(self.goLeft, "a")
        self.screen.getWindow().onkeypress(self.goRight, "d")

    def goUp(self):
        if self.snake.getHead().direction != self.directionDown:
            self.snake.getHead().direction = self.directionUp

    def goDown(self):
        if self.snake.getHead().direction != self.directionUp:
            self.snake.getHead().direction = self.directionDown

    def goLeft(self):
        if self.snake.getHead().direction != self.directionRight:
            self.snake.getHead().direction = self.directionLeft

    def goRight(self):
        if self.snake.getHead().direction != self.directionLeft:
            self.snake.getHead().direction = self.directionRight

    def move(self):
        if self.snake.getHead().direction == self.directionUp:
            y = self.snake.getHead().ycor()
            self.snake.getHead().sety(y + self.screen.step)

        if self.snake.getHead().direction == self.directionDown:
            y = self.snake.getHead().ycor()
            self.snake.getHead().sety(y - self.screen.step)

        if self.snake.getHead().direction == self.directionLeft:
            x = self.snake.getHead().xcor()
            self.snake.getHead().setx(x - self.screen.step)

        if self.snake.getHead().direction == self.directionRight:
            x = self.snake.getHead().xcor()
            self.snake.getHead().setx(x + self.screen.step)
