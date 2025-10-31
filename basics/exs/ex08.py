# Make a game with the intent for the user to guess a secret word
# Rules:
# - You can pick any word to make it secret and give the user the possibility
# of typing only one letter
# - When the user inputs this letter, you must check if it has a match in the
# word
# - If it's a match, showcase the letter
# - If it's not a match, showcase a '*' instead
# Count the amount of attempts

def printMessage(tag):
	if tag == 0:
		print("Welcome to the Secret Word Game!\n" \
		"I've picked a word now is your turn to try to guess it!\n" \
		"Let's go one letter at a time.")
	elif tag == 1:
		print("You've got a match!")
	elif tag == 2:
		print("That was a miss! Let's give it another try!")
	elif tag == 3:
		print("Congratulations! You uncovered the secret word!")
	elif tag == 4:
		print("Invalid input, try typing a letter.")
	else:
		print("Exiting the Game. Goodbye!")

word = "alcachofra"
i = 0
str1 = ""

printMessage(0)

while True:
	value = input(f"Input letter: ")
	i += 1
	bMatch = False
	if value.lower() == "exit":
		printMessage(-1)
		break
	try:
		c = value.isalpha()
	except:
		printMessage(4)
		continue
	c = value.lower()
	if len(c) != 1:
		printMessage(4)
		continue
	if c in word:
		str1 += c
		bMatch = True
	wordCreated = ""
	for char in word:
		if char in str1:
			wordCreated += char
		else:
			wordCreated += '*'
	if bMatch and word != wordCreated:
		printMessage(1)
	elif word == wordCreated:
		printMessage(3)
		break
	else:
		printMessage(2)
	print(wordCreated)
