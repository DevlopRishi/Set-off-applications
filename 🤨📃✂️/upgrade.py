import random
import time
import os
import sys # Used for flushing output buffer

# --- Constants ---
ROCK = "Rock"
PAPER = "Paper"
SCISSORS = "Scissors"
LIZARD = "Lizard"
SPOCK = "Spock"

# --- Game Version Specific Data ---

# Classic RPS (3 choices)
CHOICES_RPS = [ROCK, PAPER, SCISSORS]
WINS_AGAINST_RPS = {
    ROCK: {SCISSORS},
    PAPER: {ROCK},
    SCISSORS: {PAPER}
}
INPUT_MAP_RPS = {
    "1": ROCK, "rock": ROCK,
    "2": PAPER, "paper": PAPER,
    "3": SCISSORS, "scissors": SCISSORS,
}
CHOICE_ART_RPS = {
    ROCK: """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    (Rock)""",
    PAPER: """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
    (Paper)""",
    SCISSORS: """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
    (Scissors)"""
}
HIGH_SCORE_FILE_RPS = "rps_highscore.txt"

# Expanded RPSLS (5 choices)
CHOICES_RPSLS = [ROCK, PAPER, SCISSORS, LIZARD, SPOCK]
WINS_AGAINST_RPSLS = {
    ROCK: {SCISSORS, LIZARD},
    PAPER: {ROCK, SPOCK},
    SCISSORS: {PAPER, LIZARD},
    LIZARD: {SPOCK, PAPER},
    SPOCK: {SCISSORS, ROCK}
}
INPUT_MAP_RPSLS = {
    "1": ROCK, "rock": ROCK,
    "2": PAPER, "paper": PAPER,
    "3": SCISSORS, "scissors": SCISSORS,
    "4": LIZARD, "lizard": LIZARD,
    "5": SPOCK, "spock": SPOCK,
}
CHOICE_ART_RPSLS = {
    ROCK: CHOICE_ART_RPS[ROCK], # Reuse from RPS
    PAPER: CHOICE_ART_RPS[PAPER], # Reuse from RPS
    SCISSORS: CHOICE_ART_RPS[SCISSORS], # Reuse from RPS
    LIZARD: """
    _______
---'   __ ~)_
      (    _)____
      (   _)_____)
      (___)____)
---.__(___)
    (Lizard)""", # Slightly different Lizard
    SPOCK: """
        ____
 __   _|__|_|_
|  | | |  | | |
|__| |_|__|_|_|
     \\____//
      |   |
      \\_//
     (Spock)""" # Slightly different Spock
}
HIGH_SCORE_FILE_RPSLS = "rpsls_highscore.txt"

# --- Helper Functions ---

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_welcome(game_name, rules, high_score):
    """Displays the welcome message, rules, and high score."""
    clear_screen()
    border = "*" * (len(game_name) + 8)
    print(border)
    print(f"*   Welcome to {game_name}!   *")
    print(border)
    print("\nRules:")
    for rule in rules:
        print(f"- {rule}")
    print("\n----------------------------------------------------")
    if high_score > 0:
        print(f"🏆 Current High Score (Most Wins in a Fair Game): {high_score} 🏆")
        print("   (High score applies only when playing fairly!)")
    print("----------------------------------------------------\n")

def get_game_version():
    """Asks user to choose between Classic RPS and Expanded RPSLS."""
    print("Choose your game version:")
    print("1. Classic (Rock, Paper, Scissors)")
    print("2. Expanded (Rock, Paper, Scissors, Lizard, Spock)")
    while True:
        choice = input("Enter choice (1 or 2): ").strip()
        if choice == '1':
            return "Classic RPS", CHOICES_RPS, WINS_AGAINST_RPS, INPUT_MAP_RPS, CHOICE_ART_RPS, HIGH_SCORE_FILE_RPS, [
                "Rock crushes Scissors",
                "Paper covers Rock",
                "Scissors cuts Paper"
            ]
        elif choice == '2':
            return "Expanded RPSLS", CHOICES_RPSLS, WINS_AGAINST_RPSLS, INPUT_MAP_RPSLS, CHOICE_ART_RPSLS, HIGH_SCORE_FILE_RPSLS, [
                "Scissors cuts Paper & decapitates Lizard",
                "Paper covers Rock & disproves Spock",
                "Rock crushes Lizard & Scissors",
                "Lizard poisons Spock & eats Paper",
                "Spock smashes Scissors & vaporizes Rock"
             ]
        else:
            print("Invalid choice. Please enter 1 or 2.")

