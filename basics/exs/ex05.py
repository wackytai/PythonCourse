# EXERCISE 1:
""" nb = input("Enter an integer: ")
i = None

try:
	i = int(nb)
except:
	print(f"{nb=} is NOT an integer.".format(nb))
	exit(1)

if i % 2:
	print(f"{i} is an odd number.")
else:
	print(f"{i} is an even number.") """

# EXERCISE 2:
""" HOUR = input("Enter the current hour unit in your timezone: ")
i = None

try:
	i = int(HOUR)
except:
	print(f"'{HOUR}' is not a integer.")
	exit(1)
if i < 0 or i > 24:
	exit(print(f"'{i}' is not in 0-24 range."))
if i < 12:
	print("Good morning")
elif i < 18:
	print("Good afternoon")
else:
	print("Good night") """

# EXERCISE 3:
name = input("Enter your First Name: ")
i = 0

while (i < len(name)):
	try:
		if not name[i].isalpha():
			exit("You didn't enter a valid name.")
	except:
		exit("You didn't enter a valid name.")
	i += 1

if len(name) < 5:
	print("Your name is very short.")
elif len(name) < 7:
	print("Your name is on a normal range.")
else:
	print("Your name is very long.")