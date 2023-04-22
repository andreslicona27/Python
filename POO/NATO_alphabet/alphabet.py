import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dictionary = {row.letter: row.code for (index, row) in data.iterrows()}


def generate_phonetics():
    word = input("enter a word: ").upper()
    try:
        output_list = [phonetic_dictionary[letter] for letter in word]
    except KeyError:
        print("Only letters in the alphabet please")
        generate_phonetics()
    else:
        print(output_list)


generate_phonetics()
