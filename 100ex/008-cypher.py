alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(txt, shf):
	etext = ""
	for n in txt:
		x = 0
		for i in alphabet:
			if n == i:
				etext += alphabet[x + shf]
				break
			x += 1
	print(etext)		

encrypt(txt = text, shf = shift)