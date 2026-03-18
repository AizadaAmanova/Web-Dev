# Base class
class Animal:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def eat(self):
        return f"{self.name} is eating"

    def sleep(self):
        return f"{self.name} is sleeping"

    def speak(self):
        return "Some generic sound"

    def __str__(self):
        return f"Animal(name={self.name}, age={self.age}, color={self.color})"


# Child class 1
class Dog(Animal):
    def __init__(self, name, age, color, breed):
        super().__init__(name, age, color)
        self.breed = breed

    def speak(self):
        return f"{self.name} says Woof"

    def fetch(self):
        return f"{self.name} is fetching a ball"


# Child class 2
class Cat(Animal):
    def __init__(self, name, age, color, lives_left):
        super().__init__(name, age, color)
        self.lives_left = lives_left

    def speak(self):
        return f"{self.name} says Meow"

    def scratch(self):
        return f"{self.name} is scratching furniture"