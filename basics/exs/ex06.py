i = 0
name = input(f"Insert your first name: ")
len1 = len(name)

try:
   if not name.isalpha():
      raise ValueError("Invalid name")
except:
   exit(f"Error: You entered an invalid name.")

while i < len1:
   print(name[i] * (i + 1), end="")
   i += 1
print()