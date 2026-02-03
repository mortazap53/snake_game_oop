from turtle import Turtle

positions = [(0, 0), (-20, 0), (-40, 0)]
move_distance = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for position in positions:
            body_part = Turtle(shape="circle")
            body_part.penup()
            body_part.goto(position)
            self.snake_body.append(body_part)

    def move(self):
        for num in range(len(self.snake_body) -1, 0, -1):
            x = self.snake_body[num - 1].xcor()
            y = self.snake_body[num - 1].ycor()
            self.snake_body[num].goto(x, y)
        self.head.forward(move_distance)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)










