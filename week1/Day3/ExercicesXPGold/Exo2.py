birthdays = {"Alice": "1990-01-01", "Bob": "1985-05-12", "Charlie": "1992-07-23", "David": "1988-11-30", "Eve": "1995-03-15"}

print("Welcome to the birthday dictionary!")
print("We have birthdays for: ", list(birthdays.keys()))
print("You can look up the birthdays of the people in the list!")

name = input("Please enter a name from the list: ")
if name in birthdays.keys():
    print(f"{name}'s birthday is on {birthdays[name]}.")
else:
    print(f"Sorry, we don’t have the birthday information for {name}.")