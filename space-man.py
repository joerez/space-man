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

def show_space_man():
    global tries_left
    global space_man
    if tries_left == 7:
        print(space_man)
    elif tries_left == 6:
        space_man = """
        .-'''-.
       /= ___  l
      |- /~~~\  |
      |=( '.' ) |
      \__\_=_/__/
      """
        print(space_man)
    elif tries_left == 5:
        space_man = """

        .-'''-.
       /= ___  l
      |- /~~~\  |
      |=( '.' ) |
      \__\_=_/__/
       {_______}
       *       `
      .      [] .
      | ooo     |
       \_______/

        """
        print(space_man)
    elif tries_left == 4:
        space_man == """

        .-'''-.
       /= ___  l
      |- /~~~\  |
      |=( '.' ) |
      \__\_=_/__/
       {_______}
     l` *       `
    l= .     [] .
   l  /|ooo     |
  (   )\_______/
   l``l
    `-

        """
        print(space_man)


    else:
        print(space_man)



def print_game():
    show_space_man()

    print("\n")
    print("tries left:")
    print(tries_left)


    print("\n")
    print(encrypted_word)
    print(the_secret_word)
    print("\n")
    print("Previously guessed letters:")
    print(previously_used_letters)

# Select a random word from the list and set it equal to the secret word.
list_length = len(list_of_words)

the_secret_word = list_of_words[randint(0, list_length) - 1]



# encrypt word
# this function looks for all letters a through z in the_secret_word, and replaces them with underscores.
the_secret_word = the_secret_word.replace("", " ")


encrypted_word = re.sub('[a-z]', '_', the_secret_word)



# Space man game
def space_man():
    global tries_left
    global encrypted_word
    while (tries_left > 0):
        print_game()
        if '_' in encrypted_word:
            letter_guess = input("\nGuess a letter: ")
            if letter_guess not in previously_used_letters:
                previously_used_letters.append(letter_guess)

                if letter_guess in the_secret_word:
                    print("letter found")
                    # check which index(es) in secret word, it belongs to
                    correct_letter_indices = []
                    for i, character in enumerate(the_secret_word):
                        if the_secret_word[i] == letter_guess:
                            correct_letter_indices.append(i)

                    # change the index(es) in the encrypted word to have the letter(s)
                    encrypted_word_list = list(encrypted_word)
                    for index in correct_letter_indices:
                        encrypted_word_list[index] = letter_guess
                    encrypted_word = "".join(encrypted_word_list)


                else:
                    print("letter not found")
                    tries_left = tries_left - 1

            else:
                print("you already guessed that letter!")
        else:
            print("you win")
            break
    if (tries_left == 0):
        print('you lose')
        print(the_secret_word)


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
