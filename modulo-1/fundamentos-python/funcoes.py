'''
uma função - em Python - é definida a partir do uso da palavra reservada def (esta palavra reservada/comando é utilizada para que nós, desenvolvedores, possamos criar nossas proprias funções)

def -> nome da função -> ():
    alguma(s) intrução(ões) que compõe(m) a função 
    ou seja, as "tarefas" que a função irá cumprir

    return -> expressão de retorno/resposta da função

neste momento, encontramos a implementação do conceito de indentação! sem a correta indentação a função não irá funiconar corretamente
'''

# função 1. definição de uma função simples e concisa; uso de type hints e uso de parametros
# os dois elementos logicos definidos dentro do parenteses são parametros da função: parametros nada mais são do que variaveis
# type hint: nada mais do que uma indicação de tipo é uma funcionalidade do Python que nos permite declarar, de forma explicita, qual é o tipo de dado esperado para um parametro de função ou variavel.
def saudar_usuario(cargo: str, nome: str) -> None:

    # 2. definir a tarefa que a função irá cumprir
    print(f'Olá, {nome}! Perfil: [{cargo}]') # aqui, para exibir o resultado da tarefa da função, estamos usando o recurso f-string: com o proposito de "interpolar" o valor dos paramettros/variaveis com o literal de string que definimos.

# 3. agora, precisamos chamar a função a sua execução; para este proposito precisamos criar o CALLER -> este é o objeto "chamador" da função 
saudar_usuario('Jaclin', 'manda em tudo') # este é o "chamador" da função -> caller

# 4. neste passo, vamos fazer uma segunda chamada de função 
# saudar_usuario('Janaina')

# saudar_usuario('O manda-chuva')

# -------------------------------------------------------------------------


# função 2. aqui, vamos extender as nossas implementações e analises de função 
# para este proposito vamos definir uma nova função com retorno multiplo e estruturado num conjunto de dados tipo dicionario

def analisar_numeros(a: float, b: float) -> dict:
    # passo 1: fazer uso da expressão return para, diretamente, implementar uma estrutura de dados de dicionario contendo algumas operações matematicas 

    return {
        'soma' : a + b, 

        'subtração' : abs(a - b),

        'multiplicação' : a * b,

        'divisão' : round(a / b, 2) if b != 0 else None # esta é uma instrução criada a partir de um operador ternario em python; a divisão ocorrerá se o valor dado ao parametro b for diferente de 0; caso contrario retorna None. 

    }

# passo 2. chamada da funcão; aqui, vamos fazer uso da expressão de chamada de função 
# ou seja, não é a chamada direta da função mas , sim, a atribuição da chamada à uma var e posteriormente a chamada será realizada
resultado = analisar_numeros(3, 10)

# passo 3. exibindo os valores resultantes das operações descritas na função 
print(f'Analise numérica: {resultado}')

'''
principais conceitos:

return [....] : ao inves de definirmos inumeros print(), a ideia é que a função processe os dados e, posteriormente "devolva" o resultado "empacotado" para a estrutura principal

abs(): função, com origem no python core, que nos da a possibilidade de, a partir da operação matematica indicada na função, ter como resultado o valor ABSoluto; significa que: caso minha operação gere como resultado um valor negativo, terei o valor absoluto; ex.: 3 - 10 = -7 com o uso da função abs() teremos -> 3 - 10 = 7 

round(): função, com origem no python core, que nos da a possibilidade de, a partir da operação matematica indicada na função; o uso de round() determina que o numero decimal resultante est limitado a 2 casas decimais arredondadas.
'''

# -----------------------------------------------------------------------------------------------

# função 3. implementação de função LAMBDA -> nada mais é do que uma função "sem nome/anonima"; portanto, para executarmos uma função LAMBDA é necessario associarmos esta função a um elemento lógico nomeado - à esta técnica damos o nome de EXPRESSÃO DE FUNÇÃO 

# passo 1: definir uma lista de entrada de dados com valores que representam dados monetarios em dolar
valores_usd = [10.0, 45.6, 89.9, 5.0]

# passo 2: definir uma const que representará a taxa de cambio/conversão de valores 
TAXA_CAMBIO = 5.2

# passo 3. definição da função LAMBDA - esta função tem como proposito fazer a conversão de valores em dolar para valores em real brasileiro; 

converter = lambda valor :  valor * TAXA_CAMBIO

# valor - antes dos dois pontos é o parametro da função anonima/lambda
# valor * TAXA_CAMBIO=> este é "corpo da função lambda", a tarefa que a função irá cumprir e, tambem, o contexto de resposta/resultado/retorno que a função proverá

# definir a variavel que receberá como valor os  dados convertidos para real brasileiro
valores_brl = [converter(y) for y in valores_usd]

# y = 10.0 -> 
# y = 45.6 ->
# y = 89.9 ->
# y =  5.0 ->

# passo 4. exibir o resultado
print(f'Valores em reais brasileiro: {valores_brl}')
print()
# ====================================================
# a função list(), quando usada, gera para nós uma lista de dados - tem origem no python core
# a função map(), quando usada, ela nos auxilia a mapear/iterar cada uma dos valores do conjunto de dados que estamos manipulando; portanto, a função map() é o executor da conversão  
convertido_real = list(map(lambda valor: valor * TAXA_CAMBIO, valores_usd))

print(f'Valores em reais brasileiro: {convertido_real}')

















