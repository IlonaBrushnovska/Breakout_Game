import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from brick import Brick
from scoreboard import Scoreboard
from lifeboard import Lifeboard
from game_over import GameOver


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("BREAKOUT GAME")
screen.tracer(0)

paddle = Paddle((0, -250))
ball = Ball((0, -220))
scoreboard = Scoreboard()
lifeboard = Lifeboard()
game_over = GameOver()

screen.listen()
screen.onkey(paddle.go_right, "Right")
screen.onkey(paddle.go_left, "Left")

# Create bricks.
x_list = [-340, -230, -120, -10, 100, 210, 320]
y_list = [280, 255, 230, 205]
brick_list = []
color_list = ["red", "orange", "yellow", "green"]

for x in x_list:
    for y in y_list:
        brick = Brick((x, y))
        brick.color(color_list[y_list.index(y)])
        brick_list.append(brick)


# Count score with different levels of bricks.
def point(brick):
    if brick.fillcolor() == "green":
        scoreboard.score += 1
    if brick.fillcolor() == "yellow":
        scoreboard.score += 5
    if brick.fillcolor() == "orange":
        scoreboard.score += 10
    if brick.fillcolor() == "red":
        scoreboard.score += 20
    scoreboard.update_scoreboard()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

# Detect collision with side wall.
    if ball.xcor() < -380 or ball.xcor() > 380:
        ball.bounce_x()

# Detect collision with puddle.
    if ball.distance(paddle) < 70 and ball.ycor() < -230:
        ball.bounce_paddle()

# Detect collision with top.
    if ball.ycor() > 280:
        ball.bounce_y()

# Detect collision with bottom.
    if ball.ycor() < -280:
        ball.reset_position()
        paddle.goto(0, -250)
        lifeboard.miss_ball()

# Detect collision with bricks.
    for brick in brick_list:
        if (brick.ycor() - 20 <= ball.ycor() <= brick.ycor() + 20) and (brick.xcor() - 60 < ball.xcor() < brick.xcor() + 60):
            ball.bounce_brick()
            brick.hideturtle()
            brick_list.remove(brick)
            point(brick)

# The end of the game.
    if lifeboard.life == 0:
        game_over.write(f"GAME OVER!\nYour score: {scoreboard.score}", align="center", font=("Courier", 20, "bold"))
        game_is_on = False

screen.exitonclick()