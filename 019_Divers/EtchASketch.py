from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def clear():
    tim.clear()
    tim.up()
    tim.home()
    tim.down()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def move_left():
    tim.left(10)

def move_right():
    tim.right(10)

screen.listen()
screen.onkeypress(move_forwards, "w")
screen.onkeypress(move_backwards, "s")
screen.onkeypress(move_left, "a")
screen.onkeypress(move_right, "d")
screen.onkey(clear, "c")
screen.exitonclick()