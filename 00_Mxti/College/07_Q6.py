'''Problem 6: Illustrating Polymorphism (Duck Typing)
Task:
Define two different classes, Duck and Person.
Both classes should have a method named speak(). The Duck class's speak() method should print "Quack", and the Person class's speak() method should print "Hello".
Write a function make_it_speak(obj) that takes an object obj as input and calls obj.speak().
Create an instance of Duck and an instance of Person.
Call the make_it_speak() function with both the Duck object and the Person object as arguments.
Observe and explain how the same function call (obj.speak()) results in different behavior based on the object's type.
'''
class Duck:
    def speak(self):
        print("Quack")
class Person:
    def speak(self):
        print("Hello")
def make_it_speak(obj):
    obj.speak()
duck_obj = Duck()
person_obj = Person()
make_it_speak(duck_obj)
make_it_speak(person_obj)
