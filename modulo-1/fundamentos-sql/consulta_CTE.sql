-- CTE(Common Table Expression): é uma estrutura temporaria nomeada que armazena o resultado de uma consult SELECT. Seu funcionamento pode ser comparado a uma "Tabela Virtual" que existe apenas durante o processo de execução de uma unica instrução (CRUD)

-- sua definição é dada pela clausula WITH; seu proposito principal é "melhorar" a legibilidade e organização do código.

-- este script tem como objetivo "FILTRAR" APENAS OS PRODUTOS CUJO PREÇO INDIVIDUAL É 
-- *** ESTRITAMENTE MAIOR QUE A MÉDIA DE PREÇO DE SUA RESPECTIVA CATEGORIA
USE TreinamentosDB;
GO


-- 1. Criação da CTE para calcular o preço relativo 
WITH MediasPorCategoria AS( -- aqui, estamos iniciando a declaração da CTE 
    SELECT  
        P.ProdutoID,
        P.NomeProduto,
        P.Preco,
        P.CategoriaID,
        AVG(P.Preco) OVER(
            PARTITION BY P.CategoriaID
        )AS PrecoMedioCategoria
        -- w_function que calcula a média de por categoria.
    FROM Produtos P
)

-- 2 Consulta principal consumindo a CTE e Fazendo JOIN com Categorias
SELECT 
    M.ProdutoID,
    M.NomeProduto,
    M.Preco,
    M.PrecoMedioCategoria,
    C.NomeCategoria
FROM MediasPorCategoria M
INNER JOIN Categorias C ON M.CategoriaID = C.CategoriaID
WHERE M.Preco > M.PrecoMedioCategoria


-- ORDEM DE EXECUÇÃO SEGUIDA PELO SQL SERVER
-- FROM/JOIN -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY