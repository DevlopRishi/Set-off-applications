import random

WORDS = ["python", "linux", "cli", "game", "developer", "github", "programming", "terminal"]

# Main game logic
def play_game():
    word = random.choice(WORDS)  # Randomly pick a word
    guessed_word = ["_"] * len(word)  # Hidden word display
    attempts = 10  # Number of incorrect guesses allowed
    guessed_letters = set()  # Track guessed letters

    print("\nWelcome to Word Guess Game!")
    print("Guess the word, one letter at a time.")
    print(f"The word has {len(word)} letters.")
    print("You have 6 attempts. Good luck!")

    while attempts > 0 and "_" in guessed_word:
        print("\nWord: " + " ".join(guessed_word))
        print(f"Attempts left: {attempts}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
        
        guess = input("Enter a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetic character.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter!")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            attempts -= 1

    if "_" not in guessed_word:
        print("\n🎉 Congratulations! You've guessed the word:", word)
    else:
        print("\n😞 You're out of attempts. The word was:", word)

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again in ["yes", "y"]:
        play_game()
    else:
        print("Thanks for playing! Goodbye!")

if __name__ == "__main__":
    play_game()