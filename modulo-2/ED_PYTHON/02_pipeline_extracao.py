# 1. importar os recursos necessarios 
import os
import logging
import pandas as pd
from datetime import datetime

# ===========================================================
# CONFIGURAÇÃO DE LOGGING ESTRUTURADO (BOAS PRATICAS)
# ===========================================================

logging.basicConfig(
    level = logging.INFO,
    format  = '%(asctime)s [%(levelname)s] %(message)s',
    handlers = [
        logging.StreamHandler()
    ]
)


# ===========================================================
# DEFINIÇÃO DA CLASSE APRA EXTRAÇÃO DOS DADOS
# ===========================================================

class PipelineExtracaoDados:
    # a. definir o construtor, de forma explicita, da classe
    def __init__(self, diretorio_base = 'lakehouse'): # aqui, o método especial __init__() é o construtor de classe Python

    # self: traduzindo livremente -> auto, "eu mesmo"; self é uma declaração de "auto-referencia"! é uma referencia explicita/direta ao proprio objeto (a instancia) que esta sendo/será executada naquele mesmo momento dentro da classe
        self.diretorio_base = diretorio_base
        self.caminho_bronze = os.path.join(diretorio_base, 'bronze')
        self.caminho_silver = os.path.join(diretorio_base, 'silver')
        self._inicializar_diretorios() # aqui, estamos chamando uma função que ainda vamos definir

    # b. definir a função a _inicializar_diretorios()
    def _inicializar_diretorios(self):
        os.makedirs(self.caminho_bronze, exist_ok = True)
        os.makedirs(self.caminho_silver, exist_ok = True)

    # ===========================================================
    # EXTRAÇÃO E CARGA BRUTA (BRONZE)
    # ===========================================================
    def extrair_e_carregar_bronze(self, data_referencia, dados_simulados):
        """
            garantir a Idempotencia na Bronze: sobrescreve o arquivo especifico da data
        """
        logging.info(f'[BRONZE] Iniciando ingestão para data: {data_referencia}')

        # definir o nosso df
        df_bruto = pd.DataFrame(dados_simulados)
        df_bruto['data_ingestao'] = datetime.now()

        # obsevar o nome unico por participação de data
        arquivo_saida = os.path.join(self.caminho_bronze, f'vendas_{data_referencia}.parquet')

        # transformar o df_bruto para parquet
        df_bruto.to_parquet(arquivo_saida, index = False)
        logging.info(f'[BRONZE] Dados gravados com sucesso em: {arquivo_saida}')
