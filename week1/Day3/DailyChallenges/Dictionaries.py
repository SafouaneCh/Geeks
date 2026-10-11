# Ask a user for a word
word = input("Please enter a word: ")

# Write a program that creates a dictionary. This dictionary stores the indexes of each letter in a list.
dictonary = {}
for index, letter in enumerate(word):
    if letter not in dictonary:
        dictonary[letter] = []
    dictonary[letter].append(index)
print(dictonary)
