import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [rock, paper, scissors]

while True:
    computer_choice = options[random.randint(0, 2)]
    player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors or 4 to escape\n"))

    if player_choice == 4:
        break
    
    print("computer choice : ", computer_choice)

    player_choice = options[player_choice]

    print("player choice : ", player_choice)

    if (
        (player_choice == rock and computer_choice == scissors) or
        (player_choice == scissors and computer_choice == paper) or
        (player_choice == paper and computer_choice == rock)
    ):
        print("Player wins!")

    elif (
        (computer_choice == rock and player_choice == scissors) or
        (computer_choice == scissors and player_choice == paper) or
        (computer_choice == paper and player_choice == rock)
    ):
        print("Computer wins!")

    elif computer_choice == player_choice:
        print("Draw!")

