from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.goto(-200, 240)
        self.hideturtle()
        self.level = 1
        with open("/mnt/d/Git/python/023_TurtleCrossing/data.txt") as data:
            self.highscore = data.read()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        with open("/mnt/d/Git/python/023_TurtleCrossing/data.txt") as data:
            self.highscore = data.read()
        self.write(f"Level: {self.level}\nHigh Score: {self.highscore}", align="center", font=FONT)

    def level_done(self):
        self.level += 1
        self.update_scoreboard()

    def reset(self):
        if self.level > int(self.highscore):
            with open("/mnt/d/Git/python/023_TurtleCrossing/data.txt", mode="w") as data:
                data.write(f"{self.level}")
        self.level = 1
        self.update_scoreboard()
