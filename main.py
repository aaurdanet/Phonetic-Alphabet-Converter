import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for index, row in data.iterrows()}


def generate_nato_dict():
    input_word = input("Enter a word: ").upper()
    try:
        output = [nato_dict[letter] for letter in input_word]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_nato_dict()
    else:
        print(output)


generate_nato_dict()
