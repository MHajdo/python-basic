
print("Hello, this program converts kilometers into miles.")

while True:
    km = float(input("Enter the number of kilometers: "))

    print(f"{km} kilometers is {km * 0.621371192} miles.")

    answer = input("Do you want to do another conversion? ")

    if answer == "Yes" or answer == "yes" or answer == "YES":
        print("Ok!")
    else:
        print("Goodbye!")
        break





