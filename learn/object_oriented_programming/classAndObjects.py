# Define a class
class Person:
    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method Definition
    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

#Object Creation and Method Invocation
person = Person("Alice", 30)
person.introduce()
