import os
import random
import Hangman_arts 
from Hangman_words import words

chosen_word = random.choice(words)
lives = 6
end_of_game = False
print(Hangman_arts.logo)
display = [] # * Create blanks
for _ in chosen_word:
    display += "_"

    
while not end_of_game:
    guess = input("Guess the letter: ").lower()
    os.system('cls') # *  clear the console, remember to import os 
    if guess in display:
      print(f"You have al ready guessed {guess}")

    # * Checks if the letter is in the word 
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # * Checks if user is wrong     
    if guess not in chosen_word:
        print(f"You guessed {guess}, thats not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lose")

    print(f"{''.join(display)}")

    # * Checks if the display is complete 
    if "_" not in display:
        end_of_game = True
        print("You Win")

    print(Hangman_arts.stages[lives]) # * print the hangman 