USE TreinamentosDB;
GO

-- 1. instrução de seleção com GROUP BY
SELECT 
    C.NomeCategoria,

    COUNT(P.ProdutoID) AS TotalProdutos, -- COUNT(): função do T-SQL que tem o proposito de fazer uma contagem de produtos, existentes em nossa table, considerando os IDs dos produtos.
    -- AS TotalProdutos: esta instrução define um novo alias(apelido) para o resultado obtido a partir da operação de contagem; portanto, podemos assumir que teremos uma nova coluna para exibir este resultado

    AVG(P.Preco) AS PrecoMedio, -- AVG(): função do T-SQL que tem o proposito de fazer o calculo da média de preços dos produtos, existentes em nossa table, considerando os preços associados aos produtos armazenados.
    -- AS PrecoMedio: esta instrução define um novo alias(apelido) para o resultado obtido a partir da operação de calculo da média; portanto, podemos assumir que teremos uma nova coluna para exibir este resultado

    SUM(P.Preco) AS ValorTotalEstoque -- SUM(): função do T-SQL que tem o proposito de fazer a somatoria de preços dos produtos, existentes em nossa table, considerando os preços associados aos produtos armazenados.
    -- AS ValorTotalEstoque: esta instrução define um novo alias(apelido) para o resultado obtido a partir da operação de soma; portanto, podemos assumir que teremos uma nova coluna para exibir este resultado

FROM Categorias C
LEFT JOIN Produtos P ON C.CategoriaID = p.CategoriaID


GROUP BY C.NomeCategoria; -- GROUP BY: comando que define o agrupamento dos resultados obtidos a partir do nome da categoria que consta na table Categorias(C)