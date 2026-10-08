# OBSERVAR E IMPLEMENTAR CALCULOS ESTATISTICOS COM PYTHON

# 1. importar os recursos necessarios
import numpy as np # lib numerica 
import scipy.stats as stats # lib estatistica do python
import matplotlib.pyplot as plt # impressão de imagens

# 2. configuração ds dados seed() - "sementes/primeiros dados" para que seja implementar reproducibilidade
np.random.seed(42) # estamos, aqui, fixando o gerador de numeros aleatorios. Dessa forma conseguimos garantir que sempre que o codigo for executado os mesmos numeros "aleatorios" sejam gerados. Isso é importante pois torna o experimento "reporduzivel" em qualquer cricunstancia.

# 3. geração de duas amostras(tempo de resposta de dois modelos em milissegundos)
modelo_A = np.random.normal(loc = 120, scale = 15, size = 100) # Média = 120ms
modelo_B =  np.random.normal(loc = 112, scale = 15, size = 100) # Media = 112ms

'''
acima, temos o uso da distribuição NORMAL(GAUSSIANA)  para simular o tempo de resposta dos modelos; 
modelo_A: loc=120 -> é a média da distribuição em ms
          scale=15 -> o desvio padrão  é 15
          size=100 -> é o recurso que gera uma amostra com 100 observações 
120 +- 15 -> 120 + 15  = 135
          -> 120 - 15  = 105
'''

# 4. Teste de hipotese: t-test para duas amostras independentes
# H0: A latencia media do Modelo A e do modelo B é IGUAL.
# H1: A latencia media dos modelos é estatisticamente DIFERENTE.
t_stat, p_value = stats.ttest_ind(modelo_A, modelo_B)

# exibindo valores 
print(f'Estatistica t: {t_stat: .4f}')
print(f'p-valor: {p_value: 4e}')

# agora, vamos colocar a percentagem de erro 
alpha = 0.05

# regra de decisão 
if p_value < alpha:
    # p_value = 0.000002
    print('Conclusão: Rejeitamos a H0. A diferença de latencia entre os modelos está estatisticamente significativa. ')
else: 
    # p_value = 0.15 (> 0.05)
    print('Conclusão: Não evidencia suficiente para rejeitar a H0. A diferença pode ser fruto do acaso.')

# 5. Visualização das distribuições 
plt.figure(figsize = (10, 5))
plt.hist(modelo_A, alpha = 0.6, label = 'Modelo A (Média: ~120ms)', color = 'crimson', bins = 15)
plt.hist(modelo_B, alpha = 0.6, label = 'Modelo B (Média: ~112ms)', color = 'royalblue', bins = 15)

plt.axvline(np.mean(modelo_A), color = 'darkred', linestyle = 'dashed', linewidth = 2)
plt.axvline(np.mean(modelo_B), color = 'navy', linestyle = 'dashed', linewidth = 2)
plt.title('Comparação da Latencia de resposta entre modelos de IA')

plt.xlabel('Latencia em ms')
plt.ylabel('Frequencia')

plt.legend()
plt.grid(True, linestyle = '--', alpha = 0.5)
plt.show()
