## Dicrionary in Python 
# Dictionaries are used to store data value in key:value pairs
# They are unordered, mutable(changeable) and do not allow duplicate keys

dic = {
    "name": "Abubakar Orakzai",
     "Rollnumber" : "s2024266007",
     "Degree":"BSCS"
}

print(dic)

## Nested Dic

student = {
    "name":"Ahmed",
    "Subject":{
        "Physic":97,
        "ICT":98,
        "PF":96,
    }
}

print(student["Subject"]["Physic"])


## Dictionary Methods
# myDict.keys() -- return all keys

print(student.keys()) 
print(list(student.keys()))   # We can also convert the dictornary into list

print(len(student)) # find the lenght 

## myDict.values()   --  return all values
print(student.values())

## myDict.get(key)
## -- now here we can also say that why are we not using the Student[key] instead of hte student.get[key]
## -- the answer to that is during enter the key if we write the spelling wrong or enter the key that does not
## -- so without the method it will give error but with the get method it will return none if the key is not present in the dictionary

print("Below are the key and value through the get")
print(student.get("name"))