"""
Basic start to criate a Hangman game.
"""
import random
word_list = ["ardvark","baboon","camel"]
word = random.choice(word_list)
letter = input("Guess a letter: ").lower()
print(f"Is the letter in the o word: {letter in word}, it apear(s) {word.count(letter)} time(s) and the word was {word}")