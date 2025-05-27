# 🎯 Number Guessing Game: Player 1 sets the number, Player 2 guesses

import os
import sys

# --- Player 1 sets the number ---
try:
    number = int(input("Player 1, enter the number to guess (1–8000000000, keep it secret!): "))
    if number < 1 or number > 800000000000:
        print("❌ Please enter a number between 1 and 100.")
        sys.exit()
except ValueError:
    print("❌ Invalid input. Please enter a valid number.")
    sys.exit()

# --- Clear the screen to hide the number ---
os.system('cls' if os.name == 'nt' else 'clear')

# --- Game setup ---
number_of_guesses = 0
max_guesses = 5

# --- Player 2 guessing loop ---
while number_of_guesses < max_guesses:
    print(f"\n🎮 Guess a number between 1 and 100. You have {max_guesses - number_of_guesses} guesses left.")
    guess_input = input("Your guess: ")

    if not guess_input.isdigit():
        print("❌ Please enter a valid whole number.")
        continue

    guess = int(guess_input)

    if guess < 1 or guess > 100:
        print("❌ Guess must be between 1 and 100.")
        continue

    number_of_guesses += 1

    if guess < number:
        print("⬇️ Too low!")
    elif guess > number:
        print("⬆️ Too high!")
    else:
        print(f"\n🎉 Congratulations! You guessed the number in {number_of_guesses} tries!")
        break
else:
    print(f"\n❌ Game over! You've used all {max_guesses} guesses. The correct number was {number}.")
