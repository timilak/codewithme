#welcome message and input for numbers

print("Welcome to the calculator!")

number1 = input("Enter the first number: ")
number2 = input("Enter the second number: ")

# convert input numbers to int or float
int_number1 = int(number1)
int_number2 = int(number2)

# ask for operator
operator = input("Enter an operator (+, -, *, /, %, **): ")

# if statements to print calculation depending on output + error message
if operator == "+":
    print("The sum is: ")
    print(int_number1 + int_number2)
elif operator == "-":
    print("The difference is: ")
    print(int_number1 - int_number2)
elif operator == "*":
    print("The multiplication is: ")
    print(int_number1 * int_number2)
elif operator == "/":
    print("The quotient from division is: ")
    print(int_number1 / int_number2)
elif operator == "%":
    print("The remainder from division is: ")
    print(int_number1 % int_number2)
elif operator == "**":
    print("The exponent is: ")
    print(int_number1 ** int_number2)
else:
    print("There was an error. Please enter your operator again in the correct format")

print("Thank you for using the calculator!")