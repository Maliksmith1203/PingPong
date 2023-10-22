from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(8)
r_paddle = Paddle(x_cor=350, y_cor=0)
l_paddle = Paddle(x_cor=-350, y_cor=0)
ball = Ball()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(fun=r_paddle.go_up, key="Up")
screen.onkey(fun=r_paddle.go_down, key="Down")
screen.onkey(fun=l_paddle.go_down, key="s")
screen.onkey(fun=l_paddle.go_up, key="w")

game_on = True
collision_count = 0
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()


    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.move_speed *= 0.2



    # detect when R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.increase_left_score()
    # detect when L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.increase_right_score()


screen.exitonclick()
