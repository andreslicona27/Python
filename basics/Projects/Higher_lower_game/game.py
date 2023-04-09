import os
import random
import art
from data import data

print(art.logo)

# * PROPERTIES 
account_a = {}
account_b = {}
score = 0
guess = ""
game_should_continue = True

# * FUNCTIONS
def account_data(account):
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}"

def check_answer(guess, a_follower_count, b_follower_count):
    if a_follower_count > b_follower_count:
        return guess == "a" # if guess equals a it would return true if not it would be false
    else:
        return guess == "b"

# * MAIN CODE
account_b = random.choice(data)
while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {account_data(account_a)}")
    print(art.vs)
    print(f"Compare B: {account_data(account_b)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    
    os.system("cls")
    print(art.logo)

    if is_correct:
        score += 1
        print(f"You are right. Current score {score}")
    else :
        game_should_continue = False
        print(f"You are wrong. Final score {score}")