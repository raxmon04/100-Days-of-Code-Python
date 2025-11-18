from turtle import Turtle
import random

START_SPEED = 0.1
MIN_SPEED = 0.02  # untere Grenze für sleep (je kleiner, desto schneller)
STEP = 10

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_move = STEP
        self.y_move = STEP
        self.move_speed = START_SPEED

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        # leicht beschleunigen, aber begrenzen
        self.move_speed = max(self.move_speed * 0.9, MIN_SPEED)

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = START_SPEED
        # Starte in die Gegenrichtung auf X
        self.bounce_x()
        # Gib Y eine kleine zufällige Neigung, damit Starts variieren
        self.y_move = random.choice([-STEP, STEP])
