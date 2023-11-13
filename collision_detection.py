import turtle
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

    def snake_head_is_colliding_with_food(self, snake: Snake, food: turtle, screen: Screen):
        return snake.head.distance(food) < screen.step

    def snake_is_colliding_with_itself(self, snake: Snake, screen: Screen):
        for segment in snake.segments:
            if segment.distance(snake.head) < screen.step:
                return True

        return False

    def snake_is_colliding_with_food(self, snake: Snake, food: turtle, screen: Screen):
        segment_hits_food = False
        for segment in snake.segments:
            if segment.distance(snake.head) < screen.step:
                segment_hits_food = True
                break

        return self.snake_head_is_colliding_with_food(snake, food, screen) or \
               segment_hits_food
