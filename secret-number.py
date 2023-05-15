# Guess the secret number

secret = 19

guess = None


while guess != secret:
    guess = int(input('Guess the number: '))

    if secret == guess:
        print("Congratulations! Your guess is correct.")
    else:
        print("Too bad, this is not the secret number.")

print('Game over')