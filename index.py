import turtle
import time
import random

delay = 0.1

#set up screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor('yellow')
wn.setup(width=600, height=600)
wn.tracer(0)

#snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

#snake food
# TODO add snake food here

#scoreboards
# TODO show scoreboard

def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_left():
    if head.direction != "right":
        head.direction = "left"
def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    # TODO: Move to down
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    #TODO: move to right

#keyboard bindings
wn.listen()
wn.onkeypress(go_up, "Up")
# TODO move to down is missing, Use go_down here
wn.onkeypress(go_left, "Left")
# TODO move to right is missing. Use go_right here

# Main game loop
while True:
    wn.update()

    #TODO: check collision with border area
        # TODO: if head collied reset to 0,0
        # TODO: update scoreboard
    #TODO: check collision with food
        #TODO move the food to random place
            # random.randint(): https://docs.python.org/3/library/random.html#random.randint
            # goto(x, y): https://docs.python.org/3/library/turtle.html#turtle.goto
        # TODO: update scoreboard


    #TODO: move the segments in reverse order

    move()

    #TODO: check for collision with body
        # TODO: update scoreboard

    time.sleep(delay)

wn.mainloop()
