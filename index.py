from time import sleep
from screen import Screen
from snake import Snake
from control import Control
from food import Food
from collisionDetection import CollisionDetection

delay = 0.1
screen = Screen()
snake = Snake(screen)
control = Control(snake, screen)
food = Food(screen)
food.moveToRandom()
collisionDetection = CollisionDetection()

def resetGame():
    snake.reset()
    sleep(1)

# Main game loop
while True:
    screen.window.update()

    if collisionDetection.snakeHitsScreenEdge(snake, screen):
        resetGame()

    if collisionDetection.snakeIsCollidingWithFood(snake, food, screen):
        food.moveToRandom()
        snake.addSegment()

    snake.move()
    control.move()

    # Check for head collision with the body segments
    if collisionDetection.snakeIsCollidingWithItself(snake, screen):
        resetGame()

    sleep(delay)

screen.window.mainloop()