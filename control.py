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
        self.add_keyboard_bindings()

    def add_keyboard_bindings(self):
        self.screen.window.listen()
        self.screen.window.onkeypress(self.go_up, "w")
        self.screen.window.onkeypress(self.go_down, "s")
        self.screen.window.onkeypress(self.go_left, "a")
        self.screen.window.onkeypress(self.go_right, "d")
        self.screen.window.onkeypress(self.go_up, "Up")
        self.screen.window.onkeypress(self.go_down, "Down")
        self.screen.window.onkeypress(self.go_left, "Left")
        self.screen.window.onkeypress(self.go_right, "Right")

    def go_up(self):
        if self.snake.head.direction != self.directionDown:
            self.snake.head.direction = self.directionUp

    def go_down(self):
        if self.snake.head.direction != self.directionUp:
            self.snake.head.direction = self.directionDown

    def go_left(self):
        if self.snake.head.direction != self.directionRight:
            self.snake.head.direction = self.directionLeft

    def go_right(self):
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
