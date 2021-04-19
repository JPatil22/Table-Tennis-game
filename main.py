from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("PING PONG")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(l_paddle.go_up, "Up")
screen.onkey(l_paddle.go_down, "Down")
screen.onkey(r_paddle.go_up, "w")
screen.onkey(r_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.Bounce_y()
# collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 48 and ball.xcor() < -320:
        ball.Bounce_x()
    # miss from right paddle
    if ball.xcor() > 380:
        ball.reset_pos()
        score.l_point()

    # miss from left paddle
    if ball.xcor() < -380:
        ball.reset_pos()
        score.r_point()

screen.exitonclick()
