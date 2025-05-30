str1 = input("I will double the number you submit: ")
f = ...

""" if (str1.isdigit()):
	f= float(str1)
elif (str1.isdecimal()):
	f = float(str1) """
try:
	str1.isdigit() or str1.isdecimal()
except:
	print(f"'{str1}' is not an actual number")
f = float(str1)

print(f"The double of {f:.2f} is {f * 2:.2f}")