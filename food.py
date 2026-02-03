from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(random.randint(-270, 270), random.randint(-270, 270))

    def recreate_food(self):
        self.clear()
        self.goto(random.randint(-270, 270), random.randint(-270, 270))