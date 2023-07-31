
participants = {}


def add_part(name, money):
    participants[name] = money


rerun = "yes"
while rerun != "no":
    nom = input("Name: ")
    price = int(input("Price"))
    rerun = input("Add new participant? Yes or No")
    add_part(nom, price)

# print(participants.items())
for per, mon in participants.items():
    print(f"{per}: {mon}")
