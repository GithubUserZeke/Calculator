# This is a guessing game.

import random

lower_bound = 1
print("Enter lower bound 1.")
upper_bound = 100
print("Enter Upper bound 100.")

number_to_guess = random.randrange(100)

print("You have 7 chances to guess the number between 1 and 100.")

for i in range(1, 8):
    print(i)
    guess = int(input("What is your guess: "))
    if guess > number_to_guess:
        print("Lower")
    elif guess < number_to_guess:
        print("Higher")
    elif guess == number_to_guess:
        print("You WIN!")
        break
    if i == 7:
        print("You LOSE!", number_to_guess)
        break