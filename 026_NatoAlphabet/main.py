import pandas

CSV_PATH = "/mnt/d/Git/python/026_NatoAlphabet/nato_phonetic_alphabet.csv"
# Keyword Method with iterrows()
# {index:row for (index, row) in df.iterrows()}
data = pandas.read_csv(CSV_PATH)
#TODO 1. Create a dictionary
nato_alphabet = {row.letter: row.code for (index, row) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
nato_word = [nato_alphabet[letter] for letter in word]
print(nato_word)
