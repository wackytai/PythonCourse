# While loops execute an action while a condition is true
# 'break' is the command used to interrupt a loop
# 'continue' is the command used to skip iterations of the loop, use wisely
# these can be very tricky to use because it's easy to trigger an infinite loop:
#while True:
#    print("This is an infinite loop.\nit has not breaking point")
#print(123)
#------------------------------------------------------------------------------
# Break a Loop with a comparison operator in the loop header:
i = 0
len = 10

while i < len:
    i += 1
    print(i)
print("The loop reached its end through a header condition.")
#------------------------------------------------------------------------------
# Break a Loop with an 'if' in the loop body, using 'break':
bCondition = True

while bCondition:
    name = input(f"Insert your first name: ")
    print(name)

    if name == "exit":
        break

print("The loop reached its end through an 'if' statement.\n")
#------------------------------------------------------------------------------
# Skipping the loop, using 'continue':
index = 0
len = 40

while index < len:
    index += 1
    #skip printing numbers that are not divisible by 10, starting on 10:
    if index > 9 and index % 10:
        continue
    print(index)

print("The loop reached its end AND skipped some parts of the loop")
#------------------------------------------------------------------------------
# Nested While Loop:
row = 0
size = 9

while row < size:
    col = 0
    while col < size:
        if col == 0 or col == (size - 1):
            print('1 ', end="")
        elif row == 0 or row == (size - 1):
            print('1 ', end="")
        else:
            print('0 ', end="")
        col += 1
    print()
    row += 1
#------------------------------------------------------------------------------
# While / Else (Python particularities):
# When a while loop is executed completely (no breaks!), the else section comes in
string = "random value"

i = 0
while i < len(string):
    c = string[i]
    print(c)
    i += 1
else:
    print("Else section was executed")