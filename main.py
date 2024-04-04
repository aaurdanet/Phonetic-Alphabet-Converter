import pandas

# Create a dictionary from csv

nato = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for index, row in nato.iterrows()}

# Create a list of the phonetic code words from a word that the user inputs.
input_word = input("Enter a word: ").upper()
char_list = [char for char in input_word]

output = [nato_dict[key] if key in nato_dict else None for key in char_list]

print(output)
