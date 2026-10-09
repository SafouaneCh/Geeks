# 1. Create the function with size and text parameters
def make_shirt(size, text):
    print(f"The size of the shirt is {size} and the text is '{text}'.")


# 2. Call the function
make_shirt("Medium", "Hello World")


# 3. Modify the function with default values
def make_shirt(size="Large", text="I love Python"):
    print(f"The size of the shirt is {size} and the text is '{text}'.")


# 4. Make a large shirt with the default message
make_shirt()

# 5. Make a medium shirt with the default message
make_shirt("Medium")

# 6. Make a shirt of any size with a different message
make_shirt("Small", "Coding is fun!")

#Bonus
make_shirt(size="Large", text="I love Python")