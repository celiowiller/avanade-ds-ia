-- SCRIPT DE INSERÇÃO DE DADOS NAS TABLES DO DB NORMALIZADO
USE LogiTechDB

-- 2.1: Inserção na table Clientes
INSERT INTO Clientes(Nome_Cliente, Cidade_Cliente, Estado_Cliente)
VALUES
('Ana Silva', 'São Paulo', 'SP'),
('Bruno Souza', 'Niteroi', 'RJ');

-- 2.2: Inserção na table Vendedores
INSERT INTO Vendedores(Nome_Vendedor, Filial_Vendedor)
VALUES
('Carlos Lima', 'Filial Sul'),
('Mariana Prado', 'Filial Norte');

-- 2.3: Inserção na table Produtos
INSERT INTO Produtos(Nome_Produto, Categoria, Preco_Unitario)
VALUES
('Notebook', 'Eletronicos', 4500.00),
('Mouse sem fio', 'Perifericos', 120.00),
('Monitor 27', 'Monitores', 1800.00);

-- 2.4: Inserção na table Vendas
INSERT INTO Vendas(Data_Venda, ID_Cliente, ID_Vendedor)
VALUES
('2026-09-10', 1, 1),
('2026-09-11', 2, 1),
('2026-09-11', 1, 2);

-- 2.5: Inserção na table Itens_Venda
INSERT INTO Itens_Venda(ID_Venda, Cod_Produto, Quantidade, Preco_Praticado)
VALUES
(1, 'P0001', 1, 4500.00),
(1, 'P0002', 2, 120.00),
(2, 'P0002', 1, 120.00),
(3, 'P0003', 1, 1800.00),
(3, 'P0001', 1, 4500.00);