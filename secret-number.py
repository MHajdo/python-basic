import json
import random
import datetime


def get_score_list():
    with open("resources/score_list.json") as score_file:
        score_list = json.loads(score_file.read())
        return score_list


def play_game(level):
    attempts = 0
    secret = random.randint(1, 45)
    score_list = get_score_list()

    username = input("Enter your name: ")

    wrong_guesses = []
    if level == "hard":
        while True:
            guess = int(input('Guess the number (from 1 - 45): '))
            attempts += 1

            if secret == guess:
                print(f"Congratulations! {guess} is the secret number!")
                print(f"You needed {attempts} attempts.")

                score_list.append({"name": username, "attempts": attempts, "date": str(datetime.datetime.now()),
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
    elif level == "easy":
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
                print(f"{guess} is not the secret number. Try again.")
            else:
                wrong_guesses.append(guess)
                print(f"{guess} is not the secret number. Try again.")


def get_top_score():
    score_list = get_score_list()
    score_list.sort(key=lambda d: d['attempts'])

    for score_dict in score_list[:3]:
        print(f'Best scores: {score_dict["Name"]}, {score_dict["attempts"]} attempts, date: {score_dict["date"]} '
              f'unsuccessful guesses: {score_dict.get("wrong_guesses")}')


while True:
    selection = input("Would you like to: \nA) play a new game, \nB) see the best scores, \nC) quit?")

    if selection.upper() == "A":
        level = input("Which mode would you like to choose?\nA) Easy\nB) Hard")
        if level.upper() == "A":
            play_game(level="hard")
        else:
            play_game(level="easy")
    elif selection.upper() == "B":
        get_top_score()
    else:
        print('Game over')
        break
