name = "Khalid Khan"
age = 19
print(name,age)

ratio = 2/4;
pi = 3.14;
equation = 1+ 2j;

# DataType 

print(type(age)) # This will print the Dataype of the age   -- integer
print(type(name)) # This will print the Datatype of the name   -- string

print(type(ratio)) # Datatype -- Decimal 
print(type(pi))  # Datatype -- Decmail

print(type(equation)) # Datatype -- Complex  


# String 

print(ord('A'))   # This will print the ord unique number 
print(ord('B'))   # This will print the ord unique nunber

Department = "Computer Science";
print(Department[2]);

print(Department[-3]);

print(Department[7:16:1])

# type converstion 

a = "12";
a = int(a);

b="20";

print(type(a));
print(a);


# you can convert srting into integer if it hold valid integer.
# you can conver float value to integer 

a = "12.4"
a = float(a)

print(type(a))


# Converting values into boolean 

a = 12
b= 0
c = 12.4 
d = 0.0
e = ""
f = "hello"
print(bool(a))
print(bool(b))
print(bool(c))
print(bool(d))
print(bool(e))
print(bool(f))

# How does this happen
"""
so there is set of values on which the python return false and on the remaining value it is giving true
1- false
2- 0
3- 0.0
4- ""
5- []
6- ()
7- {}
"""
