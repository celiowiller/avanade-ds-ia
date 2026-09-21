import pandas as pd
from src.transform import processar_vendas

if __name__ == "__main__":
    print('\n ==== PIPELINE DE DADOS - TECHSHOP ==== ')

# 1. Simulação do lote de vendas
    vendas_brutas = pd.DataFrame({
            'id_venda' : [101, 102],
            'cpf_cliente':['123.456.789-10', '987.654.321-11'],
            'email_cliente': ['cliente@mail.com', 'outro_cliente@mail.com'],
            'preco_original': [2000.00, 500.00]
        })
 # 2. 1ª execução do pipeline
    print('----------- Execução 1: Processamento inicial do dia ------------')
    vendas_tratadas = processar_vendas(vendas_brutas, percentual_desconto=0.10)
    print(vendas_tratadas[['id_venda', 'id_cliente_hash', 'preco_final', 'status_pipeline']])

# 3. 2ª execução do pipeline
    print('----------- Execução 1: Processamento inicial do dia ------------')
    vendas_reprocessadas = processar_vendas(vendas_tratadas, percentual_desconto=0.10)
    print(vendas_reprocessadas[['id_venda', 'id_cliente_hash', 'preco_final', 'status_pipeline']])
