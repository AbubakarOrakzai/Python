# --- Four Pilor of the Python 
# 1- Abstraction        2- Encapsulation     3-Inheritance     4-polymorphism

# 1- Abstraction 
# Hiding the implementation details of a class and only showing the essential feature to the user

from abc import ABC, abstractmethod

class Greet(ABC):
    @abstractmethod
    def say_hello(self):
        pass  # Abstract method

class English(Greet):
    def say_hello(self):
        return "Hello!"

g = English()
print(g.say_hello())

# 2- Encapsulation 
# Wrapping data and functions into a single unit(object)