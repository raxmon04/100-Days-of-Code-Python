from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
Y_POSITIONS = [-230, -200, -150, -100, -50, 0, 50, 100, 150, 200, 230]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        if random.randint(1, 6) == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.goto(300, random.choice(Y_POSITIONS))
            new_car.setheading(180)
            self.all_cars.append(new_car)
        
    def move_car(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def reset(self):
        for car in self.all_cars:
            car.hideturtle()
        self.all_cars.clear()
        self.car_speed = STARTING_MOVE_DISTANCE
        self.create_car()

    def cleanup(self):
        alive = []
        for car in self.all_cars:
            if car.xcor() > -340:
                alive.append(car)
            else:
                car.hideturtle()
        self.all_cars = alive
            
    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT

