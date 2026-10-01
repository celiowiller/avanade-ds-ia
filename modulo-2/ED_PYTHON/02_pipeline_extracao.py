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
    def __init__(self, diretorio_base = 'data_lake'): # aqui, o método especial __init__() é o construtor de classe Python

    # self: traduzindo livremente -> auto, "eu mesmo"; self é uma declaração de "auto-referencia"! é uma referencia explicita/direta ao proprio objeto (a instancia) que esta sendo/será executada naquele mesmo momento dentro da classe
        self.diretorio_base = diretorio_base
        self.caminho_bronze = os.path.join(diretorio_base)
        self.caminho_silver = os.path.join(diretorio_base, 'silver')
        self._inicializar_diretorios() # aqui, estamos chamando uma função que ainda vamos definir

    # b. definir a função a _inicializar_diretorios()
    def _inicializar_diretorios(self):
        # os.makedirs(self.caminho_bronze, exist_ok = True)
        os.makedirs(self.caminho_silver, exist_ok = True)

    # ===========================================================
    # TRANSFORMAÇÃO E LIMPEZA COM SUPORTE AO JSON E PARQUET
    # ===========================================================
    '''
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
    '''


    def transformar_e_carregar_silver(self, nome_arquivo_bronze):
        """
            Lê arquivos do data Lake (suporta .json ou .parquet), aplica regras de qualidade e salva o resultado idempotente na Silver
        """
        # a. log de informação do processamento
        logging.info(f'[SILVER] Processando arquivo: {nome_arquivo_bronze}')

        # b. definir uma var para receber como valor a junção dos paths que "apontam" para os dados 
        arquivo_bronze = os.path.join(self.caminho_bronze, nome_arquivo_bronze)

        # c. validação de existencia do arquivo no data Lake
        if not os.path.exists(arquivo_bronze):
            raise FileNotFoundError(f'Arquivo não encontrado no data lake Bronze: {arquivo_bronze}')

        # d. LEITURA DINAMICA: detecção do formato pela extensão do arquivo
        extensao = os.path.splitext(nome_arquivo_bronze)[1].lower()
         # verificar a extensão 
        if extensao == '.json':
            logging.info('[SILVER]Executando leitor nativo pd.read_json....')
            df_bronze = pd.read_json(arquivo_bronze)
        elif extensao == '.parquet':
            logging.info('[SILVER] Executando leitor nativo pd.read_parquet...')
            df_bronze = pd.read_parquet(arquivo_bronze)
        else:
            raise ValueError(f'Formato não suportado: {extensao}. Use -.json ou .parquet!')

        # e. TRANSFORMAÇÃO E LIMPEZA DE DADOS (Qualidade)

        # identificar a pk - caso exista - disponivel (id ou id_venda...)
        coluna_pk = 'id' if 'id' in df_bronze.columns else 'id_venda'

        # deduplicação(exclusão de dados duplicados) baseada na PK identificada
        df_silver = df_bronze.drop_duplicates(subset = [coluna_pk], keep = 'last')

        # Tratamento/padronização baseado numa condição 
        if 'title' in df_silver.columns:
            df_silver['title'] = df_silver['title'].str.upper()

        # adicionar metadado de auditoria/data de transformação 
        df_silver['data_processamento_silver'] = datetime.now()
               

        # f. GRAVAÇÃO IDEMPOTENTE NA SILVER (Sempre em parquet otimizado)
        nome_saida = f'silver_{os.path.splitext(nome_arquivo_bronze)[0]}.parquet'
        arquivo_silver = os.path.join(self.caminho_silver, nome_saida)

        df_silver.to_parquet(arquivo_silver, engine = 'pyarrow', index = False, compression='snappy')

        return df_silver

# ===========================================================
# EXECUÇÃO DO PIPELINE A PARTIR DE AMBOS OS FORMATOS
# ===========================================================
if __name__ == '__main__':
    pipeline = PipelineExtracaoDados(diretorio_base='data_lake') # objeto gerado a partir da classe

    # EXECUÇÃO 1: lendo o arquivo JSON - guardado no data lake
    logging.info('=== EXECUÇÃO 1. Processando Bronze JSON ===')
    df_json = pipeline.transformar_e_carregar_silver('bronze_posts.json')
    print(df_json[['id', 'title']].head(3))


    # EXECUÇÃO 2: lendo o arquivo PARQUET - guardado no data lake
    if os.path.exists('data_lake/silve_posts.parquet'):
         logging.info('=== EXECUÇÃO 2. Processando Bronze PARQUET ===')
         df_parquet = pipeline.transformar_e_carregar_silver('silve_posts.parquet')
         print(df_parquet[['id', 'title']].head(3))



