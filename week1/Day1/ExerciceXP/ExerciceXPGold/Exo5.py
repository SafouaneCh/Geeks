num1 = input("Input the 1st number: ")
num2 = input("Input the 2nd number: ")
num3 = input("Input the 3rd number: ")

list = [num1, num2, num3]
list.sort()

print(f"the greatest number is: {list[-1]}")