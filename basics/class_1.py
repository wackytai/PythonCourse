'''
This is a docString, they are a sort of multiline comment.
Use it with caution, beucase python compiler will read it 
and store it in memoryalthough not being executable
'''
# print() function, space is the default separator between its arguments,
# but by using sep=<string> you can change it
# you can also change its ending instead of breakline, by using end=<string>
# print(123,34, end="#", sep="0")
# custom settings must always come as last arguments of the function
# print(sep=';', 123,34) WILL GIVE YOU AN ERROR
print(123,34)
print(123,34, sep="--")
# as other programming languages, use '\' to display
# the next character inside a string instead of interpreting it
# 'r' before a string can be used to show the escape chars
print("This is a \"string\"")
print(r"This is a \"string\" using r infront")
print('Explícito', 'é', 'melhor " do que implícito')
# print(type('this'))
# type converstion, typecasting, coercion: str(1), int('1'), float('1'), bool()
# for bool(): empty strings return false, white any size strings return true
# bool('') = False | bool(' ') = True

# variables:
name = 'Luiz'
age = 30
bIsAgeMajority = age >= 18
print(bIsAgeMajority)
