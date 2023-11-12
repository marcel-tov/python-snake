from food import Food
from screen import Screen
from snake import Snake

class CollisionDetection:
    def isSnakeHitsScreenEdge(self, snake: Snake, screen: Screen):
        min = screen.getMin()
        max = screen.getMax()
        x = snake.getSnakeHead().xcor()
        y = snake.getSnakeHead().ycor()

        if x < min or x > max or y < min or y > max:
            return True

        return False

    def isSnakeCollidingWithFood(self, snake: Snake, food: Food, screen: Screen):
        return snake.getSnakeHead().distance(food.food) < screen.step