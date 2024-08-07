import random

digit = random.randint(1, 200)

if input("Guess \n") == digit:
    print("Correct")
else:
    print("Nope")

