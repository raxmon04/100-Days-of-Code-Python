from data import MENU, resources

# initialize the variable to control the game length, get the ingredients for each beverage
endOfOperation = False
espresso_ingredients = MENU['espresso']['ingredients']
latte_ingredients = MENU['latte']['ingredients']
cappuccino_ingredients = MENU['cappuccino']['ingredients']


def generate_report():
    """ Function that generates the report about the resources left in the machine """
    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}g')
    print(f'Money: ${resources["money"]}')


def dispense_beverage(type_of_beverage):
    """ Function that dispenses the beverage type that is given by the user selection and requests payment """
    # if espresso
    if type_of_beverage == 1:
        # check resources espresso and if true -> request payment from the user, otherwise we say the coffee machine
        # ran out of resources.
        if check_resources(espresso_ingredients['water'], espresso_ingredients['milk'], espresso_ingredients['coffee']):
            request_payment(MENU['espresso']['cost'], 'espresso')
        else:
            print('Not Enough Resources to make the desired drink')
    # latte
    elif type_of_beverage == 2:
        # check resources latte and if true -> request payment from the user, otherwise we say the coffee machine ran
        # out of resources.
        if check_resources(latte_ingredients['water'], latte_ingredients['milk'], latte_ingredients['coffee']):
            request_payment(MENU['latte']['cost'], 'latte')
        else:
            print('Not Enough Resources to make the desired drink')
    # cappuccino
    elif type_of_beverage == 3:
        # check resources espresso and if true -> request payment from the user, otherwise we say the coffee machine
        # ran out of resources.
        if check_resources(cappuccino_ingredients['water'], cappuccino_ingredients['milk'],
                           cappuccino_ingredients['coffee']):
            request_payment(MENU['cappuccino']['cost'], 'cappuccino')
        else:
            print('Not Enough Resources to make the desired drink')
    # in case user enters invalid drink
    else:
        print('Invalid beverage selection')


def check_resources(water_required, milk_required, coffee_required):
    """ Function returns true if there are enough resources for the drink recipe, false otherwise """
    return resources['water'] >= water_required and resources['milk'] >= milk_required and resources[
        'coffee'] >= coffee_required


def request_payment(cost_of_beverage, beverage_type):
    """ This function requests coins from the user and if provided sufficient amount, dispenses coffee """

    # collect all the coins and determine monetary value
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))
    quarters_value = quarters * 0.25
    dimes_value = dimes * 0.1
    nickels_value = nickels * 0.05
    pennies_value = pennies * 0.01
    total_money_given = quarters_value + dimes_value + nickels_value + pennies_value

    # in case the user didn't provide enough money, we refund and return
    if total_money_given < cost_of_beverage:
        print(f"Insufficient balance. Your ${total_money_given} are refunded.")
    # dispense beverage and give change
    else:
        print(f"{beverage_type} is dispensing... Enjoy!")
        change = total_money_given - cost_of_beverage
        print(f"Here's your change of ${change}!")
        # remove resources from the coffee machine
        subtract_resources(cost_of_beverage, beverage_type)


def subtract_resources(cost_of_beverage, beverage_type):
    resources['water'] -= MENU[beverage_type]['ingredients']['water']
    resources['milk'] -= MENU[beverage_type]['ingredients']['milk']
    resources['coffee'] -= MENU[beverage_type]['ingredients']['coffee']
    resources['money'] += cost_of_beverage

def refill():
    """Refill machine to full capacity."""
    resources['water'] = 300
    resources['milk'] = 200
    resources['coffee'] = 100
    print("Machine refilled to full capacity:")
    generate_report()

while not endOfOperation:
    print("Welcome to the coffee machine! Please take a look at our menu!")
    print("\n1. Espresso: $1.5\n2. Latte: $2.5\n3. Cappuccino: $3.0\n")
    command_selection = input(
        'Select the beverage you would like (1./2./3.), "report" to display the machine\'s resources or "refill" to refill the machine\'s resources ')

    if command_selection == 'report':
        generate_report()
    elif command_selection == 'off':
        endOfOperation = True
    elif command_selection == 'refill':
        refill()
    else:
        int_command = int(command_selection)
        dispense_beverage(int_command)