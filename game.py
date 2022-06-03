import random as rand
user_choice = input("Enter a choice(R, P, S): ")  # this function accepts user's choice #
possible_actions = ["R", "P", "S"] # here is a list of possible actions #
computer_choice =rand.choice(possible_actions) # this allows random possible_actions be selected
print(f"\n you chose {user_choice}, computer chose {computer_choice}.\n")

if user_choice == computer_choice:
    print(f"Both players selected {user_choice}. It's a tie!")
elif user_choice == "R":
    if computer_choice == "S":
        print("R smashes S! You win!")
    else:
         print("P covers Rock! You lose!")
elif user_choice == "P":
    if computer_choice == "R":
        print("P covers R! You win!")
    else:
        print("S cuts P! You lose.")
elif user_choice == "S":
    if computer_choice == "P":
        print("S cuts P! You win!")
    else:
        print("R smashes S! You lose.")