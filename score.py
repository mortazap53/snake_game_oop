from turtle import Turtle

Alignment = "center"
Font = ("courier", 24, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("black")
        self.goto(0, 267)
        self.hideturtle()
        self.write(f"SCORE: {self.score}", align=Alignment, font=Font)

    def get_score(self):
        self.clear()
        self.score += 1
        self.write(f"SCORE: {self.score}", align=Alignment, font=Font)