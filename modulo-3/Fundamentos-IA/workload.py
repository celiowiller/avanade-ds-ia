# 1. importação dos recursos necessarios
import numpy as np # recurso de matematica/cientifica/numérica do python
from sklearn.feature_extraction.text import TfidfVectorizer # recurso usado para a asserção de texto em conjunto de vetor numerico
from sklearn.linear_model import LogisticRegression # regressão logistica para aprendizado do modelo
from sklearn.metrics import accuracy_score # pontuação de precisaõ do modelo

# 2. conjunto de dados {nosso Workload de treino}
dados_treino = [
    # frases referentes a IA (label 1)
    'A IA generativa cria novos textos e imagens',     
    'Modelos de machine learning aprendem com dados',    
    'Visão computacional detecta objetos e tarefas',    
    'Redes neurais otimizam tarefas complexas de NLP',

    # frases referentes a NÃO-IA(label 0)   
    'O servidor de inferência está com alta latencia',  
    'O banco de dados relacional caiu e precisa ser reiniciado',
    'Falha de rede o cluster Kubernetes e storage',
    'A  CPU do servidor atingiu 100 por cento de uso'
]

# 3. agora, vamos definir a lista de labels/rotulos de treino
labels_treino = [1, 1, 1, 1, 0, 0, 0, 0]

# 3.1. algumas stop words em protugues
stop_word_pt = [
    'a', 'o', 'as', 'os', 'de', 'da', 'do', 'das', 'dos', 'em', 'no', 'na', 'nos', 'nas', 'com', 'para', 'por', 'e', 'está'
] # o uso do stop_word_pt ´pe interessante pois, ao usa-lo, estamos evitando "poluir" com termos irrelevantes os espaços atribuidos ao valores e deixando de causar "alguns ruidos" no dataset

# 4. pré -processamento de extração das features (proceos de NLP/Vectorization)
# vetorizar  a lista stop_word_pt
vectorizer = TfidfVectorizer(
    stop_words = stop_word_pt, ngram_range=(1, 2) # este metodo gera tokens compostos como, por exemplo: "banco de dados", "servidor caiu", "alta latencia"; ao fazer isso, temos a permissão de uso de expressões de contexto completo para mapeamento
) # criamos o objeto de vetorização

X_train = vectorizer.fit_transform(dados_treino) # fazemos uso do objeto para ajustar e transformar nosso conjunto de dados naquilo que queremos que o nosso modelo ML aprenda

print('dados_treino vetorizado: ', X_train)

# 5. treino do Modelo (training phase)
# NOSSO MODELO TEM UMA TAREFA ESPECIFICA: FAZER CALSSIFICAÇÃO DE DADOS; PARA ESTE PROPOSITO ELE, MODELO, VAI ACESSAR O DATASET AJUSTADO -a partir do metodo fit_transform - vai associar ao numeros definidos dentro do conjunto labels_treino.

## ESTE É O NOSSO ML DE Regressão Logistica
model = LogisticRegression() # algoritmo utlizado para a classificação (de elementos de acordo com nossas premissas; por exemplo -> detecção de um email e classifica-lo como spam ou nao)

# fit(), significa APRENDER; portanto, o método irá ler todo o conjunto dados_treino e constrói um "vocabulario" proprio - mapeandop cada string do conjunto;
model.fit(X_train, labels_treino) # aqui, o modelo aprende/se ajusta de acordo com os dados que oferecemos para ele; estes dados são, na verdade, 2 conjuntos/matrizes: X_train vetoriza dados_treino e labels_treino;
# A ETAPA DE TREINAMENTO É O GRADIENT DESCENT 
# portanto, nosso modelo frará uma associaçãod e Pesos -  a partir dos valores transformados na matriz resultante no metodo fit_transform()

# X_train são os dados que queremos classifica 
# labels_treino são so dados que usaremos como classificadores
## portanto, temos o seguinte: ['positivo', negativo, positivo]

# então, nosso modelo ML irá aprender a associar matematica entre os padrões de palavras presentes na matriz de texto - dados_treino. Se tudo correr, o modelo estará pronto para fazer predições caso encontre novos textos 

'''
=============================================================================
DADOS DE TESTE DO MODELO - OU SEJA, AGOA, OFERECEMOS À ELE UM CONJUNTO DE DADOS 
PARA QUE ELE "ADIVINHE" SE É IA/ML OU INFRAESTRUTURA
=============================================================================

'''


# 6. Inferência (nova phase)
novos_dados = [
    'Agentes de IA tomam decisões autonomas',
    'O banco de dados do servidor caiu!'
]

# 6.1. saida esperada:  1 = IA/ML, 0 = Outra coisa, Infra
labels_teste_reais = [1, 0]

# 7. testando o modelo ML com os novos dados 
X_test = vectorizer.transform(novos_dados)
predicoes = model.predict(X_test) # aqui, estamos testando o modelo com os novos dados que foram vetorizados - no passo anterior

# 7.1. Vamos calcular a acuracia/precisão do modelo
acuracia = accuracy_score(labels_teste_reais, predicoes)

# 7.2. exibir a acuracia/precisão do modelo
print(f'----------- Acuracia/Precisão do modelo de teste: {acuracia * 100: .2f}% ------------/n')

# 8. exibindo o resltuado das inferencias 
for texto, pred, real in zip(novos_dados, predicoes, labels_teste_reais):
    cat_pred = 'IA/ML' if pred == 1 else 'Infraestrutura'
    cat_real = 'IA/ML' if real == 1 else 'Infraestrutura'
    status   = 'ACERTOU' if pred == real else 'ERROU'
    print(f'Texto: {texto}')
    print(f" -> Previsto: '{cat_pred}' -> Real: {cat_real}[{status}]")


'''
for texto, pred in: aqui, estamos iterando a combinação dos dois conjuntos de dados com duas variaveis auxiliares - texto e pred - texto percorre o conjunto de dados novos_dados e pred percorre o valor retornado pelo modelo.

zip(novos_dados, predicoes): zip é uma função com origem no python core; seu objetivo é "zipar/compactar/juntar" duas listas/conjuntos de dados - elemento por elemento; se o conjunto novos_dados possuem textose predicoes contem numero/labels a função zip junta cada texto com sua previsão correspondente.

categoria = 'IA/ML' if pred == 1 else 'Infraestrutura': esta faz uso da estrutura de decisão if/else em unica linha de codigo; aqui, avaliamos o seguinte -> se a previsão - valor da var pred - for igual/identico a 1 a variavel categoria ecebe como valor a string "IA/ML"; caso contrario, (se for 0) recebe o valor "Infraestrutura".


'''

