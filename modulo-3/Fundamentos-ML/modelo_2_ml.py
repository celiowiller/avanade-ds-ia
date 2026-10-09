# ESTE MODELO NOS DARÁ ALGUMAS METRICAS DE CLASSIFICAÇÃO 

# 1. importação dos recursos necessarios
from sklearn.metrics import(
    accuracy_score, precision_score, recall_score,
    f1_score, roc_auc_score, confusion_matrix, classification_report,
    mean_absolute_error,mean_squared_error,r2_score
)
import numpy as np

# importando o modelo ml para ser avaliado
from modelo_1_ml import pipeline_rf, X_test, y_test, Y_pred_rf

# 2. agora, vamos implementar a avalição do modelo que observamos anteriormente
y_probs_rf = pipeline_rf.predict_proba(X_test)[:, 1]

acc = accuracy_score(y_test, Y_pred_rf)
prec = precision_score(y_test, Y_pred_rf)
f1 = f1_score(y_test, Y_pred_rf)
rec = recall_score(y_test, Y_pred_rf)
auc = roc_auc_score(y_test, y_probs_rf)

# 3. exibir as metricas de avaliação 
print('======= MÉTRICAS DE CLASSIFICAÇÃO =======')
print(f'Acuracia: {acc: .4f}')
print(f'Precisão: {prec: .4f}')
print(f'F1-Score: {f1: .4f}')
print(f'Recall: {rec: .4f}')
print(f'ROC AUC: {auc: .4f}')

print('Matriz confusão:')
print(confusion_matrix(y_test, Y_pred_rf))

# 4. neste passo, definir simulações de Regressão
y_real_reg = np.array([100.0, 150.0, 200.0, 250.0, 300.0])
y_pred_reg = np.array([105.0, 142.0, 208.0, 240.0, 315.0])



# 5. metricas finais
mae = mean_absolute_error(y_real_reg, y_pred_reg)
rmse = np.sqrt(mean_squared_error(y_real_reg, y_pred_reg))
r2 = r2_score(y_real_reg, y_pred_reg)

# 6. exibindo as métricas finais
print('======= MÉTRICAS DE CLASSIFICAÇÃO - finais =======')
print(f'MAE: {mae: .2f}')
print(f'RMSE: {rmse: .2f}')
print(f'R²: {r2: .4f}')


'''
Em relação ao desempenho, do modelo, sobre classifição devemos observar as escala entre 0 e 1; onde: 1.0 representa perfeição e 0.0 falha miseravel!!!!

Acuracia:  0.9400 -> 94% o modelo acertou 94% de todas as previsões que fez - a partir do conjunto de testes (acertou ~188 de 200 amostras)

Precisão:  0.9556 -> quando o modelo previu que uma classe era, por exemplo, positiva(1) ele esta certo em 95,5% das vezes. Apenas 4 casos, aproximadamente, foram "alarmes-falsos"

Recall:  0.9149: o modelo conseguiu identificar/capturar 91,49% de todos os casos prositivos reais presentes na base

F1-Score:  0.9348: 93,49% a média harmonica entre Precisão  e o recall indica um modelo extremamente equilibrado, ou seja, sem qualquer vies para apenas uma classe.

ROC AUC:  0.9758: aqui, temos a saida sob uma curva ROC proxima de 1.0 - 97,60% - provando que o modelo possui uma capacidade excepcional de separa e distinguir a classe 0 da classe 1 em diferentes limiares de probabilidade

Matriz de confusão - Confusion Matrix

                        [[102   4]
                         [  8  86]]

102 (TN) Verdadeiros Negativos: eram classe 0 e o modelo previu 0 (acerto)
86  (TP) Verdadeiros Positivos: eram da classe 1 e o modelo previu 1(acerto)
4   (FP) Falso Positivo: eram da classe 0, mas o modelo classificou incorretamento como 1(Erro/"alarme falso")
8   (FN) Falso Negativo: eram da classe 1, mas o modelo calssificou incorretamente como 0(Erro/Omissão)

Total de acertos = 102 + 86 = 188 em 200amostras(188/200 = 0,94 ou seja 94%)

-----------------------------------------------------------------

MAE:  9.20 -> em média, as previsões do nosso modelo erraram por apenas 9,20 unidades para mais ou para menos em realçao ao valor real

RMSE:  9.78 -> este é o erro quadratico médio; indica que não há grandes outliers(erros discrepantes/valores gritantes)

R²:  0.9809 -> este é o coeficiente de determinação que indica que o modelo explica 98,1% da variação dos reais; Valores acima de 0.90 indicam um ajuste perfeito de reta de regressão dos dados
'''
