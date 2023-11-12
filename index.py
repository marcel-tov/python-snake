from time import sleep
from screen import Screen
from snake import Snake
from control import Control
from food import Food

delay = 0.1
wn = Screen().createScreen()
head = Snake().createHead()
control = Control(head)
control.addKeyboardBindings(wn)
food = Food()
food.moveToRandom()

# Main game loop
while True:
    wn.update()

    control.move()

    sleep(delay)

wn.mainloop()
