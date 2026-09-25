-- OPERAÇÕES COM WINDOWS FUNCTIONS
-- sua estrutura conta com os seguintes recursos: 
-- FUNÇÃO() OVER(PARTITION BY coluna_partição ORDER BY coluna_ordenação)

-- OVER(): define os limites e a ordenação da janela dados
-- PARTITION BY: aqui, dividimos o conjunto de resultados em partições independentes
-- ORDER BY: aqui, definimos a ordenação dos dados dentro de cada partição

USE LogiTechDB

-- ===============================================
-- WINDOW FUNCTION PARA HISTORICO
-- ===============================================

-- 1.6 CTE(Common Table Expression) BASE DE AGREGAÇÃO DIARIA POR VENDEDOR
-- Unifica as tables Vendas, Vendedores e Itens_Venda


WITH Vendas_Diarias_CTE AS (
    SELECT 
        ven.ID_Vendedor,
        ven.Nome_Vendedor,
        v.Data_Venda,
        SUM(iv.Quantidade * iv.Preco_Praticado) AS Total_Vendido_Dia
    FROM Vendas v
    INNER JOIN Vendedores ven ON v.ID_Vendedor = ven.ID_Vendedor
    INNER JOIN Itens_Venda iv ON v.ID_Venda = iv.ID_Venda
    GROUP BY ven.ID_Vendedor, ven.Nome_Vendedor, v.Data_Venda
)


SELECT
    Nome_Vendedor,
    Data_Venda,
    Total_Vendido_Dia,
    ROW_NUMBER() OVER(PARTITION BY ID_Vendedor ORDER BY Total_Vendido_Dia DESC) AS Sequencial_RowNumber,
    RANK() OVER(PARTITION BY ID_Vendedor ORDER BY Total_Vendido_Dia DESC) AS Posicao_Rank_ComSalto,
    DENSE_RANK() OVER(PARTITION BY ID_Vendedor ORDER BY Total_Vendido_Dia DESC) AS Posicao_DenseRank_SemSalto
FROM Vendas_Diarias_CTE;

-- ===============================================
-- OPERAÇÃO 2: LAG() E LEAD()
-- Classificando os melhores dias de venda de cada vendedor
-- ===============================================
WITH Vendas_Diarias_CTE AS (
    SELECT 
        ven.ID_Vendedor,
        ven.Nome_Vendedor,
        v.Data_Venda,
        SUM(iv.Quantidade * iv.Preco_Praticado) AS Total_Vendido_Dia
    FROM Vendas v
    INNER JOIN Vendedores ven ON v.ID_Vendedor = ven.ID_Vendedor
    INNER JOIN Itens_Venda iv ON v.ID_Venda = iv.ID_Venda
    GROUP BY ven.ID_Vendedor, ven.Nome_Vendedor, v.Data_Venda
)
SELECT
    Nome_Vendedor,
    Data_Venda,
    Total_Vendido_Dia AS Valor_Hoje,
    LAG(Total_Vendido_Dia, 1, 0) OVER(PARTITION BY ID_Vendedor ORDER BY Data_Venda) AS Valor_Dia_Anterior,
    -- definir uma operação
    Total_Vendido_Dia - LAG(Total_Vendido_Dia, 1, 0) OVER(PARTITION BY ID_Vendedor ORDER BY Data_Venda) AS Variacao_Diaria,


    LEAD(Total_Vendido_Dia, 1, 0) OVER(PARTITION BY ID_Vendedor ORDER BY Data_Venda) As Proxima_Venda_Prevista
FROM Vendas_Diarias_CTE;

-- ===============================================
-- OPERAÇÃO 3: TOTAL ACUMULADO (Running Total) e MÉDIA MOVEL
-- Soma progressiva e evolução de média por vendedor
-- ===============================================
WITH Vendas_Diarias_CTE AS (
    SELECT 
        ven.ID_Vendedor,
        ven.Nome_Vendedor,
        v.Data_Venda,
        SUM(iv.Quantidade * iv.Preco_Praticado) AS Total_Vendido_Dia
    FROM Vendas v
    INNER JOIN Vendedores ven ON v.ID_Vendedor = ven.ID_Vendedor
    INNER JOIN Itens_Venda iv ON v.ID_Venda = iv.ID_Venda
    GROUP BY ven.ID_Vendedor, ven.Nome_Vendedor, v.Data_Venda
)
SELECT 
    Nome_Vendedor, 
    Data_Venda,
    Total_Vendido_Dia,
    -- aqui, vamos fazer a acumulação progressivade faturamento dia a dia
    SUM(Total_Vendido_Dia) OVER(PARTITION BY ID_Vendedor ORDER BY Data_Venda) AS Faturamento_Acumulado,
    -- média movel das vendas até o dia atual
    AVG(Total_Vendido_Dia) OVER(PARTITION BY ID_Vendedor ORDER BY Data_Venda) AS Media_Movel
FROM Vendas_Diarias_CTE;
