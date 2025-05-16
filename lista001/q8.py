# Os dados a seguir representam os preços diários de fechamentos no pregão da
# Bovespa entre os meses de setembro e outubro de 2019. A coluna A do Excel se
# refere a VALE3 (Vale do Rio Doce) e a coluna B indica GGBR4 (Gerdau). Os dados
# estão em um arquivo Excel na planilha denominada Plan1.

# Deseja-se, então, que esses dados sejam importados para o Python com a biblioteca
# xlrd e que se responda aos itens a seguir.
# (a) Importar os dados do Excel e transformar a coluna A em uma variável que
# represente a Vale e a coluna B em outra variável que represente a coluna B.
# (b) Transformar as variáveis em vetores usando a biblioteca numpy.
# (c) Fazer os dois gráficos dos preços da Vale e da Gerdau usando subplot. Colocar
# a Vale na parte superior da figura e a Gerdau na parte inferior.
# (d) Calcular os retornos das duas empresas e plotar os quatro gráficos (preço da
# Vale e seu retorno; preço da Gerdau e seu retorno) no formato de uma matriz
# com 2×2 elementos.


# OBS: O LIVRO CITA O IMPORT DO xlrd, ENTRETANTO A PARTIR DA VERSÃO 2.0, xlrd NÃO SUPORTA MAIS .xlsx, APENAS .xls.
# OBS2: Certifique-se de ter openpyxl instalado: pip install openpyxl
# OBS3: Certifique-se de ter pandas instalado: pip install pandas


import pandas as pd
import numpy as ny
import matplotlib.pyplot as plt


# Resolução letra a:
df = pd.read_excel('Plan1.xlsx', sheet_name='aba1', engine='openpyxl', header=None)
Vale = df.iloc[:, 0]
Gerdau = df.iloc[:, 1]

# Resolução letra b:
vale_array = ny.array(Vale)
gerdau_array = ny.array(Gerdau)

# Resolução letra c:
plt.figure(figsize=(10, 6))

# Subplot 1: VALE3
plt.subplot(2, 1, 1)
plt.plot(vale_array, label="VALE3", color='blue')
plt.title('Valores VALE3')
plt.ylabel('Preço')
plt.grid(True)

# Subplot 2: GGBR4
plt.subplot(2, 1, 2)
plt.plot(gerdau_array, label="GGBR4", color='green')
plt.title('Valores GGBR4')
plt.ylabel('Preço')
plt.xlabel('Dias')
plt.grid(True)

plt.tight_layout()
plt.show()

plt.savefig('grafico_vale_gerdau.png') #OBS4: Estou gerando um arquivo png caso não seja possível exibir o gráfico na plataforma em que esteja testando


# Resolução letra d:
retorno_vale = (vale_array[1:28] - vale_array[0:27]) / vale_array[0:27]
retorno_gerdau = (gerdau_array[1:28] - gerdau_array[0:27]) / gerdau_array[0:27]

plt.figure(figsize=(10, 6))

# Subplot 1: Vale - Preços
plt.subplot(221)
plt.plot(vale_array, label="VALE3", color='blue')
plt.title('Valores VALE3')
plt.ylabel('Preço')
plt.grid(True)

# Subplot 2: Gerdau - Preços
plt.subplot(222)
plt.plot(gerdau_array, label="GGBR4", color='green')
plt.title('Valores GGBR4')
plt.ylabel('Preço')
plt.grid(True)

# Subplot 3: Vale - Retorno
plt.subplot(223)
plt.plot(retorno_vale, label="VALE3", color='blue')
plt.title('Valores VALE3 - Retorno')
plt.ylabel('Retorno')
plt.grid(True)

# Subplot 4: Gerdau - Retorno
plt.subplot(224)
plt.plot(retorno_gerdau, label="GGBR4", color='green')
plt.title('Valores GGBR4 - Retorno')
plt.ylabel('Retorno')
plt.grid(True)


plt.tight_layout()
plt.show()

plt.savefig('grafico_preco_retorno_vale_gerdau.png') #OBS4: Estou gerando um arquivo png caso não seja possível exibir o gráfico na plataforma em que esteja testando



