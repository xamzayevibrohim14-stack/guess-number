import random

secret_number = random.randint(1, 10)

count = 0
while count < 3:
    guess = int(input("enter guess number: "))
    if guess == secret_number:
        print("you win ✅")
        break
    else:
        print(f"you lose ❌>> {count}")
    count += 1