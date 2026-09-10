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

# ----------------------------------------------------------------------

print()
print('NOVO DICIONARIO / "criado automaticamente"')

# definindo o novo dicionario
novoDicionario = {
    # chave     :     valor
    # key       :     value
     y          :     y*y # temos, aqui, os pares chave/valor -> minha chave é o y e o valor associado a minha é: o valor da variavel/chave/key y² (y elevado ao quadrado)

     # iteração:

     # 0       : 0*0 = 0
     # 1       : 1*1 = 1
     # 2       : 2*2 = 4
     # 3       : 3*3 = 9
     # .....
     # .....
     # .....
     # 7      : 7*7 = 49

     # vamos fazer uso de uma função, a nós, pelo python
     for y in range(8)
     # esta é a instrução para gerar os pares key/value que compôem o dicionario.

     # o uso da função range() determina que, ao ser executada, será criado um intervalo de valores; neste caso o intervalo é gerado da seguinte forma: range(8) = 0, 1, 2, 2, 4, 5, 6, 7

     # for.... in -> este é o loop que, fazendo uso da variavel iterado - que, neste caso, é o y - gera o intervalo de valores "iterando" sobre cada valor numerico que a função range() gera!
}

# exibir o dicionario criado
print(novoDicionario)