from turtle import Turtle

ALIGNMENT = "center"
SCORE_FONT = ("Courier", 80, "normal")
END_FONT = ("Courier", 32, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.draw_center_line()
        self.update_scoreboard()

    def draw_center_line(self):
        self.goto(0, -300)
        self.setheading(90)
        self.pensize(3)
        for _ in range(30):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)

    def update_scoreboard(self):
        self.clear()           # löscht nur die Turtle-eigenen Drawings (nicht die Centerline, die war mit derselben Turtle gezeichnet)
        self.draw_center_line()# also Centerline erneut zeichnen
        # Scores
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGNMENT, font=SCORE_FONT)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGNMENT, font=SCORE_FONT)

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def game_over(self, winner_text=""):
        self.goto(0, 0)
        msg = f"{winner_text} Player Wins!" if winner_text else "Game Over"
        self.write(msg, align=ALIGNMENT, font=END_FONT)
