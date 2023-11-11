import turtle

class Control:
    def __init__(self, head):
        self.head = head

    def addKeyboardBindings(self, wn: turtle):
        wn.listen()
        wn.onkeypress(self.goUp, "w")
        wn.onkeypress(self.goDown, "s")
        wn.onkeypress(self.goLeft, "a")
        wn.onkeypress(self.goRight, "d")

    def goUp(self):
        if self.head.direction != "down":
            self.head.direction = "up"

    def goDown(self):
        if self.head.direction != "up":
            self.head.direction = "down"

    def goLeft(self):
        if self.head.direction != "right":
            self.head.direction = "left"

    def goRight(self):
        if self.head.direction != "left":
            self.head.direction = "right"

    def move(self):
        if self.head.direction == "up":
            y = self.head.ycor()
            self.head.sety(y + 20)

        if self.head.direction == "down":
            y = self.head.ycor()
            self.head.sety(y - 20)

        if self.head.direction == "left":
            x = self.head.xcor()
            self.head.setx(x - 20)

        if self.head.direction == "right":
            x = self.head.xcor()
            self.head.setx(x + 20)
