# Number Guesser - Simple beginners projects from Tech With Tim on yt
# https://youtu.be/DLn3jOsNRVE

import random  # import the module at the top

user_wins = 0
computer_wins = 0
draw = 0
game_list = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to Quoit: ").lower()
    if user_input == "q":
        break

    # check the user_input if it's equal for more than thing
    if user_input not in game_list:  # if it's not in the list
        continue  # this command will re-ask user to type proper

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = game_list[random_number]
    print(f"Computer picked {computer_pick}.")

    if user_input == "rock" and computer_pick == "scissors":
        # "or" will do the opposite to "and"
        print("You won!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1

    elif user_input == computer_pick:
        print("Draw!")
        draw += 1

    else:
        print("You lost!")
        computer_wins += 1
        continue

print(f"You won {user_wins} time.")
print(f"Computer won {computer_wins} times.")
print(f"The number of draws: {draw}.")
print("Goodbye!")
