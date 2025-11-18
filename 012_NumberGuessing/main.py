import random
from art import logo

EASY_LEVEL_GUESSES = 10
HARD_LEVEL_GUESSES = 5
START_BALANCE = 500
PAYOUT_MULTIPLIER = 1.8

def game_difficulty():
    while True:
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        if difficulty == 'easy':
            return EASY_LEVEL_GUESSES
        elif difficulty == 'hard':
            return HARD_LEVEL_GUESSES
        else:
            print("Invalid input. Please type 'easy' or 'hard'.")

def guess_outcome(player_guess, computer_number):
    if player_guess == computer_number:
        print(f"You got it! The answer was {computer_number}.")
        return True
    elif player_guess > computer_number:
        print("Too high.\nGuess again.")
    else:
        print("Too low.\nGuess again.")
    return False

def game(balance):
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print(f"Your current balance: {balance} CHF")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        try:
            bet = int(input("How much do you want to bet? "))
            if bet > balance:
                print("You cannot bet more than your current balance.")
            elif bet <= 0:
                print("Please enter a positive number.")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")

    number = random.randint(1, 100)
    attempts = game_difficulty()

    win = False
    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        try:
            player_number = int(input("Make a guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess_outcome(player_number, number):
            win = True
            break
        attempts -= 1

    if win:
        payout = int(bet * PAYOUT_MULTIPLIER)
        print(f"You win {payout} CHF!")
        balance += payout
    else:
        print(f"You've run out of guesses. The number was {number}.")
        print(f"You lose {bet} CHF.")
        balance -= bet

    print(f"Your new balance: {balance} CHF")
    return balance

balance = START_BALANCE
retry = True
while retry and balance > 0:
    balance = game(balance)
    if balance <= 0:
        print("You have lost all your money. Game over!")
        break
    again = input("Do you want to play again? Type 'yes' or 'no': ").lower()
    if again != 'yes':
        retry = False
        print("Thanks for playing! Goodbye!")