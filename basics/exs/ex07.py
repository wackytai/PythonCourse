# Creating a calculator with while loops:
# 1) Ask the first number for the user
# 2) Ask the second number for the user
# I decided to use only floats just for the sake of simplicity
import sys

def	check_input(value):
	if value.lower() == "exit":
		print(f"Goodbye")
		sys.exit()

def	get_info(question):
	str1 = ...
	if question == 1:
		str1 = "Insert first number"
	elif question == 2:
		str1 = "Insert second number"
	elif question == 3:
		str1 = "Insert operator"
	in1 = input(f"{str1}: ")
	check_input(in1)
	return in1

def check_operation(operator):
	if operator == '+' or operator == '-' or operator == '/' or operator == '*':
		return 1
	return None

def	apply_operation(nb1, nb2, operator):
	if operator == '+':
		return nb1 + nb2
	elif operator == '-':
		return nb1 - nb2
	elif operator == '/':
		return nb1 / nb2
	elif operator == '*':
		return nb1 * nb2

while True:
	nb1 = ...
	nb2 = ...
	while True:
		input_value = get_info(1)
		try:
			nb1 = float(input_value)
			break
		except:
			print(f"Invalid value. Try Again")
			continue
	while True:
		input_value = get_info(2)
		try:
			nb2 = float(input_value)
			break
		except:
			print(f"Invalid value. Try Again")
			continue
	while True:
		input_value = get_info(3)
		if not check_operation(input_value):
			print("Invalid operator. Try Again")
			continue
		else:
			print(f"{apply_operation(nb1, nb2, input_value)}")
			break
