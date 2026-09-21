# arquivo que será composto pelo conjunto (suite) de testes unitarios e automatizados aplicados ao pipeline.

# recursos necessarios para o funcionamento dos testes
import pytest
import pandas as pd
from src.transform import processar_vendas

# 1º teste: definir a função irá testar o calculo do desconto]
def test_calculo_desconto_e_remocao_pii():
    """ testar se o desconto de 10% é aplicado aos preços e se os dados PII(Personally Identifiable Information) foram removidos"""
    dados_entrada = pd.DataFrame({
        'cpf_cliente':['123.456.789-10'],
        'email_cliente': ['cliente@mail.com'],
        'preco_original': [100.0]
    })

    # defini uma nova var para receber como valor a chamada da função processar_vendas()
    resultado = processar_vendas(dados_entrada, 0.10)

    # validação 1: o valor de R$ 100,00 com 10% de desconto deve ser, exatamente R$ 90,00 
    assert resultado['preco_final'].iloc[0] == 90.0

    # validação 2: aqui, vamos observar as colunas 'cpf_cliente' e 'email_cliente'; estas colunas NÃO PODEM CONSTAR do df
    assert 'cpf_cliente' not in resultado.columns
    assert 'email_cliente' not in resultado.columns 

# 2º teste: agora, vamos testar a idempotencia e a duplicação de desconto
def test_idempotencia_nao_duplica_desconto():
    """ garantindo que o pipeline, ao rodar sucessivamente, não aplica sucessivos descontos"""
    dados_entrada = pd.DataFrame({
            'cpf_cliente':['123.456.789-10'],
            'email_cliente': ['cliente@mail.com'],
            'preco_original': [100.0]
        })

    # 1ª execução: lote 1
    execucao_1 = processar_vendas(dados_entrada, 0.10)

    # 2ª execução: lote 2 - com lote 1
    execucao_2 = processar_vendas(execucao_1, 0.10)

    # o valor final DEVE permanecer 90,00 e não sofrer novo desconto
    assert execucao_2['preco_final'].iloc[0] == 90.00

