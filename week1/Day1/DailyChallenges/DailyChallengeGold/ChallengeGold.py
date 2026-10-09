birthday = input("Enter your birthday (DD/MM/YYYY): ")
year = int(birthday[-4:])
age = str(2026 - int(birthday[-4:]))
a = 11 - int(age[-1])

if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):

    if a%2 == 0:
        b = a/2
        print(f"    {'_' * int(b)}{'i' * int(age[-1])}{'_' * int(b)}    " * 2)
    else:
        b = a//2
        print(f"    {'_' * int(b)}{'i' * int(age[-1])}{'_' * int(b + 1)}    " * 2)

    print(f"   |:H:a:p:p:y:|    " * 2)
    print(f" __|___________|__  " * 2)
    print(f"|^^^^^^^^^^^^^^^^^| " * 2)
    print(f"|:B:i:r:t:h:d:a:y:| " * 2)
    print(f"|                 | " * 2)
    print(f"~~~~~~~~~~~~~~~~~~~ " * 2)
else:
    if a%2 == 0:
        b = a/2
        print(f"    {'_' * int(b)}{'i' * int(age[-1])}{'_' * int(b)}")
    else:
        b = a//2
        print(f"    {'_' * int(b)}{'i' * int(age[-1])}{'_' * int(b + 1)}")

    print(f"   |:H:a:p:p:y:|")
    print(f" __|___________|__")
    print(f"|^^^^^^^^^^^^^^^^^|")
    print(f"|:B:i:r:t:h:d:a:y:|")
    print(f"|                 |")
    print(f"~~~~~~~~~~~~~~~~~~~")

