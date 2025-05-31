# memory id:
#var = 'a'
#print(id(var))

# about None (=null)
# common to use is/is not instead of != and ==
condition = 1
bVar = None

if condition:
	bVar = True
	print("Do something")
else:
	print("Don't do anything")

if bVar is not None:
	print(f"{bVar=}")
else:
	print(f"bVar is None")
