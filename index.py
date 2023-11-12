from time import sleep
from screen import Screen
from snake import Snake
from control import Control
from food import Food
from collisionDetection import CollisionDetection

delay = 0.1
screen = Screen()
snake = Snake()
control = Control(snake, screen)
food = Food(screen)
food.moveToRandom()
collisionDetection = CollisionDetection()

# Main game loop
while True:
    screen.getWindow().update()

    if collisionDetection.snakeHitsScreenEdge(snake, screen):
        snake.reset()

    if collisionDetection.snakeIsCollidingWithFood(snake, food, screen):
        food.moveToRandom()

    control.move()

    sleep(delay)

window.mainloop()
