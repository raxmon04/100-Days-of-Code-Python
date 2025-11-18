from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(
    title="Make your bet",
    prompt="Which color turtle will win the race? Enter a color: "
)
if user_bet:
    user_bet = user_bet.strip().lower()

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for i in range(6):
    t = Turtle(shape="turtle")
    t.color(colors[i])
    t.penup()  # alias zu .up(), ist klarer
    t.goto(x=-230, y=y_positions[i])
    all_turtles.append(t)

if user_bet:  # nur starten, wenn der Nutzer was eingegeben hat
    is_race_on = True

finish_x = 230

while is_race_on:
    for t in all_turtles:
        # erst bewegen, dann Ziel prüfen
        t.forward(random.randint(0, 10))
        if t.xcor() > finish_x:
            is_race_on = False
            winning_color = t.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
            break  # inneren loop beenden

screen.exitonclick()