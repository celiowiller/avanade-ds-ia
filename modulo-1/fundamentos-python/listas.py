# PYTHON LISTS - listas com python

'''
Uma lista, em python, determina que podemos ter um conjunto de dados COMPOSTO POR QUALQUER TIPO DE DADO/VALOR - ou seja, data types diferentes podem compor uma mesma lista!

A estrutura de um conjunto de dados do tipo list/lista segue a mesma premissa de um conjunto de dados do tipo string:  ou seja, cada valor que compõe a lista oucpa um INDICE POSICIONAL
'''

# definir uma lista - para este proposito, criaremos uma variavel e, à ela, atribuiremos um valor que seja descrito da seguinte forma: dentro de [] COLCHETES. Agora, ao usarmos o caractere [] - aqui, ele assume "o papel" de uma lista python - podemos criar o conjunto de dados LIST

umaLista = [1, 'PALAVRA', 'c', 'yuiaosidf4', 256.8] # aqui, o que define a lista é o caractere []

listona = [74, 'Sopranos', ['Python', 879, ['xalala', 568.9, 12], 50]]

# exibir as listas
print(umaLista)
print()
print(listona)

# -------------------------------------------------------------------------------------

print()
print('=====================  OPERAÇÕES COM LISTAS ====================')

print(umaLista[2])
print()
print('========= aqui, vamos manipular a listona ==============')
print(listona[1])
print(listona[2])
print(listona[2][1])
print(listona[2][2][2]) # quero o numero 12


print()
print('=====================  OUTRAS OPERAÇÕES COM LISTAS ====================')

# definir uma nova lista
# INDICES POSICIONAIS   0         1     2          3              4         5
lingProg = [         'Python', 'Java', 'C#', 'Visual Basic', 'javascript', 'C']

# exibir alguns resultados de operações 
print(lingProg[2])   # saida: C#
print(lingProg[1:])  # saida:  'Java', 'C#', 'Visual Basic', 'javascript', 'C'



print(lingProg[::-1])

print('resultado', lingProg[-1::-3])

# exercicio Luis
sub_lista_luis = lingProg[1:6:4]     # aqui, aplica-se o intervalo semi-aberto lingProg = [1:6] (-1) = [1:5]
print(sub_lista_luis)

'''
                                                          [-1   :    : -1
print('resultado', lingProg[-1::-1]) -> lê-se dessa forma: start:stop:step

start: inicie a leitura/construção do intervalo em -1; significa que a leitura/construção será invertida, ou seja, inicia-se pelo ultimo valor do conjunto

stop: determina qual é o ponto-de-parada do intervalo; neste caso, não temos.

step: determina o passo-a-passo que a instrução executa para a leitura/construção do novo intervalo; neste caso, inicia no ultimo valor e, um-a-um, irá até o primeiro valor do intervalo.
'''
