"""Write a function that takes a list value as an argument and returns
a string with all the items separated by a comma and a space, with and
inserted before the last item. """

spam = ['apples', 'bananas', 'tofu', 'cats', 1]


def listand(lis):

	printo = ""

	if not lis:
		return 'no items'
	else:
		for index, i in enumerate(lis):
			if index < len(lis) - 2:
				printo = printo + str(i) + ", "
			elif index < len(lis) - 1:
				printo = printo + str(i)
			else:
				printo = printo + " and " + str(i)
	return printo


print(listand(spam))