import time
from screen import Screen

delay = 0.1
screen = Screen()
wn = screen.createScreen()

# Main game loop
while True:
    wn.update()
    time.sleep(delay)

wn.mainloop()
