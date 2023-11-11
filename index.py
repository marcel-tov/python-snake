import time
from screen import Screen
from snake import Snake
from control import Control

delay = 0.1
wn = Screen().createScreen()
head = Snake().createHead()
control = Control(head)

# Keyboard bindings
wn.listen()
wn.onkeypress(control.go_up, "w")
wn.onkeypress(control.go_down, "s")
wn.onkeypress(control.go_left, "a")
wn.onkeypress(control.go_right, "d")

# Main game loop
while True:
    wn.update()

    control.move()

    time.sleep(delay)

wn.mainloop()
