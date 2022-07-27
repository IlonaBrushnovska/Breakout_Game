from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("red")
        self.penup()
        self.hideturtle()
        self.score = 0

    def update_scoreboard(self):
        self.clear()
        self.goto(300, -230)
        self.write(f"Score: {self.score}", align="center", font=("Courier", 20, "bold"))




