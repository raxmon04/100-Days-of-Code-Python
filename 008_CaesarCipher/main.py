# Importiert die Variable logo vom File art.py
from art import logo

# Eine Liste aller Buchstaben im Alphabet in kleinbuchstaben
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# Funktion "Caesar", hier wird die encryption und decryption durchgeführt
def caesar(original_text, shift_amount, encode_or_decode):
    # Ein leerer String in der Variable end_cipher, welcher später gefüllt wird
    end_cipher = ""

    # Hier wird abgefragt, ob der Benutzer den Text "encoden" oder "decoden" will
    if encode_or_decode == "decode":
        # Der Shift wechselt von positiv zu negativ wenn die Option decode gewählt wurde
        shift_amount *= -1

    # Für alle Buchstaben im Text, welcher vom User angegeben wird, wird der Cipher ermittelt
    for letter in original_text:
        # Hier wird geprüft, ob "letter" in der Variable "alphabet" enthalten ist
        if letter in alphabet:
            # Hier wird die Position ermittel, dazu wird der Index, also der Ort wo sich der Buchstabe befindet gezählt und danach + oder - den shift gerechnet 
            # Bsp. a = 0 + 5 shift = 5
            position = alphabet.index(letter) + shift_amount
            # Dank dieser Linie wird sichergestellt, dass, falls der Index + shift höher als 26 ist, es wider von 1 anfängt. Bsp. 27 % 26 = 1 oder 24 % 26 = 24
            position %= len(alphabet)
            # Hier wird die Position des Buchstaben im alphabet ermittelt und dem "end_cipher" hinzugefügt
            end_cipher += alphabet[position]
        # Falls die Eingabe im Text kein Buchstabe aus dem Alphabet ist, wird dieses Zeichen einfach dem "end_cipher" angehängt
        else:
            end_cipher += letter    
    
    print(f"Here is the {encode_or_decode}d result: {end_cipher}")

print(logo)

use_caesar_again = "yes"

# Schleife, welche sicherstellt, das die Abfrage solange des User "yes" eingibt, durchläuft
while use_caesar_again == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    use_caesar_again = input("Type 'yes' if you want to go again. Otherwise, type 'no': ")
