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
# (2) class methods     - cls (argumment)  - Use when you want to making the direct changin 
# (3) instance methods  - use self(argument) - Use when you want to making the changing in the instance/obbject

## Property 
# We use @property decorator on any method in the class to use the method as a property

class Student:
    def __init__(self,phy,chem,math):
         self.phy=phy
         self.chem=chem
         self.math=math
         self.percentage=str((self.phy+self.chem+self.mmath)/3)+"%"

st01=Student(98,99,499)
print(st01.percentage)

# When attribute value depend on the function then it is called function property
# The problem that we are facing before using the @property method when we change the valule of the attribute 
# The percentage value does not change 

class Student02:
    def __inti__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math

# The other way to deal with it to use the function but the must convent is to use the @property method