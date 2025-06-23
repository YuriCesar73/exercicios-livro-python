# Um website de compras deseja deixar um link para os franqueados entrarem com o
# valor de compra de um produto no input e o valor de venda no input e descobrir se
# o lucro foi menor que 10%, entre 10% e 20%, ou superior a 20%. Para tanto, deve-se
# fazer um programa em Python que imprima a mensagem com PRINT( ) dizendo
# em qual faixa a mercadoria do comerciante se localiza

valor_compra = float(input("Insira o valor de compra: "))
valor_venda = float(input("Insira o valor de venda: "))


faixa_lucro = valor_venda / valor_compra

if faixa_lucro < 1.1:
    print("Menor que 10%")
elif faixa_lucro <= 1.2:
    print("Na faixa de 10%-20%")
else:
    print("Superior a 20%")