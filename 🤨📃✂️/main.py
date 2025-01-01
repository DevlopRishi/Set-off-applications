import random

def fun_game():
    print("Welcome to Rock, Paper, Scissors, Lizard, Spock!")
    print("Choose one of the following:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Lizard")
    print("5. Spock")
    
    # List of choices
    choices = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
    
    # Take user's choice
    user_choice = input("Enter your choice (1-5): ")
    
    if user_choice not in ['1', '2', '3', '4', '5']:
        print("That's not a valid choice! Please choose a number between 1 and 5.")
        return
    
    user_choice = int(user_choice) - 1  # Convert to index
    
    print(f"You chose: {choices[user_choice]}")
    
    # Get computer's choice
    computer_choice = random.randint(0, 4)
    print(f"Computer chose: {choices[computer_choice]}")
    
    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie! Try again.")
    elif (user_choice == 0 and (computer_choice == 2 or computer_choice == 3)) or \
         (user_choice == 1 and (computer_choice == 0 or computer_choice == 4)) or \
         (user_choice == 2 and (computer_choice == 1 or computer_choice == 3)) or \
         (user_choice == 3 and (computer_choice == 1 or computer_choice == 4)) or \
         (user_choice == 4 and (computer_choice == 0 or computer_choice == 2)):
        print("You win! You outsmarted the computer!")
    else:
        print("Oh no, you lost! The computer is too clever for you!")

# Run the game
fun_game()