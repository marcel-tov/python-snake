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
        self.screen.window.listen()
        self.screen.window.onkeypress(self.goUp, "w")
        self.screen.window.onkeypress(self.goDown, "s")
        self.screen.window.onkeypress(self.goLeft, "a")
        self.screen.window.onkeypress(self.goRight, "d")

    def goUp(self):
        if self.snake.head.direction != self.directionDown:
            self.snake.head.direction = self.directionUp

    def goDown(self):
        if self.snake.head.direction != self.directionUp:
            self.snake.head.direction = self.directionDown

    def goLeft(self):
        if self.snake.head.direction != self.directionRight:
            self.snake.head.direction = self.directionLeft

    def goRight(self):
        if self.snake.head.direction != self.directionLeft:
            self.snake.head.direction = self.directionRight

    def move(self):
        if self.snake.head.direction == self.directionUp:
            y = self.snake.head.ycor()
            self.snake.head.sety(y + self.screen.step)

        if self.snake.head.direction == self.directionDown:
            y = self.snake.head.ycor()
            self.snake.head.sety(y - self.screen.step)

        if self.snake.head.direction == self.directionLeft:
            x = self.snake.head.xcor()
            self.snake.head.setx(x - self.screen.step)

        if self.snake.head.direction == self.directionRight:
            x = self.snake.head.xcor()
            self.snake.head.setx(x + self.screen.step)
