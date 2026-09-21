# arquivo/modulo que implementa as regras de negocio do projeto e, tambem, o contexto de Idempotência(significa que: caso o sistema sofra algum tipo de instabilidade, o proprio pode, ao ser reestabelecido, cometer algum. Portanto, aqui, podemos previnir este cenario)

# importação das bibliotecas
import logging
import pandas as pd
from src.security import anonimizar_cpf, criptografar_email

# definir a configuração de logs - tambem poderiamos usar prints() comuns. Mas, neste ponto, é interessante tomarmos contato com recursos masi avançados

logging.basicConfig(level = logging.INFO, format = '%(asctime)s - [%(levelname)s] - %(message)s')
logger = logging.getLogger('TechDados_Logger')

# neste passo, vamos definir uma função que tem como proposito: fazer todo o processamento dos dados de vendas do e-commerce
def processar_vendas(df: pd.DataFrame, percentual_desconto: float) -> pd.DataFrame:
    """
        esta é uma docstring: esta função processa o lote de vendas aplicando segurança (LGPD), calculando descontos e garantindo Idempotencia na execução
    """

    logger.info('Iniciando o processamento de lote de vendas...')

    # validação de segurança - considerando os parametros da função 
    if df.empty:
        logger.warning('Dataframe recebido e vazio. Processamento cancelado')
        # caso o contrario ocorra...
        return df # o df "populado" fica disponivel para as operações 

    if percentual_desconto < 0 or percentual_desconto > 1:
        raise ValueError('O percentual  de desconto deve estar entre 0.0 e 1.0')

    # neste passo, vamos fazer uma cópia do df gerado e manipular/analisar/explorar esta copia 
    df_copia = df.copy()

    # 1. MECANISMO DE IDEMPOTENCIA
    # aqui, estamos implementando o seguinte: se a coluna 'status_pipeline' ja for concluida e os dados ja foram processados; podemos concluir a etapa de processamento dos dados brutos foi finalizada
    # Portanto, podemos retornar o Dataframe sem reaplicar o desconto para evitar distorções nos preços
    if 'status_pipeline' in df_copia.columns and (df_copia['status_pipeline'] == 'CONCLUIDO').all():
        logger.info('Garantindo a Idempotencia: dados ja foram processados anteriormente.')
        return df_copia


    # 2. MECANISMO DE GOVERNANÇA E LGPD(Anonimização e Criptografia)
    logger.info('Aplicando proteção de hashing no CPF e criptografia no email')
    df_copia['id_cliente_hash'] = df_copia['cpf_cliente'].apply(anonimizar_cpf)
    df_copia['email_criptografado'] = df_copia['email_cliente'].apply(criptografar_email)

    # 3. IMPLEMENTAÇÃO DA REGRA DE NEGOCIO (aqui, a principal regra de negocio é: a aplicação do desconto no preço dos produtos)
    logger.info(f'Aplicando desconto de {percentual_desconto * 100}% nos preços originais')
    # nossa operação de aplicação do desconto
    df_copia['preco_final'] = (df_copia['preco_original'] * (1 - percentual_desconto)).round(2)

    # 4. MINIMIZAÇÃO DE DADOS & MARCAÇÃO DE ESTADO   
    # aqui, vamos remover as colunas de texto lipos e sensivies antes de salvar 
    df_copia = df_copia.drop(columns = ['cpf_cliente', 'email_cliente'])
    df_copia['status_pipeline'] = 'CONCLUIDO' 

    logger.info('Lote processado com sucesso...')
    return df_copia

