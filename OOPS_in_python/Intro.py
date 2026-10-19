# OOP in python 
# To map with real world scenarios we started using objects in code 
# This is called object oriented programming


# Classes in pyhton 
#- class is a blueprint for creating objects 

#- Creating class
class student:
    name="Khalid Khan"

    # Default Constructor
    def __init__(self):    # The self parameter is a reference to the current instance(object) of the class and is used to access variable that belong to the class self 
         print("Adding new student in database..")

# Creating object instance 
s1 = student()
print(s1.name)

## __init__ Function
# Constructor  -- Object creation
# All Classes have a function called _int_(), Which is always executed when the object is being initiated 

# Parameterized Constructor
# let suppose we want to store the name of every student different using the constructor def __int__

class student01:
     def __init__(self,fullname):
          self.name=fullname
          print("New student name added")

S2=student01("Haseeb Khan")
print(S2.name)