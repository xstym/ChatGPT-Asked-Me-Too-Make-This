import random

sn = random.randint(1, 100)  
guess = None  

while guess != sn:
    guess = int(input("Guess number (between 1 and 100): "))  

    if guess < sn:
        print("Too low!")
    elif guess > sn:
        print("Too high")

print("Congratulations!")
