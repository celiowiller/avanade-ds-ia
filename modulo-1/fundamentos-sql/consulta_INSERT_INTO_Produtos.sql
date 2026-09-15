USE TreinamentosDB;
GO

-- 1. definir a consulta de inserção de dados numa table
INSERT INTO Produtos (NomeProduto, Preco, DataCadastro, CategoriaID)
VALUES 
('Fundamentos de Python', 153.25, '2026-03-12', 1),
('Introdução ao SQL',  289.63, '2026-03-12', 2),
('Srum Master', 100.99, '2026-03-12', 3),
('Analise de dados Python', 457.78, '2026-03-12', 1);