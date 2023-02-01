from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
import pyglet

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
'''screen.tracer and screen.update to eliminate animation'''
screen.tracer(0)

song = pyglet.media.load('GW.mp3')
song.play()

scoreboard = Scoreboard()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball((0, 0))

screen.listen()
screen.onkeypress(fun=r_paddle.go_up, key="Up")
screen.onkeypress(fun=r_paddle.go_down, key="Down")
screen.onkeypress(fun=l_paddle.go_up, key="w")
screen.onkeypress(fun=l_paddle.go_down, key="s")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.ball_move()
    l_paddle.goto(-350, ball.ycor())
    #Detect collision with wall
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.ybounce()
    #Detect collision with paddle
    if ball.distance(r_paddle) < 70 and ball.xcor() > 320 or ball.distance(l_paddle) < 70 and ball.xcor() < -320:
        ball.xbounce()
        ball.move_speed *= 0.94
    if ball.distance(r_paddle) < 60 and ball.xcor() > 320:
        scoreboard.point()
    #Detect r_paddle misses
    if ball.xcor() > 380:
        scoreboard.reset()
        ball.reset()


screen.exitonclick()
