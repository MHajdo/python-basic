# Guess the secret number
import random

attempts = 0
secret = random.randint(1, 45)

with open("resources/score.txt") as score_file:
    best_score = int(score_file.read())
    print(f"Best score: {best_score}")

while True:
    guess = int(input('Guess the number (from 1 - 45): '))
    attempts += 1

    if secret == guess:
        print(f"Congratulations! {guess} is the secret number!")
        print(f"You needed {attempts} attempts.")
        if attempts < best_score:
            with open("resources/score.txt", "w") as score_file:
                score_file.write(f"{attempts}")
        break
    elif secret > guess:
        print("The secret number is bigger. Try again.")
    else:
        print("The secret number is smaller. Try Again")

print('Game over')
