import random

number = input("Enter a number from 1 to 9 (including): ")
random_number = random.randint(1, 9)

lost = 0
won = 0
if number == random_number:
    won += 1
    print("Winner!")
else:
    lost += 1
    print("Better luck next time.")

valid = ["y", "n"]
char = input("Do you want to play again? (y/n): ")
while char not in valid:
    char = input("Invalid input. Do you want to play again? (y/n): ")

while char == "y":
    number = input("Enter a number from 1 to 9 (including): ")
    random_number = random.randint(1, 9)
    if number == random_number:
        won += 1
        print("Winner!")
    else:
        lost += 1
        print("Better luck next time.")
        char = input("Do you want to play again? (y/n): ")
        while char not in valid:
            char = input("Invalid input. Do you want to play again? (y/n): ")


print(f"Games won: {won}, Games lost: {lost}")