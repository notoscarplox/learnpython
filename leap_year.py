#Check if a year is a leap year

year = int(input("Enter the year to check: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap")
        else:
            print("not leap")
    else:
        print("leap")
else:
    print("not leap")