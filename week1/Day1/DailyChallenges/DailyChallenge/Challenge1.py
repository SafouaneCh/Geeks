number = input("Enter a number: ")
length = input("Enter the length of the list: ")
result = []

for i in range(1,int(length) + 1):
    result.append(int(number) * i)
print(f"number: {number} - length: {length} => {result}")