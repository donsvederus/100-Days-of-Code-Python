import random

# ASCII art for rock, paper, scissors
rock = """
    Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    Paper
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# List of choices
choices = ["rock", "paper", "scissors"]
ascii_art = {"rock": rock, "paper": paper, "scissors": scissors}

# Mapping numbers to choices
number_to_choice = {1: "rock", 2: "paper", 3: "scissors"}

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    while True:
        try:
            user_choice = int(input("Enter 1 for rock, 2 for paper, or 3 for scissors: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if user_choice not in [1, 2, 3]:
            print("Invalid choice. Please try again.")
            continue

        user_choice_str = number_to_choice[user_choice]
        computer_choice = random.choice(choices)
        print(f"\nYou chose:\n{ascii_art[user_choice_str]}")
        print(f"Computer chose:\n{ascii_art[computer_choice]}")

        result = determine_winner(user_choice_str, computer_choice)
        print(result)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again not in ["yes", "y"]:
            break

if __name__ == "__main__":
    play_game()