from food import Food
from screen import Screen
from snake import Snake

class CollisionDetection:
    def snake_hits_screen_edge(self, snake: Snake, screen: Screen):
        min_screen = screen.get_min()
        max_screen = screen.get_max()
        x = snake.head.xcor()
        y = snake.head.ycor()

        if x < min_screen or x > max_screen or y < min_screen or y > max_screen:
            return True

        return False

    def snake_is_colliding_with_food(self, snake: Snake, food: Food, screen: Screen):
        return snake.head.distance(food.food) < screen.step

    def snake_is_colliding_with_itself(self, snake: Snake, screen: Screen):
        for segment in snake.segments:
            if segment.distance(snake.head) < screen.step:
                return True

        return False
