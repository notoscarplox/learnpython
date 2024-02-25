import random

list = []
strikeh = 0
striket = 0
totstrikeh = 0
totstriket = 0
a = None

for i in range(10000):
	res = random.randint(0,1)
	list.append(res)

for i in list:
	if list[i] == 1:
		strikeh += 1
	else:
		strikeh = 0
	if strikeh == 6:
		totstrikeh += 1
		strikeh = 0

print(f"total {totstrikeh}")