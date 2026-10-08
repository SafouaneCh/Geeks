3 <= 3 < 9
# the output : True

3 == 3 == 3
# the output : True

bool(0)
# the output : False

bool(5 == "5")
# the output : False

bool(4 == 4) == bool("4" == "4")
# the output : True

bool(bool(None))
# the output : False

x = (1 == True)
y = (1 == False)
a = True + 4
b = False + 10

print("x is", x)
# the output : True

print("y is", y)
# the output : False

print("a:", a)
# the output : 5

print("b:", b)
# the output : 10