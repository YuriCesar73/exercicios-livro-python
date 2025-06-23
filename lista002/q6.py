# A tabela a seguir fornece os descontos de uma compra. Fazer um programa em
# Python que leia o valor de uma compra, determine o desconto a ser aplicado e
# calcule o valor a ser pago pelo cliente. Imprimir o valor a ser pago com PRINT( )

# Tabela 1 – Descontos
# Valor da compra (R$) | Desconto (%)
# Entre 0 e 20           5
# Entre 21 e 50          10
# Entre 51 e 100         15
# Entre 101 e 1.000      20
# Maior que 1.000        30

valor_compra = float(input("Insira o valor da compra"))



if valor_compra > 0 and valor_compra <= 20:
    desconto = valor_compra * 0.05;
    print("Valor a ser pago: ", valor_compra - desconto)
elif valor_compra > 20 and valor_compra <= 50:
    desconto = valor_compra * 0.1;
    print("Valor a ser pago: ", valor_compra - desconto)
elif valor_compra > 50 and valor_compra <= 100:
    desconto = valor_compra * 0.15;
    print("Valor a ser pago: ", valor_compra - desconto)
elif valor_compra > 100 and valor_compra <= 1000:
    desconto = valor_compra * 0.20;
    print("Valor a ser pago: ", valor_compra - desconto)
elif valor_compra > 1000:
    desconto = valor_compra * 0.30;
    print("Valor a ser pago: ", valor_compra - desconto)


    



