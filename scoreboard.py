from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.goto(-100,200)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100,200)
        self.write(f"{self.l_score}",align="left",font=("Courier",40,"normal"))
        self.goto(100,200)
        self.write(f"{self.r_score}",align="right",font=("Courier",40,"normal"))

    def increase_left_score(self):
        self.l_score += 1
        self.update_scoreboard()

    def increase_right_score(self):
        self.r_score += 1
        self.update_scoreboard()