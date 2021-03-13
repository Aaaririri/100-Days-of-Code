def create_empty_list(word):
    lista = word.copy()
    for i in range(0, len(word)):
        lista[i] = "_"
    return lista


def replace_list(lista, word, letter):
    for i in range(0, len(word)):
        if word[i] == letter:
            lista[i] = letter
    return lista


def lifes(word, letter, number_of_trys):
    word_string = convert_to_string(word)
    if not letter in word_string:
            number_of_trys -= 1
    return number_of_trys


def convert_to_string(lista):
    lista_string = ""
    for i in range(0, len(lista)):
        lista_string += lista[i]
    return lista_string


import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["ardvark", "baboon", "camel", "lion", "phython", "toad", "scorpion", "spider", "canary", "flamingo", "penguin", "carp"]
word = list(random.choice(word_list))
empty_word = create_empty_list(word)
empty_word_string = ""
guess_list = ""
number_of_trys = 6


while number_of_trys > 0:
    letter = input("Guess a letter: ").lower()
    
    if not letter in guess_list:
        guess_list += letter
        replace_list(empty_word, word, letter)
        number_of_trys = lifes(word, letter, number_of_trys)
        empty_word_string = convert_to_string(empty_word)
        print(stages[number_of_trys])
        print(f"Used letters: {guess_list}")
        print(empty_word_string)
    else:
        number_of_trys -= 1
        print(stages[number_of_trys])
        print(empty_word_string)
        print(f"Used letters: {guess_list}")
        print("you already used that letter ")


    if empty_word == word:
        print("Congratulations You are the Winner of this challenge!!!!!!!!!!")
        break


if number_of_trys <= 0:
    print("Your man is dead, You Lose :'(")