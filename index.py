from time import sleep
from screen import Screen
from snake import Snake
from control import Control
from food import Food

delay = 0.1
screen = Screen()
window = screen.createScreen()
snake = Snake().create()
control = Control(snake, screen)
control.addKeyboardBindings(window)
food = Food(screen)
food.moveToRandom()

# Main game loop
while True:
    window.update()

    control.move()

    sleep(delay)

window.mainloop()
