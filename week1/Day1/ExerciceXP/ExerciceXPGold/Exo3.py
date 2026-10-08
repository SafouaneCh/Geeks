user_name = input("what is your name? : ")
my_name = "Safouane"

while user_name.upper() != my_name.upper():
    user_name = input("what is your name? : ")
print(f"Hello {user_name}!")