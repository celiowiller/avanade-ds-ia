USE TreinamentosDB;
GO

-- 1. criar uma seleção, agora, fazendo uso de JOIN, clausula WHERE e clausula ORDER BY

SELECT 
    P.NomeProduto,
    P.Preco,
    C.NomeCategoria
FROM Produtos P
INNER JOIN Categorias C ON P.CategoriaID = C.CategoriaID

-- aqui, vamos definir a "condição" de seleção 
WHERE C.NomeCategoria = 'Programação'AND P.Preco > 100.00
-- WHERE: "onde" NomeCategoria, com origem na table Categorias (C), seja composto com o valor Programação E(AND) o valor  de Preco seja maior que 100.00
-- vamos ordenar o resultado 
ORDER BY P.Preco DESC;

-- acima, estamos ordenando os valores encontrados, de acordo com a condição, acima, estabelecida, de forma decrescente: ou seja, "do maior para o menor"