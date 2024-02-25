# import random
# randi = random.randint(1, 20)

# print("I'm thinking of a number between 1 and 20")
# guess = 0

# tries = 0
# while guess != randi:
#     guess = int(input("Take a guess: "))
#     if guess < randi:
#         print("Too low")
#         tries += 1
#         continue
#     else:
#         print("Too high")
#         tries += 1
#         continue
# print(f"Good job. Only took you {tries} tries")


import random
randi = random.randint(1, 20)
print("I'm thinking of a number between 1 and 20")


for i in range(1,6):
    guess = int(input("Take a guess: "))
    if guess < randi:
        print("Too low")
    elif guess > randi:
        print("Too high")
    else:
        break

if guess == randi:
    print(f"You won. only took you {i} tries")
else:
    print(f"Looser you used your {i} tries")