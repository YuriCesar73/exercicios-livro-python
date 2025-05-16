# Assumir como constante no comando de linha do Python x = 3 e y = 6 e imprimir
# usando PRINT( ) o resultado das equações seguintes:
# (a) w = ex − ln(y)
# (b) z = x*y2 + y*cos(x)
# (c) s =
# x
# + ln ( x + y ) + tan ( x )
# y

# OBS: A expressão da letra c está dentro de uma raiz quadrada

import math

x = 3
y = 6

# Resolução letra a:
w = math.pow(math.e, x)
print("O valor de w é: ", w)

print("\n")
# Resolução letra b:
z = (x * math.pow(y, 2)) + (y*math.cos(x))

print("O valor de z é: ", z)
print("\n")

# Resolução letra c:
s = math.sqrt(x / y + math.log(x + y) + math.tan(x))
print("O valor de s é: ", s)
