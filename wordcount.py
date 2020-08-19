# ask the user for a file name and read it

file = open("wordcounttext.txt", "r")
contents = file.read()

# split the string into many small strings (words)
words = contents.split()
counter = 0

# for loop --> for i in list: counter
# print the word count

for word in words:
    counter+=1

print("The word count is: ")
print(counter)