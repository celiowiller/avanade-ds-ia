# esta é uma linha de comentarios 

'''
este, por exemplo, é 
um comentario de bloco
me python
'''

# abaixo, temos a função print(): esta função é definida dentro do python "core", ou seja, é o proprio python que nos dá esta função. Portanto, basta a nós, simplesmente, fazer o uso adequado: fazer referencia a esta função

# o "papel" da função print() é nos ajudar a exibir qualquer coisa, que queiramos, em tela.
print('Ola Mundo! Amo Python, voce, Python, é maravilhoso!')

print()

print('=========================================================')
print('DEFINIÇÃO-BASE DO PYTHON: INFERENCIA DE TIPO')
print()

# declarar 3 variaveis
primeiroNumero = 210
segundoNumero = 456.98
NOME = 'Pandabox'
nome = 'Nicole'

# fazer uso da função print() para exibir os valores das vars, acima
print('---------- VALORES ATRIBUIDOS --------------')
print(primeiroNumero)
print(segundoNumero)
print(NOME)
print(nome)

NOME = 'Bruno'
print(NOME)
print()
print('=============== ESTES SÃO OS TIPOS DE DADOS DEFINIDOS/INFERIDOS PARA AS VARS ================')

# VAMOS OBSERVAR QUAIS SÃO OS TIPOS INFERIDOS PARA AS VARS
print(type(primeiroNumero))
print(type(segundoNumero))
print(type(NOME))
print(type(nome))

print('=============== MANIPULAÇÃO DE STRINGS ================')

# vamos definir uma variavel para receber como valor uma string/texto/frase
umaFrase = 'Hoje é um dia excelente!'

# aqui, abaixo, serão exibidos os valores das manipulações
print()
print('----------- Manipulando a string ------------')

print(umaFrase)      # aqui, temos a string inteira - com todos os seus caracteres
print(umaFrase[23])   # aqui, queremos somente um "pedacinho" da string; para este proposito usamos o operador  slice/fatiamento [] - colchete. Este operador, aqui, assume a funcionalidade de extrair um determinado caractere de um conjunto de caracteres.

'''
abaixo, na sequencia de caracteres/string, temos - de forma "implicita/oculta" - uma sequencia numérica, crescente, que se inicia com o valor 0 (zero) que nos indica o seguinte: qual é a posicão, dentro do conjunto de caracteres, cada caractere ocupa! E, para este conjunto, oculto/implicito, o python o nomeia como INDICE POSICIONAL.

INDICES POSICIONAIS:
                         0  1  2  3 4 5 6  7  8 9  10 11 12 13 14 15 16 17 18  19  20 21 22  23
                         H  o  j  e   é    u  m     d  i  a     e  x  c  e  l   e   n  t  e   !
'''

print(umaFrase[2:15])   # aqui, neste momento, estamos fazendo outro "fatiamento"! Mas, este é o "fatiamento" de um intervalo de valores/caracteres/dados. Aqui, portanto, criamos um SUBCOJUNTO DE DADOS/CARACTERES, ou seja, uma substring.

# [.............[ = intervalo de valores semi-aberto que determina que: no intervalo, o primeiro é incluido e o ultimo valor será excluido; essa determinação é operada a partir da seguinte operação: umaFrase[2:15] (-1) = 2:14

print(umaFrase[:8])     # aqui, o intervalo de caracteres inicia-se na posição 0 pois não temos nenhum indice posicional, explicitamente, definido. Então, o python "interpreta" que o indice posicional inicial é 0 zero.

# [.............[ = intervalo de valores semi-aberto que determina que: no intervalo, o primeiro é incluido e o ultimo valor será excluido; essa determinação é operada a partir da seguinte operação: umaFrase[:8] (-1) = :7

print(umaFrase[3:])    # aqui, estamos, novamente, gerando um outro intervalo de caracteres. Neste passo, temos um indice posicional inicial. Mas não temos um indice posicional final. Portanto, a operação de intervalo semi-aberto NÃO SE APLICA.

print(umaFrase + ' Muito bom! Que todos os sejam assim') # aqui, nesta operação, estamos praticando a associação/ligação/concatenação/junção de dois elementos: a nossa variavel umaFrase e uma nova string. Para este  proposito, estamos estruturando esta operação fazendo uso do operador + (mais/soma/plus....)