# class method
# A class method is bound to the class and receives the class as an implicit first argument.
# Note static method can not access or modify class state and generally for utility

# static method is not created for the every object. it is created only once

class car:

    def __init__(self,type):
        self.type=type

        @staticmethod
        def start():
            print("Car started")


car001=car("sport-car")
print(car001.type)

## problem 

class Person:
    name="anonymous"

    def changeName(self,name):
        self.name=name

P1=Person()
P1.changeName("rahul Kumar")
print(P1.name)
print(Person.name)


# In the above code the problem that we face is that we want to change the name of the anonymous to rahul kummar 
# But it is creating a new name in that object instead of changing the anonymous 

# If we want to change the anonymous directly 

def changeName(self,name):
      Person.name=name    

# Now change will be reflect to in the real attribute

# Another way of doing this is self.__class__.name="Rahul"

## We can also use decortator for doing the same work 

@classmethod    # class decorator
def changeName(cls,name):     #  The cls is refer to the class and it will also make th direct change in the class attribute
    cls.name=name

# class method 
# (1) static methods     - Does not accept any arugument   - it can not make the direct change in the class attributes
# (2) cllass methods     - cls (argumment)  - Use when you want to making the direct changin 
# (3) instance methods  - use self(argument) - Use when you want to making the changing in the instance/obbject