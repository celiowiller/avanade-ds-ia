-- operar com a ARQUITETURA MEDALHÃO
USE TesteQUALIDADE

-- definir uma nova table 
CREATE TABLE Bronze_Ingestao(
    ID_Ingestao INT IDENTITY(1, 1) PRIMARY KEY,
    Data_Hora_Ingestao DATETIME DEFAULT GETDATE(), -- na ausencia de um valor, assume-se o valor obtido a partir do sistema; essa modalidade nos lembra UM TIMESTAP
    Nome_Arquivo_Fonte VARCHAR(50),
    ID_Transacao_Bruta VARCHAR(50),
    Data_Venda_Bruta VARCHAR(50),
    Cliente_Bruto VARCHAR(100),
    Valor_Bruto DECIMAL(10, 2),
    UF_Bruto VARCHAR(50)
);

DROP TABLE Bronze_Ingestao;

--DELETE TABLE Bronze_Ingestao;
DELETE FROM Bronze_Ingestao;
-- consulta de ingestão de dados
INSERT INTO Bronze_Ingestao
(Data_Hora_Ingestao, Nome_Arquivo_Fonte, ID_Transacao_Bruta, Data_Venda_Bruta, Cliente_Bruto, Valor_Bruto, UF_Bruto)
VALUES
(GETDATE(),'venda_20260829.csv', 5, '20260928', 'Ana Silva',    150.00,  'sp'),
(GETDATE(),'venda_20260829.csv', 5, '20260928', 'Ana Silva',    150.00,  'sp'),
(GETDATE(),'venda_20260829.csv', 6, '20260928', 'Bruno Souza',  250.00,  'rj'),
(GETDATE(),'venda_20260829.csv', 7, '20260928', 'Carla Soares', 500.00,  'são paulo');

SELECT * FROM Bronze_Ingestao


-- nivel SILVER
CREATE TABLE Silver_Vendas(
    --ID_Venda INT IDENTITY(1,1) PRIMARY KEY,
    ID_Venda INT PRIMARY KEY,
    Data_Venda DATE NOT NULL,
    Nome_Cliente VARCHAR(50) NOT NULL,
    Valor_Venda DECIMAL(10, 2) NOT NULL,
    UF_Cliente CHAR(2) NOT NULL,
    Data_Processamento_Silver DATETIME DEFAULT GETDATE()
);

DROP TABLE Silver_Vendas;


-- inserção na table Silver_Vendas
INSERT INTO Silver_Vendas
(ID_Venda, Data_Venda, Nome_Cliente, Valor_Venda, UF_Cliente, Data_Processamento_Silver)

-- DEFININDO OPERAÇÕES DO NIVEL SILVER
SELECT
    CAST(ID_Transacao_Bruta AS INT) AS ID_Venda,
    CAST(Data_Venda_Bruta AS DATE) AS Data_Venda,
    LTRIM(RTRIM(Cliente_Bruto)) AS Nome_Cliente, -- aqui, estamos fazendo uma "higienização" de texto. pois estamos removendo espaços em branco do nome do cliente - à esquerda e à direita
    CAST(Valor_Bruto AS DECIMAL(10, 2)) AS Valor_Venda,

    -- Normalização de Nomes e Regras de negocio de UF
    CASE
        WHEN UPPER(UF_Bruto) IN ('SP', 'SÃO PAULO', 'SAO PAULO') THEN 'SP'
        WHEN UPPER(UF_Bruto) IN ('RJ', 'RIO DE JANEIRO') THEN 'RJ'
        ELSE 'OU'
    END AS UF_Cliente,

    -- preenchendo a coluna Data_Processamento_Silver
    GETDATE() AS Data_Processamento_Silver

FROM (
    -- subconsulta/subquery para a eliminação de duplicidades (WF)
    SELECT
        ID_Transacao_Bruta,
        Data_Venda_Bruta,
        Cliente_Bruto,
        Valor_Bruto,
        UF_Bruto,
        ROW_NUMBER() OVER(PARTITION BY ID_Transacao_Bruta ORDER BY ID_Ingestao) AS RowNum
    FROM Bronze_Ingestao
)AS SubDuplicata
-- filtro
WHERE RowNum = 1;



-- nivel GOLD

-- definir a table GOLD (Tabela-Fato focada em consumo analitico/ BI)
CREATE TABLE Gold_Fato_Vendas(
    SK_Venda INT IDENTITY(1, 1) PRIMARY KEY, 
    ID_Venda INT NOT NULL,
    Data_Venda DATE NOT NULL,
    Ano_Venda INT NOT NULL,
    Mes_Venda INT NOT NULL,
    UF_Cliente CHAR(2) NOT NULL,
    Valor_Venda DECIMAL(10, 2) NOT NULL,
    Data_Carga_Gold DATETIME DEFAULT GETDATE()
);

-- inserção na table Gold_Fato_Vendas ("Alimentada" diretamente a partir de Silver)
INSERT INTO Gold_Fato_Vendas
(ID_Venda, Data_Venda, Ano_Venda, Mes_Venda, UF_Cliente, Valor_Venda, Data_Carga_Gold)
-- VALUES

-- DEFININDO OPERAÇÕES DO NIVEL GOLD
SELECT 
    ID_Venda,
    Data_Venda,
    YEAR(Data_Venda) AS Ano_Venda, -- aqui, estamos extraindo do ano ára otimização do relatorio
    MONTH(Data_Venda) AS Mes_Venda, -- extração do dado mês
    UF_Cliente,
    Valor_Venda,
    GETDATE() AS Data_Carga_Gold
FROM Silver_Vendas;

SELECT * FROM Gold_Fato_Vendas;


-- ===============================================
-- AUDITORIA FINAL
-- ===============================================

SELECT 'Bronze(Raw)' AS Camada, COUNT(*) AS Total_Linhas FROM Bronze_Ingestao
UNION ALL
SELECT 'Silver(Cleansed)' AS Camada, COUNT(*) AS Total_Linhas FROM Silver_Vendas
UNION ALL
SELECT 'Gold(Curated)' AS Camada, COUNT(*) AS Total_Linhas FROM Gold_Fato_Vendas;