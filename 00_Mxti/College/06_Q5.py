'''Problem 5: Single Inheritance and super()

Task:
Create a base class Vehicle with an __init__ method that takes a brand and a year and stores them. Add a method display_info() that prints the brand and year.
Create a derived class Car that inherits from Vehicle.
The Car class __init__ method should take brand, year, and model as parameters. Use super().__init__(brand, year) to call the parent class constructor, and then store the model as an instance variable.
Override the display_info() method in the Car class to also print the model along with the brand and year.
Add a new method drive() in the Car class that prints a message like "The [brand] [model] is driving."
Create a Car object and call its display_info() and drive() methods.
'''
class Vehicle:
    def __init__(self,brand,year):
        self.brand = brand
        self.year = year
    def display_info(self,):
        print(f"Brand Name: {self.brand}\nYear: {self.year}")
class Car(Vehicle):
    def __init__(self,brand, year, model):
        x = super().__init__(brand, year)
        self.model = model
    def display_info(self,):
        super().display_info()
        print(f"model: {self.model}")
    def drive(self):
        print(f"{self.brand} {self.model} is driving")
car_obj = Car("Toyota",2023,"charmy")
car_obj.display_info()
car_obj.drive()