from time import sleep
from screen import Screen
from snake import Snake
from control import Control
from food import Food
from collisionDetection import CollisionDetection
from score import Score

DELAY = 0.1
screen = Screen()
snake = Snake(screen)
control = Control(snake, screen)
food = Food(screen)
food.move_to_random()
collisionDetection = CollisionDetection()
score = Score()

def reset_game():
    snake.reset()
    food.move_to_random()
    score.reset()
    sleep(1)

# Main game loop
while True:
    screen.window.update()

    if collisionDetection.snake_hits_screen_edge(snake, screen) or collisionDetection.snake_is_colliding_with_itself(snake, screen):
        reset_game()

    if collisionDetection.snake_is_colliding_with_food(snake, food, screen):
        score.increment_score()
        food.move_to_random()
        snake.add_segment()

    snake.move()
    control.move()

    sleep(DELAY)

screen.window.mainloop()
