import json
import random


def play_game():
    country = get_country()
    capital = get_capital(country)

    while True:
        answer = input(f"What is the capital city of {country}? ")

        if answer.upper() == capital.upper():
            print(f"Correct! {capital} is the capital city of {country}.")
            break
        else:
            print(f"Wrong. {answer} is not the capital city of {country}. Try again.")


def get_country():
    with open("resources/countries.json") as countries_file:
        countries_cities = json.loads(countries_file.read())

        country = random.choice(list(countries_cities))

        return country


def get_capital(country):
    with open("resources/countries.json") as countries_file:
        countries_cities = json.loads(countries_file.read())

        capital = countries_cities.get(country)

        return capital


while True:
    selection = input("Would you like to?\nA) Play a new game,\nB) Quit? ")

    if selection.upper() == "A":
        play_game()
    else:
        print("Game over")
        break
