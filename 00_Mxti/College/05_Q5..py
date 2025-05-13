''' Problem 4: Class and Instance Variables, Basic Methods

Task:
Define a class called Dog.
Include a class variable species and set its value to "Canis familiaris".
Include an __init__ method that takes name and age as parameters and sets them as instance variables (self.name, self.age).
Add a method bark() that prints f"{self.name} says Woof!".
Add a method description() that returns a string describing the dog, e.g., f"{self.name} is {self.age} years old.".
Create two Dog objects with different names and ages.
Print the species using the class name and using one of the object names. Call the bark() and description() methods for both objects.
Briefly explain the difference in how you access class vs. instance variables and how their values differ across instances.
'''
class Dog:
    species = "Canis familiaris"
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def bark(self):
        print(f"{self.name} says Woof!")
    def description(self):
        return f"{self.name} is {self.age} year old."
obj = Dog("Jocky",5)
obj1 = Dog("Emly",9)
print("species name (with object): ",obj.species)
print("species name (with Class): ",Dog.species)
print("\nCalling methon with object 1")
obj.bark()
print(obj.description())
print("\nCalling methon with object 2\n")
obj1.bark()
print(obj1.description())
