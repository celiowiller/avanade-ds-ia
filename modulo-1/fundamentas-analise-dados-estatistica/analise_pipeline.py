# ==========================================
#  PASSO 1. Importar bibliotecas
# ==========================================

import numpy as np # numpy é a biblioteca "numérica" do python; conhecida, tambem, como biblioteca numerica de alta performance do python; é usada para inumeras operações - baseadas em numeros - mas, principalmente em processamento de grandes vetores (arrays) e matrizes.

import pandas as pd # biblioteca conhecida com ferramente-padrão para a estruturação de dados em "formato" de linha x coluna - tabela (Dataframe) - assim, podemos implementar porcessos de limpeza e agregação de dados de forma mais simples.

from scipy import stats # scipy é a biblioteca conhecida como "biblioteca cientifica" python. Dentre seus recursos, um dos famosos é stats; stats é composto por uma serie de recursos de uso estatistico, tais como: teste de hipostese, distribuições e funções estatisticas avançadas


# ==========================================
#  PASSO 2. DEFINIR O DATASET - CONJUNTO DE DADOS
# ==========================================

# a. definição do dataset e criação do dataframe: este dtaframe representa o tempo de execução de pipelines, em segundos. O dataframe possui um "travamento", se considerarmos o valor 500 - como o valor maximo que compõe a lista 
dados_pipeline = pd.DataFrame({
    'pipeline_id' : range(101, 111),
    'tempo_execucao_seg': [45, 48, 42, 47, 49, 51, 50, 46, 500, 48]
})

# b. exibir o df
print(dados_pipeline)

# ==========================================
#  PASSO 3. ANALISE METRICAS DESCRITIVAS
# ==========================================

print('------- A. Impacto dos outliers nas métricas descritivas ------------')
print()

# precisamos operar com nosso df e selecionar dados adequados
# nesta caso, nossa observancia será com os dados da coluna 'tempo_execucao_seg'
media = dados_pipeline['tempo_execucao_seg'].mean()
mediana = dados_pipeline['tempo_execucao_seg'].median()
desvio_padrao = dados_pipeline['tempo_execucao_seg'].std()

# agora, precisamos exibir os resultados obtidos 
print(f'Média: {media: .2f}s -> Enganosa! Neste caso, a média está sendo "puxada" pelo elemento outlier')
print(f'Mediana: {mediana: .2f}s -> Realista! Representaa rotina do sistema')
print(f'Desvio Padrão: {desvio_padrao: .2f}s -> Tende a indicar volatilidade. Neste caso, pode indicar uma altissima volatilidade!')



