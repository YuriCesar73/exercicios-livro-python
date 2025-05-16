# Usar a biblioteca correta e as funções matemáticas do Python, quando necessárias,
# para resolver as seguintes expressões:
# (a) y = 43 − 22
# (b) x = sen(2) − cos(4.2)
# (c) z = cos(sen(3.7) − tan(1.3))
# (d) Resto da divisão de 26 por 4.
# (e) Converter x = 46.2° para radianos.
# (f) Converter y = 3.1 rad para graus.

import math

# Resolução letra a:
y = 43 - 22
print("O valor de y é: ", y)

print("\n")

# Resolução letra b:
x = math.sin(2) - math.cos(4.2)
print("O valor de x é: ", x)

print("\n")

# Resolução letra c:
z = math.cos(math.sin(3.7) - math.tan(1.3))
print("O valor de z é: ", z)

print("\n")


# Resolução letra d:
resto_divisao = 26 % 4
print("O resto da divisão é: ", resto_divisao)

print("\n")

# Resolução letra e:
valor_radianos = math.radians(46.2)
print("O valor em radianos é: ", valor_radianos)

print("\n")

# Resolução letra f:
valor_graus = math.degrees(3.1)
print("O valor em graus é: ", valor_graus)