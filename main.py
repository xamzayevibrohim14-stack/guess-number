import random

secret_number = random.randint(1, 10)

while True:
    guess = int(input("enter guess number: "))
    if guess == secret_number:
        print("you win ✅")
        break
    else:
        print("you lose ❌")