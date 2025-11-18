print("Welcome to Treasure Island. Your mission is to find the treasure. ")
choice1 = input("left or right? ")

if choice1 == "left":
    choice2 = input("swim or wait? ")

    if choice2 == "wait":
        choice3 = input("Which colour do you choose? red, blue or yellow ")
        if choice3 == "yellow":
            print("Congratulations you found the treasure!")
        else:
            print("Game Over!")
    else:
        print("Game Over!")
else:
    print("Game Over!")