"""
================================================================================
TASK 1: HANGMAN GAME
================================================================================
A text-based Hangman game with multiple difficulty levels and visual ASCII art.
================================================================================
"""

import random

def get_hangman_display(incorrect_guesses, max_incorrect):
    """Display hangman ASCII art based on incorrect guesses"""
    stages = [
        """
           +---+
           |   |
               |
               |
               |
               |
         =========
        """,
        """
           +---+
           |   |
           O   |
               |
               |
               |
         =========
        """,
        """
           +---+
           |   |
           O   |
           |   |
               |
               |
         =========
        """,
        """
           +---+
           |   |
           O   |
          /|   |
               |
               |
         =========
        """,
        """
           +---+
           |   |
           O   |
          /|\\  |
               |
               |
         =========
        """,
        """
           +---+
           |   |
           O   |
          /|\\  |
          /    |
               |
         =========
        """,
        """
           +---+
           |   |
           O   |
          /|\\  |
          / \\  |
               |
         =========
        """
    ]
    return stages[min(incorrect_guesses, max_incorrect)]

def play_hangman():
    """Enhanced text-based Hangman game with difficulty levels"""
    # Expanded word list with categories
    word_bank = {
        "easy": ["python", "hangman", "computer", "keyboard", "mouse", "screen", "laptop"],
        "medium": ["programming", "developer", "algorithm", "function", "variable", "dictionary"],
        "hard": ["encapsulation", "polymorphism", "inheritance", "abstraction", "recursion", "optimization"]
    }
    
    print("=" * 60)
    print("Welcome to HANGMAN!")
    print("=" * 60)
    print("\nSelect difficulty level:")
    print("1. Easy (4-7 letters)")
    print("2. Medium (8-11 letters)")
    print("3. Hard (12+ letters)")
    
    while True:
        try:
            choice = input("\nEnter choice (1-3): ").strip()
            if choice == "1":
                words = word_bank["easy"]
                max_incorrect = 7
                break
            elif choice == "2":
                words = word_bank["medium"]
                max_incorrect = 6
                break
            elif choice == "3":
                words = word_bank["hard"]
                max_incorrect = 8
                break
            else:
                print("❌ Please enter 1, 2, or 3!")
        except KeyboardInterrupt:
            print("\n\nGame cancelled. Goodbye!")
            return
    
    secret_word = random.choice(words)
    guessed_letters = []
    incorrect_guesses = 0
    
    print("\n" + "=" * 60)
    print(f"Word length: {len(secret_word)} letters")
    print(f"Max incorrect guesses allowed: {max_incorrect}")
    print("=" * 60)
    
    while incorrect_guesses < max_incorrect:
        # Display hangman
        print(get_hangman_display(incorrect_guesses, max_incorrect))
        
        # Display current word state
        word_display = " ".join([letter if letter in guessed_letters else "_" for letter in secret_word])
        
        print(f"\nWord: {word_display}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        print(f"Incorrect guesses: {incorrect_guesses}/{max_incorrect}")
        
        # Get player input
        try:
            guess = input("\nGuess a letter (or 'quit' to exit): ").lower().strip()
        except KeyboardInterrupt:
            print("\n\nGame cancelled. Goodbye!")
            return
        
        if guess == "quit":
            print("\nThanks for playing! Goodbye!")
            return
        
        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter a single letter!")
            continue
        
        if guess in guessed_letters:
            print("⚠️  You already guessed that letter!")
            continue
        
        guessed_letters.append(guess)
        
        # Check if guess is correct
        if guess in secret_word:
            count = secret_word.count(guess)
            print(f"✅ Good guess! '{guess}' appears {count} time(s) in the word!")
        else:
            print(f"❌ Sorry! '{guess}' is not in the word.")
            incorrect_guesses += 1
        
        # Check if player won
        if all(letter in guessed_letters for letter in secret_word):
            print("\n" + "=" * 60)
            print(f"🎉 Congratulations! You won! The word was: {secret_word.upper()}")
            print("=" * 60)
            return
        
        print()
    
    # Player lost
    print(get_hangman_display(incorrect_guesses, max_incorrect))
    print("\n" + "=" * 60)
    print(f"💀 Game Over! The word was: {secret_word.upper()}")
    print("=" * 60)

def main():
    """Main game loop"""
    play_hangman()
    
    # Ask to play again
    while True:
        try:
            again = input("\nDo you want to play again? (yes/no): ").lower().strip()
            if again in ["yes", "y"]:
                play_hangman()
            elif again in ["no", "n"]:
                print("Thanks for playing! Goodbye!")
                break
            else:
                print("Please enter 'yes' or 'no'")
        except KeyboardInterrupt:
            print("\n\nThanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
