import random

com = random.randint(1, 100)
tries = 0 

while True:
    tries = tries + 1
    hum = int(input("Guess your number between 1 - 100 :- "))

    if hum == com:
        print(f"Congratulations you have won! It took you {tries} tries.")
        break
    elif hum > com:
        print("Sorry wrong guess, go lower!")
    elif hum < com:
        print("Sorry wrong guess, go higher!")