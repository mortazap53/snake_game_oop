from turtle import Turtle

positions = [(0, 0), (-20, 0), (-40, 0)]

class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.snake_body = []
        self.shape("circle")
        self.color("black")
        self.create_snake()

    def create_snake(self):
        for position in positions:
            body_part = Turtle(shape="square")
            body_part.penup()
            body_part.goto(position)
            self.snake_body.append(body_part)







