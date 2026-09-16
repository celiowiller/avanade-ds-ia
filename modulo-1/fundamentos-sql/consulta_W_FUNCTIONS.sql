USE TreinamentosDB;
GO
 -- neste passo, vamos fazer uso das WINDOW FUNCTIONS (funções de janela): seus propostisos são -> realizar calculos através de um conjunto de linhas relacionadas ao registro (seja ele qual for), sem a necessidade de fazer agrupamento (sem uso de GROUP BY)

 SELECT 

    C.NomeCategoria,
    P.NomeProduto,
    P.Preco,

    -- 1. W_Function que enumera os produtos do mais caro para o mais barato; dentro de cada categoria

    -- OVER(): no SQL esta instrução define uma WINDOW(Janela) de dados sobre a qual uma função agregação(SUM, AVG, COUNT) ou de ranking(ROW_NUMBER,RANK) será calculada 
    ROW_NUMBER() OVER( -- esta instrução está criando um "rankeamento"(1, 2, 3...)
       PARTITION BY P.CategoriaID -- divisão em grupos 
       ORDER BY P.Preco DESC -- ordenamento para calculaos sequenciais
    )AS PosicaoNaCategoria,

    -- ROW_NUMBER(): função que gera um número sequencial para cada linha
    -- PARTITION BY P.CategoriaID: instrução que reinicia a contagem do raking do zero para cada categoria
    -- ORDER BY P.Preco DESC: instrução que ordena os produtos do mais caro para o mais para definir quem é 0 1º, 2º...

    -- 2. Calcular a media de preço da categoria mantendo o preço individual na mesma linha
    AVG(P.Preco) OVER(
        PARTITION BY P.CategoriaID
    )AS MediaPrecoCategoria ,

    -- 3. calcular a diferença entre o preço do produto e a média de sua categoria
    P.Preco - AVG(P.Preco) OVER(
        PARTITION BY P.CategoriaID
    )AS DiferencaMedia

FROM Produtos P
INNER JOIN Categorias C ON P.CategoriaID = C.CategoriaID
ORDER BY C.NomeCategoria, PosicaoNaCategoria;