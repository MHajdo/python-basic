import json
import random
import datetime


class Result:
    def __init__(self, username, attempts, date, wrong_guesses):
        self.username = username
        self.attempts = attempts
        self.date = date
        self.wrong_guesses = wrong_guesses


def play_game(level):
    attempts = 0
    secret = random.randint(1, 45)
    score_list = get_score_list()

    username = input("Enter your name: ")

    wrong_guesses = []
    while True:
        guess = int(input('Guess the number (from 1 - 45): '))
        attempts += 1

        if secret == guess:
            new_score = Result(username=username, attempts=attempts, date=str(datetime.datetime.now()),
                               wrong_guesses=wrong_guesses)

            score_list.append(new_score.__dict__)

            with open("resources/score_list.json", "w") as score_file:
                score_file.write(json.dumps(score_list))

            print(f"Congratulations! {guess} is the secret number!")
            print(f"You needed {attempts} attempts.")
            break
        elif secret > guess and level == "easy":
            wrong_guesses.append(guess)
            print("The secret number is bigger. Try again.")
        elif secret < guess and level == "easy":
            wrong_guesses.append(guess)
            print("The secret number is smaller. Try Again")
        elif secret != guess and level == "hard":
            wrong_guesses.append(guess)
            print(f"{guess} is not the secret number. Try Again.")


def get_score_list():
    try:
        with open("resources/score_list.json") as score_file:
            score_list = json.loads(score_file.read())
    except (FileNotFoundError, json.JSONDecodeError):
        score_list = []

    return score_list


def get_top_score():
    score_list = get_score_list()
    score_list.sort(key=lambda d: d['attempts'])

    for score_dict in score_list[:3]:
        new_score = Result(username=score_dict.get("username"), attempts=score_dict.get("attempts"),
                           date=score_dict.get("date"), wrong_guesses=score_dict.get("wrong_guesses"))

        print(f"Name: {new_score.username}, attempts: {new_score.attempts}, date: {new_score.date},"
              f" wrong guesses: {new_score.wrong_guesses}")


while True:
    selection = input("Would you like to: \nA) play a new game, \nB) see the best scores, \nC) quit?")

    if selection.upper() == "A":
        mode = input("Which mode would you like to choose?\nA) Easy\nB) Hard")
        if mode.upper() == "A":
            play_game(level="easy")
        else:
            play_game(level="hard")
    elif selection.upper() == "B":
        get_top_score()
    else:
        print('Game over')
        break
