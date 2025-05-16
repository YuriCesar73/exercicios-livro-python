# Abrir um arquivo chamado bov.txt e salvar os dados das siglas das ações e seus
# valores na seguinte ordem: ‘petr4’, ‘vale3’, ‘ggbr4’, 28.4, 31.3, 15.76.

# OBS: CASO O ARQUIVO bov.txt esteja preenchido, basta apagar o seu conteúdo.
# OBS2: CASO O ARQUIVO bov.txt não esteja presente, basta criá-lo :) !!!
acoes = ['petr4', 'vale3', 'ggbr4']
valores = [28.4, 31.3, 15.76]




f = open('bov.txt', 'w')
f.write('%s:%5.2f; %s:%5.2f; %s:%5.2f;' % (acoes[0], valores[0],acoes[1], valores[1], acoes[2], valores[2]))
f.close()

print("Finalizado!")