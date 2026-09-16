-- CRUD: Create, Read, Update, Delete - fluxo de dados 
USE TreinamentosDB

-- =======================================================
-- 1. CREATE (Inserção de dados na base)
-- =======================================================
INSERT INTO Produtos(NomeProduto, Preco, CategoriaID)
VALUES 
('Fundamentos Power BI', 325.89, 1)
GO

-- =======================================================
-- 2. READ (Consulta/Leitura simples)
-- =======================================================
SELECT 
    ProdutoID,
    NomeProduto,
    Preco,
    CategoriaID
    
FROM Produtos 
WHERE NomeProduto LIKE '%BI%'; -- o uso do comando LIKE determina que a seleção siga 
-- uma condição: o valor buscado precisar ser composto pela expressão descrita entre os caracteres %%
GO

-- =======================================================
-- 3. UPDATE (Atualização de um determinado registro)
-- =======================================================
UPDATE Produtos
SET Preco = 299.90
WHERE NomeProduto = 'Fundamentos Power BI'  
GO

-- =======================================================
-- 4. DELETE (remoção de um determinado registro)
-- =======================================================
DELETE FROM Produtos
WHERE NomeProduto = 'Fundamentos Power BI'
