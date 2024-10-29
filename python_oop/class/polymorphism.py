class Animal:
    def skeak(self):
        pass

class Dog(Animal):
    def skeak(self):
        return "Bark"

class Cat(Animal):
    def skeak(self):
        return "Meow"

def mak_sound(animal):
    print(animal.skeak())

dog = Dog()
cat = Cat()

mak_sound(dog)
mak_sound(cat)

