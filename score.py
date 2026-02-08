from turtle import Turtle

Alignment = "center"
Font = ("courier", 22, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open(file= "data.txt", mode="r") as data:
            self.high_score = int(data.read())
        self.penup()
        self.color("black")
        self.goto(0, 267)
        self.hideturtle()
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(f"SCORE: {self.score}" " " f"High Score: {self.high_score}", align=Alignment, font=Font)

    def get_score(self):
        self.score += 1
        self.show_score()

    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(file="data.txt", mode="w") as set_high_score:
                set_high_score.write(str(self.high_score))
        self.score = 0
        self.show_score()
