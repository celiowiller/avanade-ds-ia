# 1. importar os recursos necessarios para a implementação e funcionamento do codigo
import os # importanto o Operating System - permite que a aplicação possa interagir diretamente com o sistema operacional

import time # modulo nativo do python. oferece recursos para alidar com valores e parametros de tempo 

import logging # modulo nativo do python. Recurso padrão para a observação de eventos de log da aplicação 

import requests # modulo externo do python - requer instalação externa. Recurso muito usado para requisições HTTP

import pandas as pd # modulo externo do python - requer instalação externa. Recurso mais importante para manipulação limpeza e análise de dados


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
# FUNÇÃO PARA CONSUMO DE API COM PAGINAÇÃO 
# ===========================================================

def extrair_dados_api(url_base, max_paginas = 3):
    """
    realizar a extração paginada de dados de uma API REST ficticia com tratamento de erros e logging
    """

    # a. definir uma lista para receber dados
    todos_dados = []

    # b. definir um loop FOR para iterar sobre os dados e criar a paginação 
    for pagina in range(1, max_paginas + 1): # range(inicio, fim) 0,1,2 portanto ao adicionar +1 estamos garatindo que a ultima pagina desejada tambem iterada no loop 

        params = {'_page': pagina, '_limit': 10} # # estamos definindo para a API qual pagina está sendo solicitada. Tambem estamos definindo a qtde de registros retornados por pagina - 10 registros. 
        logging.info(f'Requisitando pagina {pagina} da API...') # aqui, o log da instrução 

        try:
            # definir uma var para receber como valor o recurso requests
            resposta = requests.get(url_base, params=params, timeout = 10)

            # tratamento das respostas disparando alguma exceção, caso ocorra
            resposta.raise_for_status()

            # definir uma nova var para receber, como valor, o arquivo json - caso tudo corra bem na requisição para a url_base
            dados = resposta.json()

            # agora, vamos verificar se a var dados realmente recebeu algum valor 
            if not dados:
                logging.warning('Pagina vazia recebida. Finalizando iteração!')
                break # aqui, caso nao tenhamos nenhum dado, o pipeline encerra seu trabalho

            # --------------------------------------------------------------------------------
            # agora, caso os dados sejam recebidos... vamos acessar a lista todos_dados
            todos_dados.extend(dados) # e "popula-la" com os valores atribuidos a var dados, declarada acima
            logging.info(f'Pagina {pagina} processada com sucesso. Registros até agora: {len(todos_dados)}')

            # "taxa" de requisição - tempo de "espera" para que as requisições sejam feitas (Rate Limit)
            time.sleep(1)

        except requests.exceptions.HTTPError as http_err:
            logging.error(f'Erro HTTP ocorrido ao acessar a página {pagina}: {http_err}')
            raise http_err
        except requests.exceptions.RequestException as req_err:
            logging.critical(f'Falha de conexão com a API: {req_err}')
            raise req_err
    return todos_dados

# ===========================================================
# PIPELINE DE CONVERSÃO DE FORMATOS (csv -> JSON -> PARQUET) 
# ===========================================================

# definir a função de fluxo de conversão 
def executar_pipeline_conversao():

    # a. vamos definir uma const para receber como valor uma URL publica com dados
    API_URL = 'https://jsonplaceholder.typicode.com/posts'
    DIRETORIO_SAIDA = 'data_lake' # aqui, estamos criando um 'data lake' para receber dados

    # b. vamos fazer do recurso os para criar o diretorio no nosso sistema operacional
    os.makedirs(DIRETORIO_SAIDA, exist_ok = True)

    # c. extração dos dados
    dados_brutos = extrair_dados_api(API_URL, max_paginas=3)

    # d. carregamento do DF com os dados extraidos - a partir da API
    df = pd.DataFrame(dados_brutos)
    logging.info(f'DataFrame criado com {df.shape[0]} linhas e {df.shape[1]} colunas.')

    # e. escrita no formato BRONZE (Json - dados semiestruturados)
    caminho_json = os.path.join(DIRETORIO_SAIDA, 'bronze_posts.json')
    df.to_json(caminho_json, orient='records', indent = 4)
    logging.info(f'Camada Bronze (JSON) salva em: {caminho_json}')

    # f. escrita no formato SILVER/GOLD (Parquet - Colunar e Compacto)
    caminho_parquet = os.path.join(DIRETORIO_SAIDA, 'silve_posts.parquet')
    df.to_parquet(caminho_parquet, engine = 'pyarrow', index = False, compression='snappy')
    logging.info(f'Camada Silver/Gold (Parquet otimizado) salva em : {caminho_parquet}')

    # g. comparação de tamanhos dos arquivos
    tamanho_json = os.path.getsize(caminho_json) / 1024
    tamanho_parquet = os.path.getsize(caminho_parquet) / 1024

    # h. Loggings
    logging.info(f'------- COMPARATIVO DE ARMAZENAMENTO ---------')
    logging.info(f'Tamanho do arquivo JSON: {tamanho_json: .2f} KB')
    logging.info(f'Tamanho do arquivo PARQUET: {tamanho_parquet: .2f} KB')
    logging.info(f'Redução de espaço: {( (tamanho_json - tamanho_parquet) / tamanho_json) * 100: .2f}%')

# executando o pipeline
if __name__ == "__main__":
    executar_pipeline_conversao()


