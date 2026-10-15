class Zoo():

    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        print(f"The animals in {self.zoo_name} are: {', '.join(self.animals)}")

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        sorted_animals = sorted(self.animals)
        animal_dict = {}
        for animal in sorted_animals:
            first_letter = animal[0]
            if first_letter not in animal_dict:
                animal_dict[first_letter] = []
            animal_dict[first_letter].append(animal)
        return animal_dict

    def get_groups(self):
        animal_dict = self.sort_animals()
        for letter, animals in animal_dict.items():
            print(f"Group {letter}: {', '.join(animals)}")


# 1. Instantiate the zoo (already done in your code)
new_york_zoo = Zoo("New York Zoo")

# 2. Add animals (including duplicate checks)
new_york_zoo.add_animal("Ape")
new_york_zoo.add_animal("Baboon")
new_york_zoo.add_animal("Bear")
new_york_zoo.add_animal("Cat")
new_york_zoo.add_animal("Cougar")
new_york_zoo.add_animal("Emu")
new_york_zoo.add_animal("Ape")  # Won't be added twice

# 3. Print all animals in the zoo
new_york_zoo.get_animals()

# 4. Sell an animal
new_york_zoo.sell_animal("Emu")

# 5. Print animals again to confirm "Emu" was removed
new_york_zoo.get_animals()

# 6. Test sort_animals() directly (returns a dictionary)
grouped_dict = new_york_zoo.sort_animals()
print("Dictionary output:", grouped_dict)

# 7. Test get_groups() (prints formatted groups)
new_york_zoo.get_groups()