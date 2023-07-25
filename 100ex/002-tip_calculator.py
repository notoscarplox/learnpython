#!/usr/bin/python3

bill = float(input("total bill "))
tip = int(input('how much tipo? 10% 20% 30% '))
people = int(input('how many people? '))
billtip = bill + (bill * (tip / 100))
pay = round(billtip / people, 2)
print(f'you have to pay {pay}')
