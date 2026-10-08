'''
Neste algoritmo estamos observando ESPAÇOS VETORIAIS.  Esta é, portanto, uma DECOMPOSIÇÃO DIDÁTICA DE CADA UM DESTE PILARES - DE IA - ASSOCIANDO A TEORIA A CONCEITOS E APLICAÇÕES FUNDAMENTAIS E PRATICAS DE INTELIGENCIA ARTIFICIAL.
'''
# 0. importar os recursos necessarios
import numpy as np

# ===================================================
# 1. DEFINIR ALGUNS VETORES - 3 dimensões
# ===================================================
vetor_rei = np.array([0.50, 0.80, 0.12])
vetor_rainha = np.array([0.48, 0.82, 0.15])
vetor_carro = np.array([0.01, 0.05, 0.99])

# ===================================================
# 2. FUNÇÃO PARA CALCULO DE SIMILARIDADE DE COSSENO
# ===================================================

def cosine_similarity(u, v):
    # vamos definir 3 variaveis e o retorno da função 
    dot_product = np.dot(u, v)
    norm_u = np.linalg.norm(u)
    norm_v = np.linalg.norm(v)

    return dot_product / (norm_u * norm_v)

# criar duas variaveis que receberão como valor a similaridade dos cossenos
sim_rei_rainha = cosine_similarity(vetor_rei, vetor_rainha)
sim_rei_carro = cosine_similarity(vetor_rei, vetor_carro)

# exibir o valor das vars
print(f'Similaridade Cosseno (Rei, Rainha): {sim_rei_rainha: .4f}')
print(f'Similaridade Cosseno (Rei, Carro): {sim_rei_carro: .4f}')

# ===================================================
# 3. SIMULAÇÃO DE UM PASSO DE GRADIENT DESCENT
#    função de perda 
# ===================================================

w = 10.0 # peso inicial
learning_rate = 0.1

# ===================================================
# 4. LOOP PARA OBSERVAR A PERDA DO GRADIENTE
#    função de perda 
# ===================================================
print(f'\nPeso inicial (w): {w} ')
for passo in range(1, 6):
    gradiente = 2 * w
    w = w - learning_rate * gradiente
    erro = w**2
    print(f'Passo {passo}: Gradiente: {gradiente: .2f} | Novo Peso w = {w: .4f} | Perda: {erro: .4f}')


'''
          vetores                 matrizes                         distancia
TEXTO/DADO -------> REPRESENTAÇÃO ---------> PROCESSAMENTO EM MASSA----------> 

                 gradiente
COMPARAÇÃO/BUSCA ----------> APRENDIZADO DO MODELO   
'''