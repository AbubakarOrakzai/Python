## Tuples in python 
# A built-in data type that lets us create immutable sequences of values.
# tuple is immutabel that mean it value can not be change just let string (you can not add more element and can not modify the existing element in the tuple)

Number=tuple=(1,)
print(Number)

# tuple.index(el)   -- It will return the index of the value/element that you have enter
Number01 = tuple=(1,2,3,4,5,6)
print(tuple.index(4))  # Now here it will return the index of the 4

# tuple.count(element)   -- IT will count how many time the value/element have been repeat
Number02 = tuple=(1,2,2,2,2,2,2,34,5,6,7)
print(tuple.count(2))