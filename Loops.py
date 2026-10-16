## Loops in Python 

# range( 10,               101 ,           10)
#        starting value   Ending Value  iteration


## Printing table of 5 

for i in range(1, 11):
    print(f"5 * {i} = {i * 5}")

# Printing string through loops

a = "students"

for i in a:
    print(i);


## Break and continue in loops

# break
for i in range(1,11):
   if i == 4:
       break                # Now this will print 1, 2 ,3 but when it check i == 4 the conditiion will become true and it will stop and not print 4 
   print(i)

# Continue 
for i in range(1, 12):
    if i == 4:
        continue            # As the condition become true it will not print 4 and continue printing after 4 
    print(i)

## While Loop

a = 1 
while a ! = 20:
print(a)
a = a + 1