# Guess the secret number

secret = 19

guess = int(input('Guess the number: '))

if secret == guess:
    print("Congratulations! Your guess is correct.")
else:
    print("Too bad, " + str(guess) + " is not the secret number.")
