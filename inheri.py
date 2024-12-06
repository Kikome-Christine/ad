# Base class: Animal
class Animal:
    def __init__(self, name):
        self.name = name  # Attribute to store the name of the animal

    def speak(self):
        return "I am an animal."

# Derived class: Dog
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call the constructor of the base class
        self.breed = breed  # Additional attribute for Dog

    def speak(self):
        return f"{self.name} says Woof!"

# Example usage
my_dog = Dog("Buddy", "Golden Retriever")
print(my_dog.speak())  # Output: Buddy says Woof!
print(f"My dog's breed is: {my_dog.breed}")  # Output: My dog's breed is: Golden Retriever