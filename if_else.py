# using if... else statement with logical operators: and, or, not
string1 = "Hello"
string2 = "hello"
a = 13
b = 16

# not: reverses the conditon(true or false)
if not string1==string2:
    print("This statement is false")
else:
    print("This statement is true")

# and: Both statements need to be true
if string1==string2 and a>b:
    print("Both statements are true")
else:
    print("Both statements are not true")

# or: At least one statement needs to be true
if string1==string2 or a>b:
    print("One or more statements are true")
else:
    print("Both statements are false")