# list in python 
# A built-in data type that store set of value 
# It can store elements of different types (integer,float, string,etc).

# List
marks = [94.4, 87.5, 95.2, 66.4, 45.1]
print(marks)
print(type(marks))

print(f"Marks at the index 0 is {marks[0]} and at the index 1 it is {marks[1]} and so on ")

# We can also add value of the different datatype in the List           # * string is ----> immutable 
student = ["Ahmed",100,"Umt"]                                            # * List is ------> mutable (that mean you can change the value of it)

# Now change the value in the List to further demonstrate the Mutable character of the List 
Ahmed = ["Ahmed khan",22658,"Computer Science"]
Ahmed[1] = 26660;
print(Ahmed)

# SubList
marks1 = [95, 93, 90,91]
updatedmarks = (marks1[0:2])      # List slicing
print(updatedmarks)
print(marks1[1:3])