import random
import os
from art import logo, vs
from game_data import data

def pick_celebrity():
    return random.choice(data)

def celebrity_info(picked_celebrity):
    return f"{picked_celebrity['name']}, a {picked_celebrity['description']}, from {picked_celebrity['country']}"

def compare_celebrities(CelebrityA, CelebrityB):
    if CelebrityA['follower_count'] > CelebrityB['follower_count']:
        return 'a'
    return 'b'

def print_battle(CelebrityA, CelebrityB):
    print(f"Compare A: {celebrity_info(CelebrityA)}")
    print(vs)
    print(f"Against B: {celebrity_info(CelebrityB)}")

def main_game():
    is_Game_Over = False
    game_score = 0

    choiceA = pick_celebrity()
    choiceB = pick_celebrity()

    while choiceA == choiceB:
        choiceB = pick_celebrity()

    print(logo)

    while not is_Game_Over:
        print_battle(choiceA, choiceB)
        user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()

        if user_choice == compare_celebrities(choiceA, choiceB):
            os.system('cls' if os.name == 'nt' else 'clear')
            print(logo)
            game_score += 1
            print(f"You're right! Current score: {game_score}")
            choiceA = choiceB
            choiceB = pick_celebrity()

            while choiceA == choiceB:
                choiceB = pick_celebrity()

        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(logo)
            print(f'Sorry! That\'s wrong :( \n\nFinal Score: {game_score}')
            is_Game_Over = True

main_game()