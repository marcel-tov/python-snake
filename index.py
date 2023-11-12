from time import sleep
from screen import Screen
from snake import Snake
from control import Control
from food import Food

delay = 0.1
screen = Screen()
window = screen.createScreen()
head = Snake().createHead()
control = Control(head, screen)
control.addKeyboardBindings(window)
food = Food()
food.moveToRandom()

# Main game loop
while True:
    window.update()

    control.move()

    sleep(delay)

window.mainloop()
