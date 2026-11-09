# ==============================================================================
# --- Four Pillars of Object-Oriented Programming (OOP) in Python
# 1- Abstraction      2- Encapsulation      3- Inheritance      4- Polymorphism
# ==============================================================================


# ------------------------------------------------------------------------------
# 1- Abstraction
# Hiding implementation details and only showing essential features to the user.
# ------------------------------------------------------------------------------
from abc import ABC, abstractmethod

class Greet(ABC):
    @abstractmethod
    def say_hello(self):
        pass  # Abstract method (must be implemented by child classes)

class English(Greet):
    def say_hello(self):
        return "Hello!"

g = English()
print("--- 1. Abstraction ---")
print(g.say_hello())
print()


# ------------------------------------------------------------------------------
# 2- Encapsulation
# Wrapping data (attributes) and functions (methods) into a single unit (class),
# restricting direct access to private data using double underscores (__).
# ------------------------------------------------------------------------------
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = BankAccount(1000)
acc.deposit(500)
print("--- 2. Encapsulation ---")
print("Account Balance:", acc.get_balance())
print()


# ------------------------------------------------------------------------------
# 3- Inheritance
# When one class (child/derived) inherits properties and methods of another class (parent/base).
# ------------------------------------------------------------------------------

# == Types of Inheritance ==
# 1- Single Inheritance       2- Multi-Level Inheritance       3- Multiple Inheritance

# --- (1) Single Inheritance (1 Parent -> 1 Child) ---
class Animal:
    def eat(self):
        print("Eating...")

class Dog(Animal):
    def bark(self):
        print("Barking...")

print("--- 3. Inheritance ---")
print("[Single Inheritance]")
dog = Dog()
dog.eat()
dog.bark()


# --- (2) Multi-Level Inheritance (Grandparent -> Parent -> Child) ---
class Puppy(Dog):
    def weep(self):
        print("Weeping...")

print("\n[Multi-Level Inheritance]")
pup = Puppy()
pup.eat()   # Inherited from Animal
pup.bark()  # Inherited from Dog
pup.weep()  # Defined in Puppy


# --- (3) Multiple Inheritance (Multiple Parents -> 1 Child) ---
class Father:
    def gardening(self):
        print("Loves gardening")

class Mother:
    def cooking(self):
        print("Loves cooking")

class Child(Father, Mother):
    def playing(self):
        print("Loves playing")

print("\n[Multiple Inheritance]")
c = Child()
c.gardening()
c.cooking()
c.playing()
print()


# ------------------------------------------------------------------------------
# --- super() Keyword in Python
# Used in a child class to call methods and constructor (__init__) of the parent class.
# Avoids code duplication and sets attributes directly on the child instance.
# ------------------------------------------------------------------------------
class Car:
    def __init__(self, brand, fuel_type):
        self.brand = brand
        self.fuel_type = fuel_type

    def start(self):
        print(f"{self.brand} car started..")

class ToyotaCar(Car):
    def __init__(self, model, fuel_type):
        # Calls parent (Car) __init__ to set brand & fuel_type
        super().__init__("Toyota", fuel_type)
        self.model = model

print("--- super() Keyword ---")
car1 = ToyotaCar("Corolla", "Petrol")
car1.start()
print("Brand:", car1.brand)      # Initialized via super()
print("Fuel:", car1.fuel_type)   # Initialized via super()
print("Model:", car1.model)      # Defined in ToyotaCar
print()


# ------------------------------------------------------------------------------
# 4- Polymorphism
# "Many forms" - Same method name behaving differently based on the object calling it.
# ------------------------------------------------------------------------------
class Circle:
    def draw(self):
        print("Drawing a Circle")

class Square:
    def draw(self):
        print("Drawing a Square")

print("--- 4. Polymorphism ---")
shapes = [Circle(), Square()]
for shape in shapes:
    shape.draw()  # Same method name, different behavior per object