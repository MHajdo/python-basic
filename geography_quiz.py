import json
import random

with open("resources/countries.json") as countries_file:
    countries_cities = json.loads(countries_file.read())

country, capital = random.choice(list(countries_cities.items()))

while True:
    answer = input(f"What is the capital city of {country}? ")

    if answer.upper() == capital.upper():
        print(f"Correct! {capital} is the capital city of {country}.")
        break
    elif answer != capital:
        print(f"Wrong. {answer} is not the capital city of {country}. Try again.")
