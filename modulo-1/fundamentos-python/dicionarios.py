'''
um dicionario - em python - também é um conjunto de dados; da mesma forma que uma string e uma lista 
!
mas com algumas diferenças:

    1 - para definirmos um dicionario é necessario usar  os caracteres { } chaves
    2 - um dicionario é composto por pares chave : valor/key : value
    3 - o conceito de INDICE POSICIONAL NÃO EXISTE para um dicionario; então, um valor(VALUE) será selecionado por sua chave(KEY) associada; 

    **** no mais, tudo aquilo que foi observado para uma lista/string tambem pode ser aplicado a um dicionario
'''

# definir um dicionario
d = { # aqui, inicialmente, temos um dicionario vazio
    
    # agora, vamos definir os pares chave : valor / key : value

    # chave : valor
    # key   : value
    'Nome'  : 'Florinda',
    'idade' : 37,
    'Curso' : 'Visual Basic',
    40      : 'florinda@mail.com'

}

# exibir o dicionario
print('Este é meu novo conjunto de dados - um dicionario: ', d)

print()
print('================= OPERAÇÕES COM DICIONARIOS ==================')

# selecionar/extrair um valor do dicionario 
print('Imprimir o nome que esta sssociado a chave Nome: ', d['Nome']) # o valor que queremos exibir é acessado a partir da chave que compõe o conjunto de dados do dicionario 

print('Imprimir a idade que esta associada a chave idade: ', d['idade']) # o valor que queremos exibir é acessado a partir da chave que compõe o conjunto de dados do dicionario 

print('Imprimir todos os dados do dicionario: ', d['Nome'], d['idade'], d['Curso'], d[40])