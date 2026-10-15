class Dog():
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        jump_height = self.height * 2
        print(f"{self.name} jumps {jump_height} cm high!")

davids_dog = Dog("Rex", 50)
print(f"{davids_dog.name} is {davids_dog.height} cm tall.")
davids_dog.bark()
davids_dog.jump()

sarahs_dog = Dog("Teacup", 20)
print(f"{sarahs_dog.name} is {sarahs_dog.height} cm tall.")
sarahs_dog.bark()  
sarahs_dog.jump()

if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} is bigger than {sarahs_dog.name}.")
elif davids_dog.height < sarahs_dog.height:
    print(f"{sarahs_dog.name} is bigger than {davids_dog.name}.")
else:
    print(f"{davids_dog.name} and {sarahs_dog.name} are the same height.")