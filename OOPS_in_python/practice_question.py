# Create student class that take name and marks of 3 subject as arguments in constructor
# then create a method to print the average

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks  # We will pass a list of marks here

    # New method to calculate and print the average
    def print_average(self):
        total = sum(self.marks)
        average = total / len(self.marks)
        print(f"Name: {self.name} | Average Marks: {average}")

# Create the object and pass a list of 3 subject marks
s1 = Student("Ali", [98, 90, 85])

# Call the method
s1.print_average()

#Question 02

class Account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account_no0=acc

        def debit(self,amount):
            self.balance -= amount
            print("Rs.",amount,"was debited")
            print("total",self.get_balance())

        def credit(self,amount):
            self.balance+=amount
            print("Rs",amount,"was credited")
            print("total balance",self.get_balance())

        def get_balance(self):
            return self.balance
        

acc1=Account(1000,123456)
print(acc1.balance)
print(acc1.account_no)
