# 1. importações de recursos necessarios
import numpy as np
import re # este é o recurso necessario para fazer uso de expressões regulares me python
from typing import List, Dict, Tuple


# 2. implementar a classe que irá operar como um elemento recursivo 
class RecursiveChuncker:
    # definir o método construtor da classe
    # aqui, estamos definindo o tamanho maximo de caracteres por chunk -> chunk_size = 200
    # overlap: int = 40: definir a qtde de sobreposição de caracteres
    def __init__(self, chunk_size: int = 200, overlap: int = 40):
        self.chunk_size = chunk_size
        self.overlap = overlap

    # definir o método quer receberá uma string/texto e poderá dividi-lo em pedaços
    def split_text(self, text: str) -> List[str]: # ponto de entrada do fatiamento

        # vamos definir os separadores por ordem de priopridade semantica
        separators = ["\n\n", "\n", ". ", " "] # aqui, definimos a prioridade das quebras de linha/texto: 

        # 1 - primeiro, tentamos quebrar por quebra de paragrafo: "\n\n"
        # 2 - depois, tentamos quebrar por linha: \n 
        # 3 - depois, ainda, por frase - quem nos da esta indicação é o uso do . (ponto)
        # 4 - e, por fim, tentamos quebrar por palavra: quem nos da esta indicação é a string vazia -> " "

        return self._recursive_split(text, separators) # aqui, estamos retornando o resultado do private method (metodo privado)

    def _recursive_split(self, text: str, separators: List[str]) -> List[str]:
        # vamos definir uma lista
        chuncks = []

        # verificar se o parametro text - pertencente ao metodo - recebeu algum valor de argumento
        if len(text) <= self.chunk_size: # caso o texto ja for menor/igual  ao tamanho maximo então queremos que os espaços "das pontas" sejam removidos e, então, possamos retorna-lo numa lista - com os dados tratados
            return [text.strip()]

        # aaqui, abaixo, usamos a var sep para "pegar" o primeiro separador da list; caso a lista esteja vazia , usamos a string vazia
        sep = separators[0] if separators else ""
        splits = text.split(sep) if sep else list(text) # caso haja um separador , dividimos o texto numa lista de caracteres individuais

        # neste passo, vamos definir uma propriedade que, incialmente, recebe uma string vazia e, tambem, vamos definir um loop para iterar sobre a var splits
        current_chunk = '' # esta é a propriedade que irá acumular os valores dos "pedaços" do nosso texto

        for s in splits: # agora, o loop - com a var s - percorre todos os elementos atribuidos a var splits
            item = s + (sep if sep != " " else " ") # aqui, estamos reanexando o separador ao "pedaço atual" com o objetivo de preservar a formatação original

            if len(current_chunk) + len(item) <= self.chunk_size:
                current_chunk += item # current_chunk = current_chunk + item: aqui estamos verificando se o item adicionado ultrapassa o limite maximo de caracteres definidos para chunk_size

            else: # caso o contrario ocorra
                # abaixo, estamos garatindo que o ultimo pedaço restante tqmbem seja salvo apos o termino do loop
                if current_chunk: # salvamos current_chunk atual na lista de chuncks(com strip()) e iniciamos um novo current_chunk contendo o item atual.
                    chuncks.append(current_chunk.strip())
                current_chunk = item

        if current_chunk:
            chuncks.append(current_chunk.strip())

        return [c for c in chuncks if c] # aqui, estamos retornando a lista de chuncks(pedaços) ignorando enventuais pontuações/strings vazias (if c)

#  2.1 uma nova função que irá atuar   como um simulador de vetorização com hashing;  portanto, esta função simula o comportamento de modelo embendding (ex.: OpenAI) pois gera vetores numericos deterministicos
def generate_mock_embedding(text: str, dim: int = 128) -> np.ndarray:
        """ esta função irá gerar um veotr normalizado de dimensão 'dim' a aprtir do rash de texto"""
        np.random.seed(abs(hash(text)) % (2**32)) # este é o hash do texto como - dado inicial "semente randomica" - para que o mesmo texto sempre gere exatamente o mesmo valor.

        vec = np.random. randn(dim) # aqui, estamos criando um vetor aleatorio com numeros sob distribuição normal  de dimendsão -dim - (128 dimensoes por padrão)

        return vec / np.linalg.norm(vec) #aqui, aplicamos a normalização dividindo o vetor pelo seu comprimento . Essa aplicação trasnformará o vetor num vetor unitário (comprimento 1); essa transformação tambem simplicará o calculo da similaridade de cosseno.

