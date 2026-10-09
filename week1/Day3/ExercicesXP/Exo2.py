family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

#How much does each family member have to pay ?
for name, age in family.items():
    if age < 3:
        print(f"{name} has to pay 0$")
    elif age >= 3 and age <= 12:
        print(f"{name} has to pay 10$")
    else:
        print(f"{name} has to pay 15$")

#Print out the family’s total cost for the movies.
total_cost = 0
for age in family.values():
    if age < 3:
        total_cost += 0
    elif age >= 3 and age <= 12:
        total_cost += 10
    else:
        total_cost += 15

print(f"The total cost for the family is {total_cost}$")

#Bonus
family = {}
member_count = int(input("Enter the number of family members: "))
for i in range(member_count):
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    family[name] = age

#How much does each family member have to pay ?
for name, age in family.items():
    if age < 3:
        print(f"{name} has to pay 0$")
    elif age >= 3 and age <= 12:
        print(f"{name} has to pay 10$")
    else:
        print(f"{name} has to pay 15$")

#Print out the family’s total cost for the movies.
total_cost = 0
for age in family.values():
    if age < 3:
        total_cost += 0
    elif age >= 3 and age <= 12:
        total_cost += 10
    else:
        total_cost += 15

print(f"The total cost for the family is {total_cost}$")