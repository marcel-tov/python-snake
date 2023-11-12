import turtle
from food import Food
from screen import Screen

class CollisionDetection:
    def isSnakeHitsScreenEdge(self, snakeHead: turtle.Turtle, screen: Screen):
        min = screen.getMin()
        max = screen.getMax()
        x = snakeHead.xcor()
        y = snakeHead.ycor()

        if x < min or x > max or y < min or y > max:
            return True

        return False

    def isSnakeCollidingWithFood(self, snakeHead: turtle.Turtle, food: Food, screen: Screen):
        return snakeHead.distance(food.food) < screen.step