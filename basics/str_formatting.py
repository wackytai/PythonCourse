# from ex02:
#nome = "Luiz Otávio"
#altura = 1.80
#peso = 95
#imc = peso / (altura ** 2)

#str1 = "nome tem altura de altura"
# fstring enables one to use variables inside strings by enclosing it in {}:
#str1 = f"{nome} tem {altura} de altura"
# you can format how numbers are displayed by adding : and format setting to the var
#str2 = f"{nome} tem {altura:.2f} de altura"

#print(str1)
#print(str1)
#print(str2)

a = "A"
b = "B"
c = 1.1
str2 = ("{0}" + "{1}" + "{2:.2f}").format(a, b, c)
str3 = f"{a + b + str(c)}"
formato = "a={} b={} c={}".format(a, b, c)

print(str2)
print(str3)
print(formato)

nome = "Luiz"
idade = 23
#formato = "{1} tem {0} anos"
formato = "{n} tem {i} anos"
print(formato.format(n=nome, i=idade))
