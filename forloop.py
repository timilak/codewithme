# this is a for loop using a string and list

string = "Cherry"
fruits = ["Apple", "Banana", "Cherry", "Orange", "Watermelon", "Strawberry"]
count = 0

for letter in string:
  if letter=="r":
    count += 1

# count even numbers between 1 to 100

counter = 0
for number in range(1, 100):
  if number%2==0:
    counter += 1
print(counter)