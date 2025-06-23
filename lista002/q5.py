# Considere uma equação do segundo grau:
# Ax 2 + Bx + C = 0
# Utilizando-se ∆ = B 2 − 4 AC , escrever um programa em Python que calcule as
# raízes da equação tal que:

# (i) Se não há raízes (Δ < 0), o programa retorna um PRINT “não existem raízes
# reais”.

# (ii) Se há uma única raiz (Δ = 0), o programa mostra ao usuário a única raiz calcu-
# lada como: x1 = −B / (2*A).

# (iii) Se há duas raízes, mostre ao usuário calculando-as desta forma:
# x1 =−B + ∆
#        2A


# x2 = −B − ∆
# 2A

import math

print("Vamos calcular as raízes de uma equação de segundo grau")

a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

delta = math.pow(b, 2) - (4 * a * c);

if delta < 0:
    print("\nnão existem raízes reais")
elif delta == 0:
    valor_raiz = (-1 * b) / (2*a);
    print("\nValor da raiz: ", valor_raiz)
else:
    valor_raiz_um = ((-1 * b) + math.sqrt(delta)) / 2*a

    valor_raiz_dois =  ((-1 * b) - math.sqrt(delta)) / 2*a

    print("\nValor da primeira raiz: ", valor_raiz_um)
    print("\nValor da segunda raiz: ", valor_raiz_dois)


