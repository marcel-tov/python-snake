import turtle

class Snake:
    def createHead(self):
        head = turtle.Turtle()
        head.speed(0)
        head.shape("square")
        head.color("black")
        head.penup()
        head.goto(0, 0)
        head.direction = "stop"

        return head
