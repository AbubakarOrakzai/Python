# Question 01: Voting Eligibility
age = int(input("Enter your age: "))

if age >= 18:
    print("You can vote")  # Indented correctly
else:
    print("You can not vote")  # Indented correctly


## Question 02: Age Categorization

if age < 18:
    print("Child")
elif age >= 18 and age < 30:
    print("Young")
elif age >= 30 and age < 60:
    print("man")
else:
    print("old")