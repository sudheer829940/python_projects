import random

def get_computer_choice():
    """Randomly return rock, paper or scissors for the computer."""
    options = ["rock", "paper", "scissors"]
    return random.choice(options)

def decide_winner(user, computer):
    """Decide the winner of the game based on rules."""
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") \
         or (user == "scissors" and computer == "paper") \
         or (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

def play_game():
    user_score = 0
    computer_score = 0

    print("Welcome to Rock-Paper-Scissors Game!")
    print("Type 'rock', 'paper', or 'scissors' to play. Type 'exit' to quit.\n")

    while True:
        user_choice = input("Your move (rock/paper/scissors): ").strip().lower()

        if user_choice == "exit":
            print("\nGame Over. Final Score → You:", user_score, "| Computer:", computer_score)
            break

        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice, please try again.\n")
            continue

        computer_choice = get_computer_choice()
        print("Computer chose:", computer_choice)

        result = decide_winner(user_choice, computer_choice)

        if result == "tie":
            print("It's a tie!\n")
        elif result == "user":
            print("You win this round!\n")
            user_score += 1
        else:
            print("Computer wins this round!\n")
            computer_score += 1

        print("Current Score → You:", user_score, "| Computer:", computer_score, "\n")

# Run the game
if __name__ == "__main__":
    play_game()
