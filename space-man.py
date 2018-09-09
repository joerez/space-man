# imports
import math
from random import randint
import re

# Import a list of words.
text_file = open("./words.txt")
word_file = text_file.readlines()

list_of_words = []

for words in word_file:
    a = words.replace("\n", "")
    list_of_words.append(a)

# Declare default stuff

tries_left = 7
previously_used_letters = []
space_man = ""
encrypted_word = ""

def print_game():
    print("\n")
    print("tries left:")
    print(tries_left)
    print("\n")
    print(space_man)
    print("\n")
    print(encrypted_word)
    print("\n")
    print("Previously guessed letters:")
    print(previously_used_letters)

# Select a random word from the list and set it equal to the secret word.
list_length = len(list_of_words)

the_secret_word = list_of_words[randint(0, list_length) - 1]

# encrypt word
# this function looks for all letters a through z in the_secret_word, and replaces them with underscores.

encrypted_word = re.sub('[a-z]', '_ ', the_secret_word)

# Space man game
def space_man():
    while (tries_left > 0):
        print_game()
        letter_guess = input("\nGuess a letter: ")
        if letter_guess not in previously_used_letters:
            previously_used_letters.append(word_guess)

            if letter_guess in the_secret_word:
                print("letter found")
            else:
                print("letter not found")
                tries_left - 1






        else:
            print("you already guessed that letter!")



space_man()




"""
 Collect user input in the form of a letter from A-Z. Save this letter to an array called Used Letters. Compare this input to the used letters array so users don’t select the same letter twice.

 Check users input with each space of the secret word.

 If the letter matches, then replace the index with that letter. Then keep going till the end            of the secret word.

 If the letter does not match, add a part of the space man.

 Output to the console a diagram of some sort that shows the used characters, the secret word with the correctly guessed letters filled in, and the spaceman himself. Maybe also display tries leftover out of 7.

 If seven tries go by, it’s game over and space man launches into space.

 If a user wins, then they win.
"""
