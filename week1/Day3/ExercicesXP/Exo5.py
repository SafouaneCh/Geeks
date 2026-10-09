import random

def function(num):
    if num >= 1 and num <= 100:
        num1 = random.randint(1, num)
    if num1 == num:
        return "You win!"
    else :
        return f"You lose! your number was {num}. The winning number was {num1}."

print(function(50))