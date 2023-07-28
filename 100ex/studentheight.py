
student_heights = input("Entrer heights ").split()

print(f"students {student_heights}")

student_heights = [int(heights) for heights in student_heights]

n = 0
suma = 0
for heights in student_heights:
    suma += heights
    n += 1

print(f"sum is {suma} and no. of heights is {n}")
print(f"Avarage is {round(suma/n)}")