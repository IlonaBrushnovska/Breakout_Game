from turtle import Turtle


class Lifeboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("green")
        self.penup()
        self.hideturtle()
        self.life = 5
        self.update_lifeboard()

    def update_lifeboard(self):
        self.clear()
        self.goto(-300, -230)
        self.write(f"Lives: {self.life}", align="center", font=("Courier", 20, "bold"))

    def miss_ball(self):
        self.life -= 1
        self.update_lifeboard()

