# Arithmetic operators:
#  add: +
#	if you add int with a float, the result will be a float
# subtract: -
# multiply: *
# power: **
# true division: / (retuns a floating-point result)
# floor division: // (returns largest integer less than or equal to the result)
# module: %
# concat:
""" concat = 'Luiz' + ' ' + 'Miranda'
print(concat)

# repetition:
char = 'A'

print(char * 10) """

#operations priority:
# 1. (n + n)
# 2. **
# 3. * / // %
# if you have several operators with same piro, it starts from the left
# 4. * -

# ----------------------------------------------------------------------------

# Comparison operators:
# > (greater)
# >= (greater or equal)
# < (less)
# <= (less or equal)
# == (equal)
# != (not equal)
# the result is always a bool of the result

# ----------------------------------------------------------------------------

# Logical operators:
# and
# or
# not
# Values considered as false: 0 0.0 "" False Null (None?)
# if 1 and 1:
	# the statement velow would be a conditional
	# so it stops at the first false value and returns it.
	# It is known as -- Short-circuit evaluation --
#	print(True and 1 and False)

""" userInput = input("[E]nter or [Q]uit: ")
userPassword = input("Enter password: ")

allowedPassword = "123456"
if (userInput == 'E' or userInput == 'e') and userPassword == allowedPassword:
	print("Enter")
elif userPassword != allowedPassword:
	print("Wrong password")
	print("Quit")
else:
	print("Quit") """
str1 = None
str2 = ''

if not str1:
	print(bool(str1))
if not str2:
	print(bool(str2))
print('-' * 10)
if 1:
	print(True and False and 1)
if 1:
	print(True and '' and 1)
if 1:
	print(True and None and 1)