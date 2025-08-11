# EXERCISE 03:
nb1 = input("Choose a number: ")
nb2 = input("Choose a second number: ")

if nb1 > nb2:
	print(f"{nb1=} is greater than {nb2=}".format(nb1, nb2))
elif nb2 > nb1:
	print(f"{nb2=} is greater than {nb1=}".format(nb2, nb1))
else:
	print(f"{nb1=} is equal to {nb2=}".format(nb1, nb2))