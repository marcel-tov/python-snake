from food import Food
from screen import Screen
from snake import Snake

class CollisionDetection:
    def snakeHitsScreenEdge(self, snake: Snake, screen: Screen):
        min_screen = screen.getMin()
        max_screen = screen.getMax()
        x = snake.head.xcor()
        y = snake.head.ycor()

        if x < min_screen or x > max_screen or y < min_screen or y > max_screen:
            return True

        return False

    def snakeIsCollidingWithFood(self, snake: Snake, food: Food, screen: Screen):
        return snake.head.distance(food.food) < screen.step

    def snakeIsCollidingWithItself(self, snake: Snake, screen: Screen):
        for segment in snake.segments:
            if segment.distance(snake.head) < screen.step:
                return True

        return False
