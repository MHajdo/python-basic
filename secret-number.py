# Guess the secret number
import random

secret = random.randint(1, 45)

while True:
    guess = int(input('Guess the number (from 1 - 45): '))

    if secret == guess:
        print(f"Congratulations! {guess} is the secret number!")
        break
    elif secret > guess:
        print("The secret number is bigger. Try again.")
    else:
        print("The secret number is smaller. Try Again")

print('Game over')
