--======================================================
-- EXERCICIO DE NORMALIZAÇÃO DE DB (3FN)
-- Empresa: LogiTech Solutions
-- Ferramenta: VSCode / Ambiente: SQL SERVER
-- Tema: Estrutura DDL e Normalização ... Cardinalidade
--======================================================

--======================================================
-- PASSO 1: CRIAÇÃO DO DB
--======================================================
-- CREATE DATABASE LogiTechDB 

USE LogiTechDB
GO

-- 1.1 Tabela Cadastral: Clientes
-- 1ª leitura de Cardinalidade: (Clientes <---> Vendas): (0, N) = N
-- 1ª leitura de Cardinalidade: (Vendas <---> Clientes): (1, 1)

-- Cardinalidade resultante: 1:N
CREATE TABLE Clientes(
    ID_Cliente INT IDENTITY(1, 1) PRIMARY KEY,
    Nome_Cliente VARCHAR(100) NOT NULL,
    Cidade_Cliente VARCHAR(50) NOT NULL,
    Estado_Cliente CHAR(2) NOT NULL
)

-- 1.2 Tabela Cadastral: Vendedores

-- 2ª leitura de Cardinalidade: Vendas <--> Vendedores -> (Vendas <---> Vendedores): (1, 1) = 1
-- 2ª leitura de Cardinalidade: Vendedores <--> Vendas -> (Vendedores <---> Vendas): (0, N) = N

-- Cardinalidade Resultante: 1:N
CREATE TABLE Vendedores(
    ID_Vendedor INT IDENTITY(1, 1) PRIMARY KEY,
    Nome_Vendedor VARCHAR(100) NOT NULL,
    Filial_Vendedor VARCHAR(50) NOT NULL
)

-- 1.3 Tabela Cadastral: Produtos
CREATE TABLE Produtos(
    -- 1. Coluna numerica sequencial que, vamos assumir, ficará "oculta"
    ID_Produto INT IDENTITY(1, 1),

    -- 2. Coluna que usa a operação de automação de geração do Cod_Produto como PK "automatizado"
    -- portanto, a partir da operação, abaixo, vamor gerar a seguinte sequencia de codigo: 'P01', 'P02',....
    --Cod_Produto AS CAST('P' + RIGHT('00' + CAST(ID_Produto AS VARCHAR(10)), 2) AS VARCHAR(10)) PERSISTED PRIMARY KEY,
    --Cod_Produto AS CAST('P' + RIGHT('0000' + CAST(ID_Produto AS VARCHAR(10)), 4) AS VARCHAR(10)) PERSISTED PRIMARY KEY,
    --Cod_Produto AS CAST('P' + FORMAT(ID_Produto, '0000')) AS VARCHAR(10)) PERSISTED PRIMARY KEY,
    Cod_Produto AS CAST('P' + REPLACE(STR(ID_Produto, 4), ' ', '0') AS VARCHAR(10)) PERSISTED PRIMARY KEY,
    Nome_Produto VARCHAR(100) NOT NULL,
    Categoria VARCHAR(50) NOT NULL,
    Preco_Unitario DECIMAL(10, 2) NOT NULL
)

-- 1.4 Tabela Transacional: Vendas

-- 1ª leitura de Cardinalidade: (Vendas <---> Clientes): (1, 1) 
-- 1ª leitura de Cardinalidade: (Clientes <---> Vendas): (0, N) = N 

-- agora, precisamos de uma cardinalidade resultante -->  1:N
-- 1ª leitura de Cardinalidade: a cardinalidade resultante é *** composta pelo valor minimo e maximo de cardinalidade observadas nas "pontas" e, extraimos os valores maximos;

-- COMO OBTEMOS A CARDINALIDADE RESULTANTE: Juntamos apenas os valores maximos observados nas duas "pontas":

--   Maximo de Clientes -> Vendas = N
--   Maximo de Vendas -> Clientes = 1
-- quando combinamos os dois valores maximos (1 e N), o relacionamento é classificado como 1:N (Um para Muitos)

CREATE TABLE Vendas(
    ID_Venda INT IDENTITY(1, 1) PRIMARY KEY,
    Data_Venda DATE NOT NULL,
    ID_Cliente INT NOT NULL,
    ID_Vendedor INT NOT NULL, 
    CONSTRAINT FK_Vendas_Clientes FOREIGN KEY(ID_Cliente) REFERENCES Clientes(ID_Cliente),
    CONSTRAINT FK_Vendas_Vendedores FOREIGN KEY(ID_Vendedor) REFERENCES Vendedores(ID_Vendedor) 
)

