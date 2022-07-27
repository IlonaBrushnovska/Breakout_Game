from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.goto(position)
        self.x_move = random.choice([5, 7, 10])
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def bounce_paddle(self):
        self.y_move *= -1
        self.move_speed *= 0.9

    def bounce_brick(self):
        self.y_move *= -1
        self.x_move *= 1.05
        self.y_move *= 1.05

    def reset_position(self):
        self.goto(0, -220)
        self.move_speed = 0.1
        self.bounce_y()






