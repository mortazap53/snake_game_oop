from turtle import Turtle

Alignment = "center"
Font = ("courier", 22, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
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
        self.score = 0
        self.show_score()

    def save_high_score(self):
        return self.high_score