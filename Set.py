 ## Set in pyton 
# Set is the collection of the unordered items
# Each element in set must be unique and immutable 

# We can store boolen, int , float , str , tuple in the set but 
# We can not store list and dictionary in the set beacuse it is immutable vlaue 
# set also ignore the duplicate value

collection = {1,2,2 , "Hello","world","world",4}
print(collection)
print(type(collection))
print(len(collection))  #len will colculate teh total number of items and it will ignore the duplicated value

# Set is imutable(you can add and remove value from the set but you can not modify the exist value in the set) but the element in the set is mutable 

# Set Methods

#-- set.add(element)  -- Adds an element

collection.add(1)
collection.add(2)
print(collection)

# -- set.remove(element) -- removes the element

collection.remove(2) 
print(collection)
# --  set.clear() -- empties the set
# -- set.pop() #removes a random value
