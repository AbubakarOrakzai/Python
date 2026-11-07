#                     ----Attribute in Python-----
# -- Class Attributes
# Class attributes is when write a same name for all the object 
# like if you want to university name and all the student with the univesity share 
# the same university name 

# Instance Attributes 
# Instance Attributes is when you have different name for the same varaible 
# like all the student in the college have different name we use the self attributes

#   When we use both in the code the Instance Attributes get priority over the class attributes


class Student:
    college_name="ABC College"  #Class Attributes

    def __init__(self,name,marks):
        self.name=name #object attributes
        self.marks=marks
        print("adding new student in the database")


s1=Student("Ahmed",95)
# print(s1.name,s1.marks)

# -- Methods in the python 

class Dep:
    Dep_name="Computer Science"

    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def welcome(self):
        print("Welcome student",self.name, "marks is ",self.marks)

s2=Dep("Cs",99.99)
print(s2.name,s2.marks)

# ---------------

# Static Method
# Methods that do not use the self parameter (work at class level)

class Student:
    @staticmethod #Decorator 
    def college():
        print("Abc college")