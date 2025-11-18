import os
import random
from art import logo

def pick_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards_hand):
    if len(cards_hand) == 2 and sum(cards_hand) == 21:
        return 0
    if 11 in cards_hand and sum(cards_hand) > 21:
        cards_hand[cards_hand.index(11)] = 1
    return sum(cards_hand)
    
def compare_scores(user_score, dealer_score):
    if dealer_score > 21 and user_score > 21:
        return "You loose, because you went over 21"
    if user_score == dealer_score:
        return "You both have the same Score, it's a draw"
    elif dealer_score == 0:
        return "Dealer has Blackjack! You loose"
    elif user_score == 0:
        return "User has Blackjack! You win!"
    elif user_score > 21:
        return "You went over 21. You loose!"
    elif dealer_score > 21:
        return "Dealer went over 21. You win!"
    elif user_score > dealer_score:
        return "You win!"
    else:
        return "You loose!"

def setup_hands(computer_hand, user_hand): 
    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)
    computer_hand.clear()
    user_hand.clear()
    for i in range(2):
        user_hand.append(pick_card())
        computer_hand.append(pick_card())

def play_single_hand(hand, dealers_hand, bet, balance):
    isGameOver = False
    doubled = False
    while not isGameOver:
        players_score = calculate_score(hand)
        dealers_score = calculate_score(dealers_hand)
        print(f"You cards: {hand} | your score: {players_score}")
        print(f"Dealer's first card: {dealers_hand[0]}")
        if players_score == 0 or dealers_score == 0 or players_score > 21:
            isGameOver = True
        elif len(hand) == 2:
            action = input("Type 'y' to hit, 'n' to stand, or 'd' to double: ")
            if action == "d":
                if balance < bet:
                    print("Not enough balance to double!")
                    continue
                hand.append(pick_card())
                players_score = calculate_score(hand)
                print(f"You cards: {hand} | your score: {players_score}")
                isGameOver = True
                doubled = True
                continue
            elif action == "y":
                hand.append(pick_card())
            else:
                isGameOver = True
        else:
            pick_again = input("Would you like to pick another card? Type 'y' or 'n' ")
            if pick_again == "y":
                hand.append(pick_card())
            else:
                isGameOver = True
    return hand, doubled

def play_game(balance):
    dealers_hand = []
    players_hand = []
    setup_hands(dealers_hand, players_hand)

    print(f"Your current balance: {balance}")
    while True:
        try:
            bet = int(input("How much would you like to bet? "))
            if bet > balance or bet <= 0:
                print("Invalid bet amount.")
            else:
                break
        except:
            print("Please enter a valid number.")

    split_hands = []
    split_bet = bet
    split_used = False
    if players_hand[0] == players_hand[1]:
        split = input(f"Your cards: {players_hand}. Type 's' to split or any other key to continue: ")
        if split.lower() == "s":
            if balance < bet * 2:
                print("Not enough balance to split!")
            else:
                split_hands = [
                    [players_hand[0], pick_card()],
                    [players_hand[1], pick_card()]
                ]
                split_used = True

    total_win = 0
    if split_hands:
        final_scores = []
        doubles = []
        for idx, hand in enumerate(split_hands):
            print(f"\n--- Playing split hand {idx+1} ---")
            finished_hand, doubled = play_single_hand(hand, dealers_hand, bet, balance)
            final_scores.append(finished_hand)
            doubles.append(doubled)
        dealers_score = calculate_score(dealers_hand)
        while dealers_score != 0 and dealers_score < 17:
            dealers_hand.append(pick_card())
            dealers_score = calculate_score(dealers_hand)
        print(f"\nDealers final score is: {dealers_score} \nDealers final hand is: {dealers_hand}")
        for idx, hand in enumerate(final_scores):
            players_score = calculate_score(hand)
            hand_bet = bet * 2 if doubles[idx] else bet
            result = compare_scores(players_score, dealers_score)
            print(f"\nYour final score for hand {idx+1} is: {players_score} \nYour final hand is: {hand}")
            print(f"{result}")
            if players_score == 0 and dealers_score != 0:
                win = int(hand_bet * 1.5)
                print(f"Blackjack! You win {win}")
                total_win += win
            elif "win" in result.lower():
                print(f"You win {hand_bet}")
                total_win += hand_bet
            elif "draw" in result.lower():
                print("It's a draw, your bet is returned.")
            else:
                print(f"You loose {hand_bet}")
                total_win -= hand_bet
        balance += total_win
    else:
        isGameOver = False
        doubled = False
        while not isGameOver:
            players_score = calculate_score(players_hand)
            dealers_score = calculate_score(dealers_hand)
            print(f"You cards: {players_hand} | your score: {players_score}")
            print(f"Dealer's first card: {dealers_hand[0]}")
            if players_score == 0 or dealers_score == 0 or players_score > 21:
                isGameOver = True
            elif len(players_hand) == 2:
                action = input("Type 'y' to hit, 'n' to stand, or 'd' to double: ")
                if action == "d":
                    if balance < bet:
                        print("Not enough balance to double!")
                        continue
                    players_hand.append(pick_card())
                    players_score = calculate_score(players_hand)
                    print(f"You cards: {players_hand} | your score: {players_score}")
                    isGameOver = True
                    doubled = True
                    continue
                elif action == "y":
                    players_hand.append(pick_card())
                else:
                    isGameOver = True
            else:
                pick_again = input("Would you like to pick another card? Type 'y' or 'n' ")
                if pick_again == "y":
                    players_hand.append(pick_card())
                else:
                    isGameOver = True
        dealers_score = calculate_score(dealers_hand)
        while dealers_score != 0 and dealers_score < 17:
            dealers_hand.append(pick_card())
            dealers_score = calculate_score(dealers_hand)
        print(f"\nYour final score is: {players_score} \nYour final hand is: {players_hand}")
        print(f"\nDealers final score is: {dealers_score} \nDealers final hand is: {dealers_hand}")
        result = compare_scores(players_score, dealers_score)
        hand_bet = bet * 2 if doubled else bet
        if players_score == 0 and dealers_score != 0:
            win = int(hand_bet * 1.5)
            print(f"Blackjack! You win {win}")
            balance += win
        elif "win" in result.lower():
            print(f"You win {hand_bet}")
            balance += hand_bet
        elif "draw" in result.lower():
            print("It's a draw, your bet is returned.")
        else:
            print(f"You loose {hand_bet}")
            balance -= hand_bet
    print(f"\nYour new balance: {balance}")
    return balance

balance = 500
while balance > 0 and input("\nWould you like to play a game of blackjack (y/n) ") == 'y':
    os.system('cls' if os.name == 'nt' else 'clear')
    balance = play_game(balance)
if balance <= 0:
    print("You are out of money! Game over.")