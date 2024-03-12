# Download Wordbank from nltk. you can create your own words list

# import nltk
# nltk.download('wordnet')

from nltk.corpus import wordnet

import random


import os

word_bank = wordnet.words()

word_bank = list(word_bank)



# print (words)

# Hangman Ascii Art


stage1='''
____..__
| .___))___|
| | / /      ||\
'''
stage2='''
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \\
| |          ||  `/,|
| |          (\\`_.'\
'''
stage3='''
| |         .-`--'.
| |        /Y . . Y\\
| |       // |   | \\\
'''
stage4='''
| |      //  | . |  \\
| |     ')   |   |   (`
| |          ||'||  
| |          || ||\\\
'''
stage5='''
| |          || ||
| |          || ||
| |         / | | \\\
'''
stage6='''
""""""""""|_`-' `-' |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :  
. .          `'       . .
'''

# Select a random word from the word bank
word = random.choice(word_bank)

# Set up the game
guesses = []
max_attempts = 6
remaining_attempts = max_attempts

# print (word)

word='islamabad'
# Clear the console screen
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


# Build the game
while remaining_attempts > 0:
    # Display the hangman ASCII art corresponding to the remaining attempts
    clear_console()
    # print(globals()["stage" + str(stage)])

    if remaining_attempts == max_attempts:
        print(stage1)
    elif remaining_attempts == max_attempts - 1:
        print(stage1+stage2)
    elif remaining_attempts == max_attempts - 2:
        print(stage1+stage2+stage3)
    elif remaining_attempts == max_attempts - 3:
        print(stage1+stage2+stage3+stage4)
    elif remaining_attempts == max_attempts - 4:
        print(stage1+stage2+stage3+stage4+stage5)
    elif remaining_attempts == max_attempts - 5:
        print(stage1+stage2+stage3+stage4+stage5+stage6)

  

    # Display the word with blanks for unguessed letters
    display_word = ''
    for letter in word:
        if letter in guesses:
            display_word += letter
        else:
            display_word += '_'
    print(display_word)

      # Display the remaining attempts
    print("Remaining attempts:", remaining_attempts)

    # Take user input for a letter guess
    guess = input("Guess a letter (enter 'quit' to exit the game '): ").lower()
    if guess == 'quit':
        print("Game over. You quit the game.")
        break
    # Check if the guess is valid (single letter and not already guessed)
    if len(guess) != 1:
        print("Invalid guess! Please enter a single letter.")
        continue
    if guess in guesses:
        print("You have already guessed that letter. Try again.")
        continue
    

    # Add the guess to the list of guesses
    guesses.append(guess)

    # Check if the guess is correct
    if guess in word:
        print("Correct guess!")
    else:
        print("Incorrect guess!")
        remaining_attempts -= 1

    # Check if the word has been fully guessed
    if all(letter in guesses for letter in word):
        print("Congratulations! You guessed the word correctly.")
        break

# Game over
if remaining_attempts == 0:
    print("You ran out of attempts. The word was:", word)
