from food import Food
from screen import Screen
from snake import Snake

class CollisionDetection:
    def snakeHitsScreenEdge(self, snake: Snake, screen: Screen):
        min = screen.getMin()
        max = screen.getMax()
        x = snake.getSnakeHead().xcor()
        y = snake.getSnakeHead().ycor()

        if x < min or x > max or y < min or y > max:
            return True

        return False

    def snakeIsCollidingWithFood(self, snake: Snake, food: Food, screen: Screen):
        return snake.getSnakeHead().distance(food.food) < screen.step