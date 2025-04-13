class Animal:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

# Dog Class (inherits from Animal)
class Dog(Animal):
    def move(self):
        return "The dog is running 🐕"

# Bird Class (inherits from Animal)
class Bird(Animal):
    def move(self):
        return "The bird is flying 🐦"

# Fish Class (inherits from Animal)
class Fish(Animal):
    def move(self):
        return "The fish is swimming 🐠"

# Creating Objects
dog = Dog()
bird = Bird()
fish = Fish()

# Demonstrating Polymorphism
animals = [dog, bird, fish]

for animal in animals:
    print(animal.move())