# For loops: it does not work directly with indexes, it takes the value itself
nb = 0
str1 = "Hello!" # Object to be iterated
#str2 = ""
#
#for c in str1:
#	str2 += c
#	print(str2)

# For loop with Range function: range -> range(start, stop, step)
maxNb = 10

for nb in range(0, maxNb, 2):
	print(f"Value: {nb}")

# for c in str1:
#c = iter(str1) # iterator
#while True:
#	try:
#		print(next(c))
#	except StopIteration:
#		break
	