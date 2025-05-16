# Criar a lista com nomes das bolsas de valores do mundo: Bolsas = [‘dow’, ‘ibov’, ‘ftse’,‘dax’, ‘nasdaq’, ‘cac’]. 
# Fatiá-la conforme os itens a seguir.
# (a) Selecionar as três primeiras.
# (b) Incluir a sublista Bs = [‘hong kong’, ‘merval’] na lista anterior.
# (c) Descobrir qual o índice da ‘nasdaq’.
# (d) Remover ‘cac’ da lista.
# (e) Inserir “sp&500” como índice 2 na lista de bolsas, mas sem excluir nenhum
# elemento já inscrito.


bolsas = ['dow', 'ibov', 'ftse','dax', 'nasdaq', 'cac']

# Resolução letra a:
print(bolsas[:3])


# Resolução letra b:
sub_lista_bolsas = ['hong kong', 'merval']
bolsas.append(sub_lista_bolsas)
print(bolsas)

# Resolução letra c:
print("indice: ", bolsas.index('nasdaq'))

# Resolução letra d:
bolsas.remove('cac')
print(bolsas)

# Resolução letra e:
bolsas.insert(2, 'ps&500')
print(bolsas)

