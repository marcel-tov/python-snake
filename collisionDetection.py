import turtle
from food import Food
from screen import Screen

class CollisionDetection:
    def isSnakeCollidingWithFood(self, snakeHead: turtle.Turtle, food: Food, screen: Screen):
        return snakeHead.distance(food.food) < screen.step