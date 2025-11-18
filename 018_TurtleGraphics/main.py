import turtle as t
import random
tim = t.Turtle()

# import colorgram

# rgb_colors = []
# colors = colorgram.extract("/mnt/d/Git/python/018_TurtleGraphics/image.jpg", 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)

# print(rgb_colors)
tim.hideturtle()
tim.speed(0)
t.colormode(255)
color_list = [(245, 243, 237), (248, 241, 244), (238, 240, 246), (201, 164, 112), (239, 246, 241), (152, 75, 50), (221, 201, 138), (57, 95, 126), (170, 152, 44), (138, 31, 20), (135, 163, 183), (196, 94, 75), (49, 121, 88), (143, 177, 149), (95, 75, 77), (76, 39, 32), (164, 146, 157), (16, 98, 71), (232, 176, 165), (54, 46, 48), (32, 61, 76), (22, 83, 89), 
            (182, 204, 176), (141, 22, 25), (86, 147, 127), (45, 66, 85), (8, 68, 53), (177, 94, 97), (222, 177, 182), (109, 128, 151)]

def color_dot():
    tim.color(random.choice(color_list))
    tim.dot(20)
    tim.up()
    tim.fd(50)

def back_to_left():
    tim.left(90)
    tim.fd(50)
    tim.left(90)
    tim.fd(500)
    tim.left(180)

for _ in range(10):
    for _ in range(10):
        color_dot()
    back_to_left()

screen = t.Screen()
screen.exitonclick()