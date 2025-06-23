# O “suporte” de uma ação é calculado como 30% do intervalo histórico de uma ação
# (máximo subtraído do mínimo). A “resistência” é calculada como o valor de 60%
# do intervalo histórico. Veja o exemplo:
# Baixa histórica: 1.50
# Alta histórica: 2.20
# Suporte: 1.5 + (2.20 – 1.50) * 0.3
# Resistência: 1.5 + (2.20 – 1.5) * 0.6
# Fazer um programa em Python em que o usuário forneça com input o valor mais
# baixo historicamente e o valor mais alto. O programa pede o valor atual da ação
# também com input e diz com PRINT( ) qual é o suporte, qual é a resistência e se o
# preço da ação está dentro da faixa de suporte-resistência ou fora dela.

valor_baixo = float(input("Insira o valor mais baixo históricamente: "))
valor_alto = float(input("Insira o valor mais alta históricamente: "))
valor_atual = float(input("Insira o valor atual da ação: "))

taxa_suporte = 0.3
taxa_resistencia = 0.6

diferenca_historica = valor_alto - valor_baixo


suporte = valor_baixo + (diferenca_historica * taxa_suporte)
resistencia = valor_baixo + (diferenca_historica * taxa_resistencia)


print("Valor suporte: ", suporte)
print("Valor resistência: ", resistencia)

if valor_atual < suporte:
    print("O valor atual está abaixo do valor do suporte. Fora da faixa suporte-resistência")
elif valor_atual >= suporte and valor_atual <= resistencia:
     print("O valor atual está na faixa de valores suporte-resistência")
else: 
     print("O valor atual está acima do valor da resistência. Fora da faixa suporte-resistência")

