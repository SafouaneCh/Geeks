class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

# 1. Instantiate three Cat objects
cat1 = Cat("Mino", 3)
cat2 = Cat("shime", 5)
cat3 = Cat("Shadow", 2)


# 2. Determine the oldest cat
def oldest_cat(list = [cat1, cat2, cat3]):
    oldest = max(list, key=lambda cat: cat.age)
    return f"The oldest cat is {oldest.name}, and is {oldest.age} years old."

print(oldest_cat())
