# Dados três lados de um triângulo qualquer, fazer um programa para descobrir se
# o triângulo é equilátero, isósceles ou escaleno. Entrar com os valores com input.

lado_a = float(input("Digite o valor do primeiro lado do triângulo: "))
lado_b = float(input("Digite o valor do segundo lado do triângulo: "))
lado_c = float(input("Digite o valor do último lado do triângulo: "))

if lado_a == lado_b and lado_b == lado_c:
    print("O triângulo é equilátero")

elif lado_a == lado_b or lado_b == lado_c or lado_a == lado_c:
    print("O triângulo é isósceles")

else:
    print("O triângulo é escaleno")