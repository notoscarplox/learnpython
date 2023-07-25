tdays = 365 * 90
tweeks = 52 * 90
tmonths = 12 * 90
age = int(input('enter age '))
daysleft = tdays - (365 * age)
weeksleft = tweeks - (52 * age)
monthsleft = tmonths - (12 * age)
print(f'you have {daysleft} days left, {weeksleft} weeks left and {monthsleft} months left')
