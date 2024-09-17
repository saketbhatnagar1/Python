
class Animal:
def __init__(self, name):
self.name = name
def speak(self):
raise NotImplementedError("Subclasses must implement this
method")
def __str__(self):
return f"Animal: {self.name}"
def __repr__(self):
return f"Animal(name={self.name!r})"
# Define a derived class inheriting from Animal
class Dog(Animal):
def __init__(self, name, breed):
super().__init__(name) # Call the base class constructor
self.breed = breed
def speak(self):
return f"{self.name} says Woof!"
def __str__(self):
return f"Dog: {self.name}, Breed: {self.breed}"
def __repr__(self):
return f"Dog(name={self.name!r}, breed={self.breed!r})"
def __add__(self, other):
if isinstance(other, Dog):
return f"Combining breeds: {self.breed} and {other.breed}"
return NotImplemented
# Define another derived class
class Cat(Animal):
def __init__(self, name, color):
super().__init__(name)
self.color = color
def speak(self):
return f"{self.name} says Meow!"
def __str__(self):
return f"Cat: {self.name}, Color: {self.color}"
def __repr__(self):
return f"Cat(name={self.name!r}, color={self.color!r})"
def __lt__(self, other):
if isinstance(other, Cat):
return self.name < other.name
return NotImplemented
# Demonstrate usage of classes and methods
def main():
# Create instances
dog1 = Dog("Rex", "Labrador")
dog2 = Dog("Buddy", "Beagle")
cat1 = Cat("Whiskers", "White")
# Print object details using __str__ and __repr__
print(dog1) # Output: Dog: Rex, Breed: Labrador
print(repr(dog1)) # Output: Dog(name='Rex', breed='Labrador')
print(cat1) # Output: Cat: Whiskers, Color: White
print(repr(cat1)) # Output: Cat(name='Whiskers', color='White')
# Call methods
print(dog1.speak()) # Output: Rex says Woof!
print(cat1.speak()) # Output: Whiskers says Meow!
# Demonstrate inheritance and method overriding
print(dog1.speak()) # Output: Rex says Woof!
print(cat1.speak()) # Output: Whiskers says Meow!
# Demonstrate polymorphism
animals = [dog1, dog2, cat1]
for animal in animals:
print(animal.speak())
# Demonstrate special methods
print(dog1 + dog2) # Output: Combining breeds: Labrador and
Beagle
# Comparison using special methods
print(cat1 < Cat("Tom", "Gray")) # Output: True
# Encapsulation
dog1.name = "Max" # Modifying name directly
print(dog1) # Output: Dog: Max, Breed: Labrador
if __name__ == "__main__":
main(
