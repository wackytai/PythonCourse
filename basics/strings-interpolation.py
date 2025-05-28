# think about how print() is constructed in C. Python can do it directly:
name = "Luiz"
price = 1000.938745984
var = "%s, o preço é R$%.2f" % (name, price)
print(var)
print("O hexadecimal de %d é %08X" % (1500, 1500))