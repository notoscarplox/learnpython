scores = input("Entrer scores ").split()
scores = [int(score) for score in scores]

high = 0
for score in scores:
    if score > high:
        high = score

print(f"highest is {high}")