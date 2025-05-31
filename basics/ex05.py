nb = input("Enter an integer: ")
i = None

try:
	i = int(nb)
except:
	print(f"{nb=} is NOT an integer.".format(nb))
	exit(1)

if i % 2:
	print(f"{i} is an odd number.")
else:
	print(f"{i} is an even number.")

