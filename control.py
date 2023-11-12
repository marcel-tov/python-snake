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
        self.screen.window.onkeypress(self.goUp, "Up")
        self.screen.window.onkeypress(self.goDown, "Down")
        self.screen.window.onkeypress(self.goLeft, "Left")
        self.screen.window.onkeypress(self.goRight, "Right")

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
        x = self.snake.head.xcor()
        y = self.snake.head.ycor()
        step = self.screen.step

        if self.snake.head.direction == self.directionUp:
            self.snake.head.sety(y + step)

        if self.snake.head.direction == self.directionDown:
            self.snake.head.sety(y - step)

        if self.snake.head.direction == self.directionLeft:
            self.snake.head.setx(x - step)

        if self.snake.head.direction == self.directionRight:
            self.snake.head.setx(x + step)
