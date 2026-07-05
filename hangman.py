import random

# List of predefined words
words = ["python", "computer", "keyboard", "program", "science"]

# Select a random word
secret_word = random.choice(words)

guessed_letters = []
incorrect_guesses = 0
max_incorrect = 6

print("=" * 40)
print("🎮 Welcome to Hangman Game")
print("=" * 40)

while True:
    # Display current progress
    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)
    print("Remaining Chances:", max_incorrect - incorrect_guesses)

    # Check win condition
    if "_" not in display:
        print("\n🎉 Congratulations! You guessed the word:", secret_word)
        break

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter only one alphabet.")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess not in secret_word:
        incorrect_guesses += 1
        print("❌ Wrong Guess!")

    if incorrect_guesses >= max_incorrect:
        print("\n💀 Game Over!")
        print("The correct word was:", secret_word)
        break