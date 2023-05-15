num = int(input("Enter a number between 1 and 100: "))

for x in range(num + 1):


    if ((x % 5 == 0) and (x % 3 == 0) and (x >= 5)):
        print("fizzbuzz")
    elif (x % 5 == 0) and (x >= 5):
        print("buzz")
    elif (x % 3 == 0) and (x >= 3):
        print("fizz")
    else:
        print(f"{x}")
