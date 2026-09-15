--USE TreinamentosDB;
--GO

--EXEC sp_help 'Produtos';

USE TreinamentosDB;
GO

-- 1. definir a consulta de inserção de dados numa table
INSERT INTO Produtos (NomeProduto, Preco, CategoriaID)
VALUES 
('Fundamentos de Java', 153.25, 1),
('Introdução ao HTML',  289.63, 2),
('Kanbam', 100.99, 3),
('Fundamentos de Javascript', 457.78, 1);