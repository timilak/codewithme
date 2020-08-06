# upper and lower
mystring = "Hello there! Is there anyone here? There is no one here."
upper_string = mystring.upper()
lower_string = mystring.lower()
# print(lower_string)

# len function
# print(len(mystring))

# count method
count_here = lower_string.count("here", 5, 21)
#print(count_here)

# find method
find_string = mystring.rfind("here")
#print(find_string)

# replace
replaced = mystring.replace("e", "a", 3)
#print(replaced)

# split
split_string = mystring.split()
#print(split_string)

fruits = ["Apple", "Cherry", "Orange"]

# join
separator = " "
joined_string = separator.join(fruits)
print(joined_string)