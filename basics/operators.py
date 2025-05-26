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
concat = 'Luiz' + ' ' + 'Miranda'
print(concat)

# repetition:
char = 'A'

print(char * 10)

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
# AND
# OR
# NOT
# Values considered as false: 0 0.0 "" False Null

userInput = input("[E]nter or [Q]uit: ")
userPassword = input("Enter password: ")

allowedPassword = "123456"
if userInput == 'E' and userPassword == allowedPassword:
	print("Enter")
elif userPassword != allowedPassword:
	print("Wrong password")
	print("Quit")
else:
	print("Quit")