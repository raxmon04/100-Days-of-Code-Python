import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# === Screen ===
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# === Objekte ===
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()


# === Steuerung ===
screen.listen()
screen.onkeypress(player.move_up, "Up")

# === Game Loop ===
def run_game():
    game_is_on = True
    while game_is_on:
        time.sleep(0.1)

        car_manager.create_car()
        car_manager.move_car()
        car_manager.cleanup()

        for car in car_manager.all_cars:
            if player.distance(car) < 30:
                scoreboard.reset()
                player.reset()
                car_manager.reset()

        if player.reached_top():
            car_manager.increase_speed()
            scoreboard.level_done()

        screen.update()

run_game()
