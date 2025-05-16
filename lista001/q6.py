# Abrir o arquivo bov.txt do exercício anterior no Console e imprimir o resultado
# dos elementos existentes nele.

# OBS: ESSE EXERCÍCIO DEPENDE DA RESOLUÇÃO DO EXERCICIO ANTERIOR
# OBS2: CASO O ARQUIVO bov.txt não esteja presente, basta criá-lo :) !!!

f=open('bov.txt', 'r')
y = f.read()

print(y)

f.close()
