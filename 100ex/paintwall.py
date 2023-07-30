import math

def meters(hight, width):
    total = math.ceil((hight * width) / 5)
    print(f"You need {total} cans")

h = int(input("Enter hight: "))
w = int(input("Enter width: "))

meters(h , w)