def get_play_mode():
    """Asks the user if they are ready, subtly enabling fair mode with 'f'."""
    while True:
        # Prompt doesn't explicitly mention 'f' as fair mode
        mode = input("Ready to play? (y/f): ").lower().strip()
        if mode == 'f':
            print("\nAlright, let's begin!")
            time.sleep(0.5)
            return True # Fair mode (secretly activated)
        elif mode == 'y':
            print("\nInteresting... Let's see how this goes.")
            time.sleep(0.5)
            return False # Cheat mode (activated by the 'normal' input)
        else:
            print("Please enter 'y' or 'f'.")

def get_num_rounds():
    """Gets the desired number of rounds from the user."""
    while True:
        try:
            num_rounds = int(input("How many rounds do you want to play? "))
            if num_rounds > 0:
                return num_rounds
            else:
                print("Please enter a positive number of rounds.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def load_high_score(filename):
    """Loads the high score from the specified file."""
    if not os.path.exists(filename):
        return 0
    try:
        with open(filename, 'r') as f:
            score = int(f.read().strip())
            return score
    except (ValueError, IOError):
        print(f"Warning: Could not read high score file '{filename}'. Resetting to 0.")
        return 0

def save_high_score(filename, score):
    """Saves the high score to the specified file."""
    try:
        with open(filename, 'w') as f:
            f.write(str(score))
    except IOError:
        print(f"Warning: Could not save high score to file '{filename}'.")

def get_player_choice(choices, input_map):
    """Gets and validates the player's choice based on the current game version."""
    print("\nChoose your weapon:")
    num_options = len(choices)
    for i, choice in enumerate(choices):
        print(f"{i+1}. {choice}")

    while True:
        user_input = input(f"Enter your choice (1-{num_options} or name): ").lower().strip()
        if user_input in input_map:
            return input_map[user_input]
        else:
            print(f"Invalid choice. Please enter a number between 1 and {num_options} or a valid name.")

def get_computer_choice_fair(choices):
    """Returns a random choice for the computer from the current choice list."""
    return random.choice(choices)

def get_computer_choice_cheat(player_choice, choices, wins_against):
    """Determines the choice that beats the player's choice for the current game version."""
    possible_winning_moves = []
    for choice in choices:
        # Check if the current 'choice' beats the 'player_choice'
        if player_choice in wins_against.get(choice, set()):
             possible_winning_moves.append(choice)

    if possible_winning_moves:
        return random.choice(possible_winning_moves) # Pick one if multiple beat player

    # Fallback if somehow no winning move is found (e.g., logic error)
    # Or if player chose something invalid that slipped through (shouldn't happen)
    print("DEBUG: No cheat move found, choosing randomly.", file=sys.stderr) # For debugging
    return get_computer_choice_fair(choices)


def determine_winner(player, computer, wins_against):
    """Determines the winner based on the provided WINS_AGAINST dictionary."""
    if player == computer:
        return "tie"
    elif computer in wins_against.get(player, set()): # Use .get for safety
        return "player"
    else:
        # If not tie and player didn't win, computer must have
        # assert player in wins_against.get(computer, set()), f"Logic Error: P:{player} vs C:{computer}"
        return "computer"

def display_choices(player, computer, choice_art):
    """Displays the choices made using the appropriate ASCII art."""
    clear_screen() # Clear before showing choices for better visibility
    print("\n--- Choices Revealed ---")
    print("You Chose:")
    print(choice_art.get(player, player)) # Use .get with fallback
    time.sleep(0.8)
    print("\nComputer Chose:")
    print(choice_art.get(computer, computer)) # Use .get with fallback
    time.sleep(0.8)
    print("--------------------\n")

def update_stats(stats, winner, player, computer, choices):
    """Updates the game statistics dictionary."""
    stats["rounds_played"] += 1
    stats["player_choices"][player] = stats["player_choices"].get(player, 0) + 1
    stats["computer_choices"][computer] = stats["computer_choices"].get(computer, 0) + 1
    if winner == "player":
        stats["player_score"] += 1
    elif winner == "computer":
        stats["computer_score"] += 1
    else:
        stats["ties"] += 1

def display_round_result(winner, is_fair_mode):
    """Prints the outcome of the round, subtly hinting if cheat mode is active."""
    if winner == "player":
        print("🎉 You win this round! 🎉")
    elif winner == "computer":
        if not is_fair_mode:
             print("💥 Computer wins this round! (Too easy?) 💥") # Hint for cheat mode
        else:
             print("💥 Computer wins this round! 💥")
    else:
        print("⚖️ It's a TIE! ⚖️")

def display_final_results(stats, high_score, is_fair_mode, high_score_file, choices):
    """Displays the final scores, statistics, and high score information."""
    print("\n*****************************************")
    print("*             GAME OVER!                *")
    print("*****************************************")

    print(f"\n--- Final Score ({stats['rounds_played']} Rounds) ---")
    print(f"  You:      {stats['player_score']}")
    print(f"  Computer: {stats['computer_score']}")
    print(f"  Ties:     {stats['ties']}")
    print("-----------------------------------------")

    # --- Overall Winner ---
    player_won = stats['player_score'] > stats['computer_score']
    computer_won = stats['computer_score'] > stats['player_score']

    if player_won:
        print("🏆 Congratulations! You are the overall winner! 🏆")
        # --- High Score Logic ---
        if is_fair_mode:
            if stats['player_score'] > high_score:
                print(f"\n🎉 NEW HIGH SCORE: {stats['player_score']} wins! 🎉")
                save_high_score(high_score_file, stats['player_score'])
            else:
                 print(f"(Current High Score for this mode: {high_score})")
        else:
            print("(High score saving disabled when not playing fairly)")

    elif computer_won:
        print("💻 The Computer reigns supreme this time! 💻")
        if not is_fair_mode:
             print("   (Perhaps the odds were... tilted? 😉)")
    else:
        print("🤝 It's an overall tie! Well played! 🤝")

    # --- Statistics ---
    print("\n--- Game Statistics ---")
    print("Your Choices:")
    for choice in choices: # Iterate through the official choices for order
        count = stats["player_choices"].get(choice, 0)
        if count > 0:
             print(f"  - {choice}: {count} time(s)")
    print("Computer Choices:")
    for choice in choices:
        count = stats["computer_choices"].get(choice, 0)
        if count > 0:
             print(f"  - {choice}: {count} time(s)")
    print("-----------------------")

    print("\nThanks for playing!")
    print("*****************************************\n")


# --- Main Game Logic ---

def main():
    """Main function to run the game."""
    clear_screen()

    # 1. Choose Game Version
    game_name, choices, wins_against, input_map, choice_art, high_score_file, rules = get_game_version()

    # 2. Load High Score for selected version
    high_score = load_high_score(high_score_file)

    # 3. Display Welcome for selected version
    display_welcome(game_name, rules, high_score)

    # 4. Get Play Mode (Subtle Fair/Cheat)
    is_fair_mode = get_play_mode()

    # 5. Get Number of Rounds
    num_rounds = get_num_rounds()

    # Initialize stats based on the chosen choices
    stats = {
        "player_score": 0,
        "computer_score": 0,
        "ties": 0,
        "rounds_played": 0,
        "player_choices": {choice: 0 for choice in choices},
        "computer_choices": {choice: 0 for choice in choices}
    }

    # --- Game Loop ---
    for round_num in range(1, num_rounds + 1):
        # Don't clear screen here, display_choices will do it
        print(f"\n================ Round {round_num} of {num_rounds} ================")
        print(f"Score -> You: {stats['player_score']} | Computer: {stats['computer_score']} | Ties: {stats['ties']}")
        # Only show the cheat mode indicator if it's active
        if not is_fair_mode:
            print("😈 Computer feels confident... 😈")
        print("===================================================")
        sys.stdout.flush() # Ensure text is shown before input

        player_choice = get_player_choice(choices, input_map)

        if is_fair_mode:
            computer_choice = get_computer_choice_fair(choices)
        else:
            # In cheat mode, computer always picks the winning move
            computer_choice = get_computer_choice_cheat(player_choice, choices, wins_against)

        # Display choices clears the screen internally
        display_choices(player_choice, computer_choice, choice_art)

        winner = determine_winner(player_choice, computer_choice, wins_against)
        display_round_result(winner, is_fair_mode)
        update_stats(stats, winner, player_choice, computer_choice, choices)

        print(f"\nEnd of Round {round_num}. Score -> You: {stats['player_score']} | Computer: {stats['computer_score']}")
        print("===================================================")
        sys.stdout.flush() # Ensure text is shown before pause
        if round_num < num_rounds:
             try:
                 # Use timeout=5 for input if possible (requires platform specific libraries typically)
                 # Simple cross-platform way:
                 input("Press Enter to continue to the next round...")
             except EOFError: # Handle if input stream is closed unexpectedly
                 print("\nInput stream closed, ending game early.")
                 break

    # --- End of Game ---
    clear_screen()
    display_final_results(stats, high_score, is_fair_mode, high_score_file, choices)

# --- Run the Game ---
if __name__ == "__main__":
    main()