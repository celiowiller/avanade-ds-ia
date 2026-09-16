'''
requests: biblioteca - client - para aplicações que fazem requisições HTTP para Web APIs

fastapi: framework leve e rapido para a contrução de Web APIs

uvicorn: este é um recurso/biblioteca que nos daá a possibilidade de "construir" um servidor web para colocar  a API "no ar"/funcionando

pydantic: recurso-garantidor da qualidade do formato do arquivo JSON recebido nas requisições
'''

# ESTE ARQUIVO SERÁ NOSSA API: aqui, vamos observar de onde vem o dado - esta será uma API local

# passo 1. fazer as importações da libs necessarias
from fastapi import FastAPI # aqui, estamos "trazendo" para dentro do nosso programa os recursos necessarios para que tudo funcione plenamente. Neste caso, o recurso que acabamos de importar pertence a instalação da biblioteca fastapi - que instalamos a pouco

from pydantic import BaseModel # este é o recurso - BaseModel -  que, quando usado, vai observar o formato do padrão para garantir que os dados sejam "empacotados" corretamente.

# passo 2. vamos definir uma variavel que receberá com valor a inicialização do recurso FastAPI
app = FastAPI(title = 'API Versão 1')

# passo 3. definir a estrutura do pacote de dados (modelo json que deve ser observado e obedecido)
class Curso(BaseModel):  # uso da palavra reservada class para definir uma classe, em Python.
    id: int           # isto é uma variavel: que, pelo fato de compor um classe, ganha uma nova nomenclatura: ATRIBUTO
    titulo: str
    preco: float

# passo 4. definição de uma base - simulada. em tempod e execução - dados para as operações 
# para este propotio vamos criar uma lista composta por alguns dicionarios 
BANCO_DADOS = [
    {'id': 1, 'titulo': 'Fundamentos de python', 'preco': 153.89},
    {'id': 2, 'titulo': 'Introdução ao SQL', 'preco': 289.56},
    {'id': 3, 'titulo': 'Scrum Master', 'preco': 100.99}
]

# passo 5. neste passo, vamos definir a "rota"/ endpoint raiz da nossa API

# ESTA FUNÇÃO CRIA UM "PONTO DE ACESSO"(ENDPOINT) NAQUILO QUE VAMOS CHAMAR DE "ENDEREÇO" PRINCIPAL DA APLICAÇÃO QUE PODERIAMOS  ACESSAR COM ESTE EXEMPLO: http://localhost:8080/

@app.get('/') # uso do decorator (decorador) que possui o seguinte proposito: "escutar" requisições HTTP GET para a rota principal da aplicação - representado pela / (barra)
def mensagem_boas_vindas():
    return {'mensagem': 'API no ar com sucesso!'} # retorno da função no formato JSON

# passo 6. definir a rota GET: esta rota, quando acessada irá retornar a listagem completa dos cursos
# ESTA FUNÇÃO CRIA UM "PONTO DE ACESSO"(ENDPOINT) NAQUILO QUE VAMOS CHAMAR DE "ENDEREÇO" ESPECIFICO DA APLICAÇÃO QUE PODERIAMOS  ACESSAR COM ESTE EXEMPLO: http://localhost:8080/cursos
@app.get('/cursos')
def listar_cursos():
    return BANCO_DADOS



