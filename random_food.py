from random import randint
from collision_detection import CollisionDetection
from screen import Screen
from food import Food
from snake import Snake

class RandomFood:
    def __init__(self, screen: Screen,
                snake: Snake,
                food: Food,
                collision_detection: CollisionDetection):
        self.screen = screen
        self.snake = snake
        self.food = food
        self.collision_detection = collision_detection

    def move_to_random(self):
        x = self.get_random_x()
        y = self.get_random_y()

        self.food.food.goto(x, y)

    def get_random_x(self):
        step = self.screen.step
        min_screen = self.screen.get_min()
        max_screen = self.screen.get_max()

        return self.get_random(min_screen + (step / 2), max_screen - step)

    def get_random_y(self):
        step = self.screen.step
        min_screen = self.screen.get_min()
        max_screen = self.screen.get_max()

        return self.get_random(min_screen + step, max_screen - (step / 2))

    def get_random(self, min_screen, max_screen):
        random = -1
        step = self.screen.step

        while random % step != 0:
            random = randint(min_screen, max_screen)

        return random
