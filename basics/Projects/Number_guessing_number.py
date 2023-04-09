import random 
import os

logo = """
██████  ██    ██ ███████ ███████ ███████     ████████ ██   ██ ███████     ███    ██ ██    ██ ███    ███ ██████  ███████ ██████  
██       ██    ██ ██      ██      ██             ██    ██   ██ ██          ████   ██ ██    ██ ████  ████ ██   ██ ██      ██   ██ 
██   ███ ██    ██ █████   ███████ ███████        ██    ███████ █████       ██ ██  ██ ██    ██ ██ ████ ██ ██████  █████   ██████  
██    ██ ██    ██ ██           ██      ██        ██    ██   ██ ██          ██  ██ ██ ██    ██ ██  ██  ██ ██   ██ ██      ██   ██ 
 ██████   ██████  ███████ ███████ ███████        ██    ██   ██ ███████     ██   ████  ██████  ██      ██ ██████  ███████ ██   ██ 
                                                                                                                                 
"""

# * PROPERTIES
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
turns = 0

# * FUNCTIONS
def check_answer(guess, answer, turns):
    if guess > answer:
        print("To high")
        return turns - 1
    elif guess < answer:
        print("To low")
        return turns - 1
    else:
        print("You got it! The answer was {answer}")

def choose_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    print(logo)
    print("Guess the number between 1 and 100")
    answer = random.randint(1,100)
    turns = choose_difficulty()

    guess = 0
    while guess != answer:    
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)

        print(f"You have {turns} attempts remaining to guess the number")
        if turns == 0:
            print("You have run out of guesses, you lose")
            return
        elif guess != answer:
            print("Guess again")

# * MAIN CODE 
game()