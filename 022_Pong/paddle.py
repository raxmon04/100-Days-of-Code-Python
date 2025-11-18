from turtle import Turtle

MOVE_DISTANCE = 20
TOP_LIMIT = 250
BOTTOM_LIMIT = -250

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)  # 20px * 5 = 100px hoch
        self.color("white")
        self.speed("fastest")
        self.goto(position)

    def move_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        if new_y > TOP_LIMIT:
            new_y = TOP_LIMIT
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        if new_y < BOTTOM_LIMIT:
            new_y = BOTTOM_LIMIT
        self.goto(self.xcor(), new_y)
