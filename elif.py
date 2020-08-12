# check a>b, a==b, a<b

a = input("Enter a number: ")
b = input("Enter another number: ")
number1 = int(a)
number2 = int(b)

if number1>number2:
    print("the first numebr is greater")
elif number1==number2:
    print("the numbers are equal")
else:
    print("the second number is greater")