import random

secret_number = random.randint(1, 10)

guess = int(input("enter guess number: "))
if guess == secret_number:
    print("you win ✅")
else:
    print("you lose ❌")