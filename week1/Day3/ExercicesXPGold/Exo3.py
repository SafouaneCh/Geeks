def sum(number):
    X = int(str(number))
    XX = int(str(number) * 2)
    XXX = int(str(number) * 3)
    XXXX = int(str(number) * 4)
    total = X+XX+XXX+XXXX
    return f"{total} ({X} + {XX} + {XXX} + {XXXX})"

print(sum(3))