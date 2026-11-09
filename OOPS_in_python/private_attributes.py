# Del keyword 

class Student:
    name="Abubakar Orakzai"

    def __init__(self,uni_name):
        self.uni_name=uni_name

s1=Student("UMT");
print(s1.uni_name)
del s1 # This will delete the object s1 and you can also delete the indiv attribute of the object 

## -- public 

class Account:
    def __init__(self,account_number,account_password):
        self.account_number=account_number
        self.account_password=account_password

acc1=Account("23454","abucdss")
print(acc1.account_number,acc1.account_password) #  As you will be seeing that this will be access the data outside the class which is not good practice beacuse as we allow the access to the outside the chance of the changes increases

# Inorder to make the attribute private we will use the two underscore (__)

class Account02:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass  # by puting the __ infront of the varaible now this become the private varaible  

acc2=Account02("5362","jlfkasd")
print(acc2.acc_no)
print(acc2.__acc_pass)  # now the account password will not be printing because it is private attribute
