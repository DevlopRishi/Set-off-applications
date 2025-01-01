import random

def fun_game():
    print("Welcome to Rock, Paper, Scissors!")
    print("Choose one of the following:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    
    # List of choices
    choices = ["Rock", "Paper", "Scissors"]
    
    # Take user's choice
    user_choice = input("Enter your choice (1-3): ")
    
    if user_choice not in ['1', '2', '3']:
        print("That's not a valid choice! Please choose a number between 1 and 3.")
        return
    
    user_choice = int(user_choice) - 1  # Convert to index
    
    print(f"You chose: {choices[user_choice]}")

#Ayee, Don't peek here

    totally_not_cheat_choice = (user_choice + 1) % 3
    print(f"Computer chose: {choices[totally_not_cheat_choice]}")
    
    print("Oh no, you lost! The computer is too clever for you!")

# Run the game
fun_game()