class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""

        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0  # Default value for an attribute

    def get_description(self):
        """Return neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    # Method to read odometer
    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print(f"This car has {self.odometer} miles")

    # Method used to update the odometer
    def update_odometer(self, mileage):
        """Set the odometer reading to the given value"""
        if mileage < self.odometer:
            print("Can't rollback the odometer")
        else:
            self.odometer = mileage

    # Method to increment odometer
    def increment_odometer(self, miles):
        """Add miles to odometer"""
        self.odometer += miles


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery_size = 40

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")


my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_description())
my_leaf.describe_battery()

# my_car = Car("sudi", "b6", 2019)
# print(my_car.get_description())
# my_car.odometer = 23  # Modify attribute's value directly
# my_car.read_odometer()
#
#
# my_used_car = Car("bmw", "b6", 2020)
# print(my_used_car.get_description())
#
# my_used_car.update_odometer(655)  # Modify attribute's value through a method
# my_used_car.read_odometer()
#
# my_used_car.increment_odometer(100)  # Method to increment odometer
# my_used_car.read_odometer()
