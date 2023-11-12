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
        if self.snake.getSnakeHead().direction != self.directionDown:
            self.snake.getSnakeHead().direction = self.directionUp

    def goDown(self):
        if self.snake.getSnakeHead().direction != self.directionUp:
            self.snake.getSnakeHead().direction = self.directionDown

    def goLeft(self):
        if self.snake.getSnakeHead().direction != self.directionRight:
            self.snake.getSnakeHead().direction = self.directionLeft

    def goRight(self):
        if self.snake.getSnakeHead().direction != self.directionLeft:
            self.snake.getSnakeHead().direction = self.directionRight

    def move(self):
        if self.snake.getSnakeHead().direction == self.directionUp:
            y = self.snake.getSnakeHead().ycor()
            self.snake.getSnakeHead().sety(y + self.screen.step)

        if self.snake.getSnakeHead().direction == self.directionDown:
            y = self.snake.getSnakeHead().ycor()
            self.snake.getSnakeHead().sety(y - self.screen.step)

        if self.snake.getSnakeHead().direction == self.directionLeft:
            x = self.snake.getSnakeHead().xcor()
            self.snake.getSnakeHead().setx(x - self.screen.step)

        if self.snake.getSnakeHead().direction == self.directionRight:
            x = self.snake.getSnakeHead().xcor()
            self.snake.getSnakeHead().setx(x + self.screen.step)
