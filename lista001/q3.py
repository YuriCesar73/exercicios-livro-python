# Criar a lista de números num=[3, 3, 4, 1, 2, 1, 1, 2, 3, 4, 4, 1, 1, 5, 2] e fatiá-la con-
# forme os itens a seguir:
# (a) Fatiar do elemento de índice 2 ao de índice 3.
# (b) Fatiar do quinto elemento ao nono elemento.
# (c) Fatiar do elemento de índice 1 ao último.
# (d) Fatiar do primeiro elemento ao último.
# (e) Fatiar do primeiro elemento ao último saltando de três em três elementos.
# (f) Selecionar o último elemento da lista.
# (g) Selecionar os três últimos elementos da lista.
# (h) Selecionar os quatro primeiros elementos da lista.
# (i) Contar o número de elementos da lista.
# (j) Contar quantas vezes aparece o número 1 na lista.

num=[3, 3, 4, 1, 2, 1, 1, 2, 3, 4, 4, 1, 1, 5, 2]

# Resolução letra a:
print(num[2:4])

# Resolução letra b:
print(num[5:10])

# Resolução letra c:
print(num[1:])

# Resolução letra d:
print(num[0:])

# Resolução letra e:
print(num[0::3])

# Resolução letra f:
print(num[-1])

# Resolução letra g:
print(num[-3:])

# Resolução letra h:
print(num[:4])

# Resolução letra i:
print(len(num))

# Resolução letra j:
print(num.count(1))
