from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("/mnt/d/Git/python/020_SnakeGameP1/data.txt") as data:
            self.highscore = data.read()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        with open("/mnt/d/Git/python/020_SnakeGameP1/data.txt") as data:
            self.highscore = data.read()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)
    
    def reset(self):
        if self.score > int(self.highscore):
            self.highscore = self.score
            with open("/mnt/d/Git/python/020_SnakeGameP1/data.txt", mode="w") as data:
                data.write(f"{self.score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()