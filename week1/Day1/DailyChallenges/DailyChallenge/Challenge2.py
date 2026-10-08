string = input("Enter a string: ")
new_string = string[0]
set = set()



for char in string:
    set.add(char)
    if char in set and char != new_string[-1]:
        new_string += char
print(f"user's word :: {string} => {new_string}")
        
        