-- 1.5 Tabela do relacionamento Intermediario: Itens_Venda
-- em função de obtermos uma cardinalidade N:N entre Produtos e Vendas - criamos uma table Associativa -> Itens_Venda; assim, resolvemos o contexot das relação indireta entre as dua tables.
CREATE TABLE Itens_Venda(

    ID_Venda INT NOT NULL,
    Cod_Produto VARCHAR(10) NOT NULL,
    Quantidade INT NOT NULL,
    Preco_Praticado DECIMAL(10, 2) NOT NULL,
    CONSTRAINT PK_Itens_Venda PRIMARY KEY (ID_Venda, Cod_Produto),
    CONSTRAINT FK_Itens_Vendidos FOREIGN KEY(ID_Venda) REFERENCES Vendas(ID_Venda),
    CONSTRAINT FK_Itens_Produtos FOREIGN KEY(Cod_Produto) REFERENCES Produtos(Cod_Produto)
)

--  Cod_Produto : nome da coluna que estamos criando
-- AS (...): definição que esta é uma coluna calculada
-- PERSISTED: indicação de que o valor desta coluna será fisicamente no disco
-- PRIMARY KEY: definiç~´ao da chave primaria

-- CAST('P' + RIGHT(...) AS VARCHAR): 

-- 1. CAST(ID_Produto AS VARCHAR(10)): aqui, neste pedaço da formula estamos fazendo uma conversão; convertendo a coluna  ID_Produto (numérica) para o formato de texto(VARCHAR(10)); fazemos isto pois, no SQL, juntar um numero e um texto é impossivel.

-- 2. '00' + CAST(...): aqui, estamos adicionando dois zeros junto do numero convertido; se o ID for 1 -> '001'

-- 3. RIGHT('00' + ....., 2): extraindo apenas OS 2 ULTIMOS CARACTERES A DIREITA DA STRING RESULTANTE. É AQUI QUE OS ZEROS À ESQUERDA DO NUMERO SÃO FORMATADOS COM TAMANHO FIXO ADEQUADO. Exemplo: acima, temos a saida prevista: '001'
-- 'pegar' somente os DOIS ULTIMOS ELEMENTOS DE SAIDA: '001' -> '01' === 'P01'; **** ESTA LÓGICA FUNCIONA PARA IDs INCREMENTAIS ATÉ O NUMERO 99. QUANDO O ID FOR 100 -> DEVERIAMOS TER ALGO PARECIDO COM ISTO == '00100'; MAS TEMOS A NOSSA REGRA, PORTANTO TEREMOS O SEGUINTE RESULTADO: '00'

-- 4. 'P'+ RIGHT(...):  aqui, estamos juntando a letra 'P' com o reusltado formatado de 2 digitos. Nossa saida, formatada, será: 1 -> '001' -> '01' == 'P' + '01' -> 'P01'

-- 5. CAST('P' + ... AS VARHCAR(10)): aqui, temos a conversão de todo o textos final resultante para o tipo de dado VARCHAR(10) de forma explicita. Portanto, estamos garantindo que a coluna Cod_Produto tenha um tipo de dado claro e definido e esperado para o DB.

-- 6. REPLACE(STR(ID_Produto, 4), ' ', '0'): aqui, estamos usando a funçãio REPLACE() para 'converter' o valor numerico em algum outro formato; 
-- 6.1: STR(ID_Produto, 4): aqui, temos o processo de conversão; o ID_produto - numérico - se torna uma string com o uso da função STR(); o valor 4 determina a quantidade de caracteres desejados;

-- 6.2: ' ', '0': temos um espaço vazio ( ' ' ) -> portanto, a função REPLACE ir´pa 'varrer' este espaço fazendo a contagem dos caracteres; por exemplo: ID_Produto == 1 -> teremos: '   1' tres espaços vazios e o quarto espaçoi ocupado pelo numero 1 e, assim, sucessivamente. Mas, temos a função REPLACE com outro parametro: '0'; significa que a saida anterior: '   1' será, na verdade, -> '0001'





-- ANALISE DE CARDINALIDADE Produtos <--> Vendas 
-- ANALISE DE CARDINALIDADE Vendas <--> Produtos
-- neste caso, CARDINALIDADE RESULTANTE: N:N

