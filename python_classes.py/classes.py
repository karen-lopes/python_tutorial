class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

my_dog = Dog('Willie', 6)

print(f"My dog's name is {my_dog.name}")
print(f"My dog is {my_dog.age} years old.")

my_dog.name

my_dog.sit()
my_dog.roll_over()

class Restaurant:
    """Restaurant description"""
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.name} is a restaurant and its cuisine type is {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"{self.name} is open!")

favorite_restaurant = Restaurant('Lamen_acu', 'japanese')

favorite_restaurant.name
favorite_restaurant.cuisine_type

favorite_restaurant.describe_restaurant()
favorite_restaurant.open_restaurant()


class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialie attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")




my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.read_odometer()

#Modifying an attribute's value directly
my_new_car.odormeter_reading = 23

my_new_car.read_odometer()

#Modifying an attribute's value through a method
class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialie attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

my_new_car.update_odometer(23)
my_new_car.read_odometer()

#Incrementing an atributte's value through a method
class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialie attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

my_used_car = Car('subaru', 'outback', 2015)
my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()
