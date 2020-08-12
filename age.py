# find out whether the user is eligible to vote or not
age = input("What is your age?")
int_age = int(age)
if int_age>=18:
    print("Congrats! You can vote now!")
else:
    print("Sorry, you can't vote this year.")