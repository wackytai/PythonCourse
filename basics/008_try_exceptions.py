#try means you will literally try to execute a code snippet
#if it gives you an error, you catch it through except
#an 'IF' statement only checks a condition, it doesn't prevent errors from happening
str1 = input("I will double the number you enter here: ")
f = ...

""" if (str1.isdigit()):
	f = float(str1)
elif (str1.isdecimal()):
	f = float(str1) """
try:
	str1.isdigit() or str1.isdecimal()
except:
	print(f"Error: '{str1}' is not an actual number")
f = float(str1)

print(f"The double of {f:.2f} is {f * 2:.2f}")