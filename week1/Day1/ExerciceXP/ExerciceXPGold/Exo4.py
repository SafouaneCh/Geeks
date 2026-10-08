names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
print(names)

user_name = input("what is your name? : ")

for name in names:
    if name == user_name:
        print(names.index(name))
        break