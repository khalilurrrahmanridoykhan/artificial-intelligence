class AllThinks:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class Human(AllThinks):
    def __init__(self, name, age, height, weight):
        super().__init__(name, age)
        self.height = height
        self.weight = weight

    def display(self):
        return f"Name: {self.name}, Age: {self.age}, Height: {self.height}, Weight: {self.weight}"

class Animal(AllThinks):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def display(self):
        return f"Name: {self.name}, Age: {self.age}, Color: {self.color}"

human = Human("Rahul", 25, 5.8, 65)
animal = Animal("Dog", 5, "Black")

print(human.display())
print(animal.display())