# ESTA SERÁ NOSSA APLICAÇÃO CLIENT - APLICAÇÃO PARA "CONSUMIR" A API

# passo 1. iniciamos pela importação das libs necessarias
import requests 
from pydantic import BaseModel, Field, ValidationError

# ======================================================
# A. DEFINIÇÃO DO CONTRATO DE DADOS (Data Contract)
# ======================================================

# aqui, definiremos o forma OBRIGATÓRIO do dado. Se a API mandar algo diferente, o pydantic irá rejeitar 
class CursoContrato(BaseModel):
    id: int
    titulo: str
    preco: float = Field(..., gt=0) # aqui, na instrução composta com Field indicamos que: ..., qualquer valor dever ser greater than (gt)um numero maior que zero (0)

# ======================================================
# B. CONSUMO DA API COM TRATAMENTO DE ERROS HTTP
# ======================================================

# URL_API = 'http://127.0.0.1:8000'
URL_API = 'http://127.0.0.1:8000/cursos'

print('Conectado à API. Extraindo dados....')

try: 
    # tentando fazer um pedido (requisição GET) ao servidor 
    resposta =  requests.get(URL_API, timeout = 5)

    # verficar se o codigo dde status - 200 ok - foi enviado. Se ocorrer algum erro, podemos ter os codigos 404, 500 isso significa que podemos ter uma exceção 
    resposta.raise_for_status()

    # conversão do "corpo" da resposta num lista de dicionarios python
    dados_brutos = resposta.json()
    print(f'Dados brutos recebidos da API: {dados_brutos}')

    # ======================================================
    # C. VALIDAÇÃO DOS DADOS "CONTRA" O CONTRATO
    # ======================================================    

    cursos_validados = []

    ## vamos definir um loop para iterar sobre cada item da variavel dados_brutos
    for item in dados_brutos:
        curso_validado = CursoContrato(**item) # aqui, estamos GERANDO O OBJETO A PARTIR DA CLASSE CursoContrato()
        # este objeto esta sendo gerando a partir da instanciação da classe: instanciação nada mais do que a inicialização da classe: inicializaçãod e uma classe nada mais do que "disponilizar os recursos descritos na classe para uso"; mas temos de tratar algo em especial: para gerar o objeto não executamos a classe pois UMA CLASSE É UM ELEMENTO DESCRITIVO. Precisamos, necessariamente, inicializar/executar seu método-construtor; neste caso, em nossa classe nãot emos nenhum metodo-constutor descrito, explicitamente, portanto, o ambiente de execução reconhece o uso implicito e o objeto é gerado.

        # **item: operador(Dictionary Unpacking): esta é instrução que irá "desempacotar" os pares chave: valor do dicionario que, aqui chegará, como argumentos para o parametro da classe  

        cursos_validados.append(curso_validado) # aqui, estamos acessando a nossa lista cursos_validados e adicionando, a partir do uso do função append() cada um dos itens, descompactados e atribuidos ao objeto curso_validado.

    print('\n SUCESSO: todos os dados passaram pela validação do "contrato"')

    # definir um novo loop: com o seguinte proposito -> iterar sobre o conjunto de dados validados e exibir seu resultado
    for c in cursos_validados:
        print(f'-[{c.id}] {c.titulo} -> R$ {c.preco}')

except requests.exceptions.RequestException as erro_http:
    print(f'Falha de Conexão ou Server Indisponivel: {erro_http}')

except ValidationError as erro_contrato:
    print(f'Quebra de contrato detectada!!! Os dados estão fora de padrão! {erro_contrato}')
