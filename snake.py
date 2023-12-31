import turtle
from screen import Screen

class Snake:
    segments = []

    def __init__(self, screen: Screen):
        self.screen = screen
        self.head = self.create_body("green")
        self.reset()

    def reset(self):
        self.head.home()
        self.head.direction = "stop"

        for segment in self.segments:
            x = self.screen.get_max() + self.screen.step + 1
            y = x
            segment.goto(x, y)

        self.segments.clear()

    def create_body(self, color = "grey"):
        body = turtle.Turtle()
        body.speed(0)
        body.shape("square")
        body.color(color)
        body.penup()

        return body

    def add_segment(self):
        self.segments.append(self.create_body())

    def move(self):
        for i in range(len(self.segments) -1, 0, -1):
            x = self.segments[i - 1].xcor()
            y = self.segments[i - 1].ycor()
            self.segments[i].goto(x, y)

        if len(self.segments) > 0:
            x = self.head.xcor()
            y = self.head.ycor()
            self.segments[0].goto(x, y)
