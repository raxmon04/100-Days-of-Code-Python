from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# ==== Konfiguration ====
WIDTH, HEIGHT = 800, 600
RIGHT_OUT = 380
LEFT_OUT = -380
WALL_Y = 280
PADDLE_HIT_X = 320
WIN_SCORE = 10

# ==== Screen ====
screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

# ==== Objekte ====
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# ==== Steuerung ====
screen.listen()
screen.onkeypress(r_paddle.move_up, "Up")
screen.onkeypress(r_paddle.move_down, "Down")
screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_down, "s")

# ==== Game Loop ====
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()

    # Wände (oben/unten)
    if ball.ycor() >= WALL_Y or ball.ycor() <= -WALL_Y:
        ball.bounce_y()

    # Paddle-Kollisionen (mit Richtungscheck, um Doppel-Bounces zu vermeiden)
    hit_right = (ball.xcor() > PADDLE_HIT_X and ball.distance(r_paddle) < 50 and ball.x_move > 0)
    hit_left  = (ball.xcor() < -PADDLE_HIT_X and ball.distance(l_paddle) < 50 and ball.x_move < 0)
    if hit_right or hit_left:
        ball.bounce_x()

    # Out of bounds rechts → Punkt für links
    if ball.xcor() > RIGHT_OUT:
        ball.reset_position()
        scoreboard.l_point()

    # Out of bounds links → Punkt für rechts
    if ball.xcor() < LEFT_OUT:
        ball.reset_position()
        scoreboard.r_point()

    # Sieg?
    if scoreboard.l_score >= WIN_SCORE:
        scoreboard.game_over("Left")
        game_is_on = False
    elif scoreboard.r_score >= WIN_SCORE:
        scoreboard.game_over("Right")
        game_is_on = False

    screen.update()

screen.exitonclick()
