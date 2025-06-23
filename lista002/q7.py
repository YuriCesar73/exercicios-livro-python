# Uma loja de departamentos de roupas de cama e banho percebeu que, se separar seu
# servidor de vendas em pedidos pares e ímpares, o atendimento fica mais ágil. Fazer um
# algoritmo em Python em que se deve ler o número que representa o total de vendas n
# de uma sequência de números naturais e, posteriormente, ler a própria sequência com
# input. Armazenados os números da sequência, o programa deve mostrar com PRINT( )
# o valor da soma dos números pares (SP) e o valor da soma dos números ímpares (SI).

qtde_pedidos = int(input("Insira a quantidade de pedidos: "))

soma_impar = 0
soma_par = 0

valor_pedido = 0
for numero_pedido in range(qtde_pedidos):

    valor_pedido = float(input("Insira o valor do pedido {}: ".format(numero_pedido + 1)))

    if numero_pedido % 2 == 0:
        soma_impar = soma_impar + valor_pedido
    else:
        soma_par = soma_par + valor_pedido


print("Valor da soma dos pedidos impares", soma_impar)
print("Valor da soma dos pedidos pares: ", soma_par)
