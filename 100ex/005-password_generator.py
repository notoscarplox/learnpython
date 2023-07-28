import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


rand = 0
letts_random = ""
for let in range(0, int(nr_letters)):
    rand = random.randint(0, len(letters) - 1)
    letts_random += letters[rand]


symb_random = ""
for sym in range(0, int(nr_symbols)):
    rand = random.randint(0, len(symbols) - 1)
    symb_random += symbols[rand]


num_rand = ""
for sym in range(0, int(nr_numbers)):
    rand = random.randint(0, len(numbers) - 1)
    num_rand += numbers[rand]


passwd = letts_random + symb_random + num_rand


randomized_passwd = ""
lenpasswd = len(passwd)
for n in range(0, lenpasswd):
    rand = random.randint(0, lenpasswd -1)
    randomized_passwd += passwd[rand]


 
print(randomized_passwd)



#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P