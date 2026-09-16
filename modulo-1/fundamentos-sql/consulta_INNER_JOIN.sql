-- ESTUDO DE SELEÇÃO E JOINS (JUNÇÕES)
USE TreinamentosDB; -- definindo o DB de trabalho - é o uso do comando USE
GO -- é o comando de "separação" de execução em lotes.... significa que, antes do comando, estmaos executando um lote de instruções e, na sequencia, outro lote de instruções 

-- 1. fazer da instrução de seleção 
SELECT -- comando de inicia a seleção de dados de uma determinada table 

    P.ProdutoID, -- instrução que seleciona a coluna ProdutoID - esta coluna pertence ao alias(apelido) P
    P.NomeProduto, -- instrução que seleciona a coluna NomeProduto - esta coluna pertence ao alias(apelido) P
    P.Preco, -- instrução que seleciona a coluna Preco - esta coluna pertence ao alias(apelido) P
    C.NomeCategoria -- instrução que seleciona a coluna NomeCategoria - esta coluna pertence ao alias(apelido) C

FROM Produtos P -- aqui, estamos definindo que a table Produtos é a tabela principal da consulta de seleção; também, estamos dizendo que esta mesma tabela para a ser "conhecida" como P, ou seja, este é seu alias(apelido)
INNER JOIN Categorias C ON P.CategoriaID = C.CategoriaID;

-- acima, estamos definindo que a table Categorias é a tabela que ESTÁ SENDO "JUNTADA" A TABELA PRODUTOS da consulta de seleção; também, estamos dizendo que esta mesma tabela para a ser "conhecida" como C, ou seja, este é seu alias(apelido). Esta junção permite que trazer/recuperar os registros que possuem CORRESPONDENCIA NAS DAS TABLES.

-- ON P.CategoriaID = C.CategoriaID;: estamos definindo p critério de "ligação/junção" entre as tabelas. O omando relaciona a chave estrangeira CategoriaID da table  de Produtos(P) com a chave primaria CategoriaID da table Categorias(C)

--**==========================================================================**

-- 2. LEFT JOIN: a instrução preserva os dados da tabela - à esquerda da junção - e retorna todos os dados da outra tabela, DESDE QUE ESTES DADOS EXISTAM
SELECT
    P.ProdutoID,
    P.NomeProduto,
    P.Preco,
    C.NomeCategoria
FROM Produtos P
LEFT JOIN Categorias C ON P.CategoriaID = C.CategoriaID;

-- 3. RIGHT JOIN: a instrução preserva os dados da tabela - à DIREITA da junção (estamos dizendo que a tabela à direita da junção nada mais é do que: A TABELA INFORMADA DEPOIS DA CLAUSULA/COMANDO RIGHT JOIN) - e retorna todos os dados da outra tabela, DESDE QUE ESTES DADOS EXISTAM
SELECT
    P.NomeProduto,
    P.Preco,
    C.CategoriaID,
    C.NomeCategoria
FROM Produtos P
RIGHT JOIN Categorias C 
ON P.CategoriaID = C.CategoriaID;