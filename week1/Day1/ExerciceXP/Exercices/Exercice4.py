height = input("Enter your height in cm: ")

if height.isdigit():
    height = int(height)
    if height >= 145:
        print("you are tall enough to ride")
    else:
        print("You are not tall enough to ride, you need to grow a bit more.")
else:
    print("Please enter a valid number for height.") 