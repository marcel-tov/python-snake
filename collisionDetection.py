from food import Food
from screen import Screen
from snake import Snake

class CollisionDetection:
    def snakeHitsScreenEdge(self, snake: Snake, screen: Screen):
        min = screen.getMin()
        max = screen.getMax()
        x = snake.head.xcor()
        y = snake.head.ycor()

        if x < min or x > max or y < min or y > max:
            return True

        return False

    def snakeIsCollidingWithFood(self, snake: Snake, food: Food, screen: Screen):
        return snake.head.distance(food.food) < screen.step

    def snakeIsCollidingWithItself(self, snake: Snake, screen: Screen):
        for segment in snake.segments:
            if segment.distance(snake.head) < screen.step:
                return True

        return False
