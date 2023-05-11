# Calculator

num1 = int(input('Input the first number: '))
num2 = int(input('Input the second number: '))
operation = input('Input the desired arithmetic operation ("+", "-", "*" or "/"): ')

if operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "*":
    print(num1 * num2)
elif operation == "/":
    print(num1 / num2)
else:
    print('Invalid operator')
