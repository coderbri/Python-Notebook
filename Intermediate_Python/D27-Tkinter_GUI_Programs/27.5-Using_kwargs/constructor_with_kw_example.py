class Car:
    # The __init__ method is the constructor for the Car class.
    # It takes '**kw' (short for keyword arguments) which will be a dictionary
    # containing any named arguments passed during object creation.
    def __init__(self, **kw):
        # We can initialize object attributes from the 'kw' dictionary.
        # This approach is flexible, allowing us to pass 'make' and 'model'
        # as keyword arguments when creating a Car object.
        self.make = kw["make"]
        self.model = kw["model"]

# When creating 'my_car', we don't explicitly see 'make' or 'model'
# as parameters in the __init__ signature, but '**kw' captures them.
my_car = Car(make="Nissan", model="GT-8")
print(f"My car model: {my_car.model}") # Output: My car model: GT-8

# Handling Missing Keyword Arguments with .get()
# If you try to access a key from the 'kw' dictionary that wasn't provided,
# it will cause a KeyError, making the program crash.
# For example, if we create a car without a 'model':
# my_car_incomplete = Car(make="Honda")
# print(my_car_incomplete.model) # This would raise a KeyError because 'model' is not in 'kw'.

# To prevent a KeyError when a keyword argument might be optional,
# you can use the dictionary's .get() method.
# .get() returns the value for a given key if it exists.
# If the key does not exist, it returns 'None' by default (or a specified default value).
class CarSafe:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model") # If 'model' is not provided, self.model will be None.

my_car_safe = CarSafe(make="Nissan")
print(f"My safe car model (without model provided): {my_car_safe.model}") # Output: My safe car model (without model provided): None

# You can also provide a custom default value with .get()
class CarWithDefault:
    def __init__(self, **kw):
        self.make = kw.get("make", "Unknown Make") # If 'make' is not provided, defaults to "Unknown Make"
        self.model = kw.get("model", "Unknown Model") # If 'model' is not provided, defaults to "Unknown Model"

my_car_default = CarWithDefault(make="Toyota")
print(f"Car with default model: Make: {my_car_default.make}, Model: {my_car_default.model}") # Output: Car with default model: Make: Toyota, Model: Unknown Model

my_car_full_default = CarWithDefault()
print(f"Car with all defaults: Make: {my_car_full_default.make}, Model: {my_car_full_default.model}") # Output: Car with all defaults: Make: Unknown Make, Model: Unknown Model
