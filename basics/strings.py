# strings interpolation
#  think about how print() is constructed in C. Python can do it directly:
""" name = "Luiz"
price = 1000.938745984
var = "%s, o preço é R$%.2f" % (name, price)
print(var)
print("O hexadecimal de %d é %08X" % (1500, 1500)) """

# -----------------------------------------------------------------------
# basics of string formatting: f-strings:
""" var = "ABC"
print(f"-{var}-")
print(f"-{var:$>10}-")
print(f"-{var:$<10}-")
print(f"-{var:$^10}-")
print(f"{1000.4283748726497392:0>+10,.1f}")
print(f"{1000.4283748726497392:0=+10,.1f}")
print(f"O hexadecimal de 1500 é {1500:08X}")
print(f"{var!r}")
print(f"{var!s}")
print(f"{var!a}") """

# -----------------------------------------------------------------------
# splitting strings:
# str[start:end:pace]
# last index is never inclusive !
var = "Hello world"
print(var[4])
print(var[:4])
print(var[4:10])
print(var[-7:-1])
print(var[4:])
print(var[0:len(var):1])
print(var[0:len(var):2])
print(var[::-1])
print(var[-1:-len(var)-1:-1])