# 3. definir o vector database e a engine de retenção (retrieval); portanto, esta classe será responsavel por armazenar os textos, guardar seus vetores(embeddings) e realizar buscas por similaridade
class VectorStore:
    # 3.1. definir o metodo construtor da classe
    def __init__(self):
        self.documents: List[str] = [] # listas vazias par armazenar os trechos de textos originais
        self.embeddings: List[np.ndarray] = [] # lista vazia para armazenar os vetores numéricos associados a cada documento na mesma ordem de indice 

    # 3.2. aqui, vamos definir o método que tentará inserir texto nos documentos; ou seja, inserir textos para indexação 
    def add_texts(self, texts: List[str]):
        for t in texts: # aqui, percorremos cada string presente na lista recebida pelo parametro
            self.documents.append(t) # adicionamos o texto bruto na lsita de documentos 
            self.embeddings.append(generate_mock_embedding(t)) # geramos o vetor de texto chamando a função simuladora para armazenar o embedding correspondente

    # 3.3. definir uma função para realizar buscas; aqui, o método recebe uma "pergunta" do usuario - no parametro query - e a quantidade de resultados desejados - top_k: int = 2 - E, na sequencia, retorna uma lista de tuplas conteudo o texto e a pontuação referente à ele 
    def search(self, query:str,  top_k: int = 2) -> List[Tuple[str, float]]:

        query_vec = generate_mock_embedding(query) # neste passo, vetorizamos a pergunta do usuario para permitir a comparação matematica do espaço vetorial

        scores = [] # aqui, criamos a lista vazia para guardar a pontuação de relevancia de cada documento

        # definir um loop para observar a similaridade de cossenos
        for doc, doc_vec in zip(self.documents, self.embeddings):
            sim = np.dot(query_vec, doc_vec) # aqui, estamos calculando o produto escalar entre o vetor da pergunta e o vetor do documento. Ambos foram, previamente, normalizados; portanto, o produto escalar é, necessariamente, a similaridade de cossenos.

            scores.append((doc, float(sim)))
        # 3.4. agora, vamos fazer a ordenção decrescente dos valores pela pontuação de similaridade
        scores.sort(key = lambda x: x[1], reverse = True)
        return scores[:top_k]

    
#-------------------------------------------------------------------------
# 3.5. função para simular a resposta do LLM
def generate_response_from_context(context_str: str, pergunta: str) -> str:
    """ função que irá extrair o contexto das linhas relevantes para responder a pergunta """
    palavras_chave = [p.lower() for p in pergunta.split() if len(p) > 3]
    linhas = context_str.split("\n")
    melhores_linhas = []

    # definir o loop para iterar sobre o valor da propriedade linhas
    for linha in linhas:
        if any(p in linha.lower() for p in palavras_chave):
            melhores_linhas.append(linha.strip())

    if melhores_linhas:
        return "\n".join(melhores_linhas)
    return "Dado não encontrado"
#-------------------------------------------------------------------------


# 4. Pipeline Completo de RAG com verificação de Ancoragem (grouding)
def rag_pipeline_execution(documento_bruto: str, pergunta: str) -> Dict:

    # passo A. Chunking
    chunker = RecursiveChuncker(chunk_size=150, overlap=20)
    chunks = chunker.split_text(documento_bruto)
    
    # passo B. Indexação Vetorial
    vector_db = VectorStore()
    vector_db.add_texts(chunks)

    # passo C. Retenção - Retrieval
    retrieved_context = vector_db.search(pergunta, top_k=2)
    context_str = "\n".join([doc for doc, score in retrieved_context])    

    # passo D. Geração de um prompt Estruturado (Grounding - Ancoragem Estrita)
    augmented_prompt = f""" [SISTEMA: Responda APENAS  com base no contexto fornecido. Se a resposta não estiver explicita, responda: 'Dado não encontrado no contexto'] 

        
    --- CONTEXTO ---
    {context_str}

    --- PERGUNTA ---
    {pergunta}
    """

    # passo E. extração da resposta, simulada, do LLM
    resposta = generate_response_from_context(context_str, pergunta)

   
    return {
        "chunks_gerados": len(chunks),
        "contexto_recuperado": retrieved_context,
        "prompt_enviado_ao_llm": augmented_prompt,
        "resposta_final" : resposta
    }

# ---  TESTE DE EXECUÇÃO ---
documento_tecnico = """
A arquitetura de microsserviços da plataforma utiliza Kubernetes para orquestração de contêineres.
O banco de dados principal é o PostgreSQL hospedado no Amazon RDS com replicação multi-AZ.
Para caching de alto desempenho, adotamos o Redis Cluster com tempo de expiração padrão de 15 minutos.
Os logs de auditoria são armazenados no Amazon S3 e retidos por 5 anos por motivos de compliance LGPD.
"""

resultado = rag_pipeline_execution(documento_tecnico, 'Qual é o banco de dados principal e onde ele está hospedado?')

print('====== RESULTADO DO PIPELINE RAG =====')
print(f'Chunks criados: {resultado['chunks_gerados']}')
print( '\nTop Chunks Recuperados:')

for doc, score in resultado['contexto_recuperado']:
    print(f' - [Score: {score: .4f}] {doc}')

print('\nPrompt Final gerado para o LLM:')
print(resultado['prompt_enviado_ao_llm'])

print('====== RESPOSTA FINAL - LLM SIMULADO =====')
print(resultado['resposta_final'])



