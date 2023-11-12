from time import sleep
from screen import Screen
from snake import Snake
from control import Control
from food import Food
from collisionDetection import CollisionDetection

delay = 0.1
screen = Screen()
window = screen.createScreen()
snake = Snake()
snakeHead = snake.create()
control = Control(snakeHead, screen)
control.addKeyboardBindings(window)
food = Food(screen)
food.moveToRandom()
collisionDetection = CollisionDetection()

# Main game loop
while True:
    window.update()

    if collisionDetection.isSnakeHitsScreenEdge(snakeHead, screen):
        snake.reset()

    if collisionDetection.isSnakeCollidingWithFood(snakeHead, food, screen):
        food.moveToRandom()

    control.move()

    sleep(delay)

window.mainloop()
