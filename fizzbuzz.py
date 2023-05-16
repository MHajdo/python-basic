num = int(input("Enter a number between 1 and 100: "))

for x in range(1, num + 1):

    if x % 5 == 0 and x % 3 == 0:
        print("fizzbuzz")
    elif x % 5 == 0:
        print("buzz")
    elif x % 3 == 0:
        print("fizz")
    else:
        print(f"{x}")
