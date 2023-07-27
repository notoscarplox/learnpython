name1 = input("Name 1: ")
name2 = input("Name 2: ")

n1 = name1.lower()
n2 = name2.lower()

n3 = n1 + n2

c = n3.count("t")
c += n3.count("r")
c += n3.count("u")
c += n3.count("e")

d = n3.count("l")
d += n3.count("o")
d += n3.count("v")
d += n3.count("e")

t = str(c) + str(d)

if int(t) < 10 or int(t) > 90:
    print(f"Score is {t}Together like me and alcohol")
elif int(t) > 40 and int(t) < 50:
    print(f"score is {t} you are ok")
else:
    print(f"Score is {t} kill yourselves")
