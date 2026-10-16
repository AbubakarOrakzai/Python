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

## List Methods

 # list.append -- Adds one element at the end of the list
rollnumber = [2,1,3]
rollnumber.append(10)
print(rollnumber)

# list.sort -- Arragne the list in ascending order
rollnumber.sort()
print(rollnumber)

rollnumber.sort(reverse=True)
print(rollnumber)

# list.reverse -- The will reverse the original list 
rollnumber.reverse()
print(rollnumber)

# list.insert(index,element) -- This is use to insert value/element at the specific location first write the index where you want to insert the value/element then write the value/element that you want to insert 
rollnumber.insert(1,100)
print(rollnumber)

# list.remove(index)   -- remove the value/element at the specific index that you mention 
rollnumber.remove(3)
print(rollnumber)

# list.pop()   --- delete the last value/element of the listy
rollnumber.pop()
print(f"Using pop i will remove the last value/element {rollnumber}")


## Pratice Question 01
# Take favourite 3 movie name form the use and store it in the list
movieslist=[]
for i in range(0,3):
     movies=input("Enter your favourite movie name")
     movieslist.append(movies)
     print(movieslist)

##  Pratice Quesiton 02
# Check is the list is palindrome or not

Number03 = [1,2,1]
cpNumber03 = Number03.copy()

cpNumber03.reverse()

if Number03 == cpNumber03:
  print("The list is Palindrome")
else:
  print("The number is not Palindrome")

# Now check the list which is not palindrome
Number04 = [1,2,3]
cpNumber04 = Number04.copy()

cpNumber04.reverse()

if Number04 == cpNumber04:
  print("The list is Palindrome")
else:
  print("The number is not Palindrome")