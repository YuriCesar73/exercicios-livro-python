# O financiamento de um automóvel foi contratado respeitando a série matemática a
# seguir para 70 meses. Criar um algoritmo em Python para calcular a soma seguinte
# até o termo n que o usuário desejar, seguindo a lógica a seguir.
# 
# S=    70 69 68 67
#       + + + + ...
#       7 14 21 28

n = int(input("Insira a posicao do termo n que você deseja saber a soma: "))

soma = 0.0

numerador = 70
divisor = 7
for i in range(n):
    soma = soma + (numerador / divisor)
    numerador = numerador - i
    divisor = divisor + 7

print("A soma é: ", soma)
