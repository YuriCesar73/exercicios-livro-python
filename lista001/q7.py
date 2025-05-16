# Observar a seguinte lista de dados, lista= [2, 2, 3, 3, 3, −1, −1, −2, 0, 0, 0, 2, 4, 5, 1, 2, 2, 0, 0, 0,2 ,1, 5, 5, 7, 6, 5, 0, 0]. 
# Programar o Console para encontrar as seguintes medidas estatísticas:
# (a) Soma de todos os elementos.
# (b) Máximo elemento da lista.
# (c) Mínimo elemento da lista.
# (d) Média dos elementos da lista.
# (e) Mediana dos elementos da lista.
# (f) Moda dos elementos da lista.
# (g) Desvio-padrão amostral.
# (h) Desvio-padrão populacional.
# (i) Contar o número de vezes que aparece o número 0.
# (j) Contar o número de vezes que aparece o número 5.
# (k) Ordenar a lista em ordem crescente.
# (l) Ordenar a lista em ordem decrescente.

import statistics as st

lista = [2, 2, 3, 3, 3, -1, -1, -2, 0, 0, 0, 2, 4, 5, 1, 2, 2, 0, 0, 0, 2 ,1, 5, 5, 7, 6, 5, 0, 0]
# lista = [1, 3, 5]

# Resolução letra a:
print("Valor da soma de todos os elementos: ", sum(lista))

# Resolução letra b:
print("O maior elememento da lista é: ", max(lista))

# Resolução letra c:
print("O menor elemento da lista é: ", min(lista))

# Resolução letra d:
print("A média dos elementos da lista é: ", st.mean(lista))

# Resolução letra e:
print("A mediana dos elementos da lista é: ", st.median(lista))

# Resolução letra f:
print("A moda dos elementos da lista é: ", st.mode(lista))

# Resolução letra g:
print("O desvio padrão é: ", st.stdev(lista))

# Resolução letra h:
print("O desvio padrão populacional é: ", st.pstdev(lista))

# Resolução letra i:
print("Quantidade de vezes que o número 0 aparece: ", lista.count(0))

# Resolução letra j:
print("Quantidade de vezes que o número 5 aparece: ", lista.count(5))

# Resolução letra k:
lista.sort()
print("Lista ordenada de forma crescente: ", lista)

# Resolução letra l:
lista.sort(reverse=True)
print("Lista ordenada de forma decrescente: ", lista)



