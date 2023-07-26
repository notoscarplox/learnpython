import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

no_names = len(names)

payer = random.randint(0, no_names - 1)

print(f"The payer is {names[payer]}")