import json
import random
import datetime

attempts = 0
secret = random.randint(1, 45)

with open("resources/score_list.json") as score_file:
    score_list = json.loads(score_file.read())

for score_dict in score_list:
    print(f'Best scores: {score_dict["Name"]}, {score_dict["attempts"]} attempts, date: {score_dict["date"]} '
          f'unsuccessful guesses: {score_dict.get("wrong_guesses")}')

username = input("Enter your name: ")

wrong_guesses = []
while True:
    guess = int(input('Guess the number (from 1 - 45): '))
    attempts += 1

    if secret == guess:
        print(f"Congratulations! {guess} is the secret number!")
        print(f"You needed {attempts} attempts.")

        score_list.append({"Name": username, "attempts": attempts, "date": str(datetime.datetime.now()),
                           "wrong_guesses": wrong_guesses})

        with open("resources/score_list.json", "w") as score_file:
            score_file.write(json.dumps(score_list))
        break
    elif secret > guess:
        wrong_guesses.append(guess)
        print("The secret number is bigger. Try again.")
    else:
        wrong_guesses.append(guess)
        print("The secret number is smaller. Try Again")

print('Game over')
