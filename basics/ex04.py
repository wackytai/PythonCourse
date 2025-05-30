name = input("Name: ")
age = input("Age: ")
isSpacedName = False

if not name or not age:
	print("Sorry, you left at least one field empty")
else:
	if ' ' in name:
		isSpacedName = True
	print(f"Your name is {name}")
	print("Your inverted name is", name[::-1]) # f"Your inverted name is {name[::-1]}"
	print("Does your name have spaces?", isSpacedName)
	print(f"Your name has {len(name)} letter(s)")
	print(f"Your name's first letter is {name[0]}")
	print(f"Your name's last letter is {name[len(name)-1]}")