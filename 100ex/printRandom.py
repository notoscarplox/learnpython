import random
randi = random.randint(1, 20)

print("I'm thinking of a number between 1 and 20")
guess = 0

tries = 0
while guess != randi:
    guess = int(input("Take a guess: "))
    if guess < randi:
        print("Too low")
        tries += 1
        continue
    else:
        print("Too high")
        tries += 1
        continue
print(f"Good job. Only {tries} times")