# Importiert alle Module
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Importieren der Klassen aus den anderen Dateien
coffe_machine = CoffeeMaker()
coffe_menu = Menu()
coin_machine = MoneyMachine()


# end_of_operation Variable zum definieren, wann die Kaffemaschine stoppt
end_of_operation = False

# Die Kaffeemaschine läuft in einer endlosschleife, bis der User 'off' eingibt.
while not end_of_operation:
    # Zeigt die Verfügbaren Getränke an
    print("\nWillkommen bei Pera AG. Was darf es heute für sie sein?\n")
    print(coffe_menu.get_items())
    user_choice = input("\nBitte wählen sie ihr Getränk: ")

    # Zeigt einen Report der Zutaten und des Kontostandes an
    if user_choice == 'report':
        coffe_machine.report()
        coin_machine.report()
    # Schaltet die Maschine aus
    elif user_choice == 'off':
        end_of_operation = True
    # Gibt das Produkt aus
    else:
        # Sucht das Getränk im Menü
        user_beverage = coffe_menu.find_drink(user_choice)
        # Prüft ob Genug Resourcen und Geld vorhanden ist
        if coffe_machine.is_resource_sufficient(user_beverage) and coin_machine.make_payment(user_beverage.cost):
            # Macht den Kaffee
            coffe_machine.make_coffee(user_beverage)