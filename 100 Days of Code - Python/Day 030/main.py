import pandas

data = pandas.read_csv("Day 030/nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

list_check = False
while not list_check:
    try:
        word = input("Enter a word: ").upper()
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry only letters in the alphabet please")
    else:
        list_check = True
        print(output_list)
