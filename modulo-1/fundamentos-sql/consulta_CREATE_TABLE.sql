-- 2. agora, para criarmos uma table - dentro do nosso DB TreinamentosDB - é preciso seleciona-lo
USE TreinamentosDB;
GO -- este comando indica que, após a "leitura" da instrução anterior, o ambiente de execução deve seguir, imediatamente/diretamente, para a proxima instrução

-- 3. Criar a table
CREATE TABLE Categorias(
    -- agora, neste passo, vamos definir a estrutura - colunas - da table
    CategoriaID INT IDENTITY(1, 1) PRIMARY KEY, -- aqui, temos a primeira coluna da nossa table 
    NomeCategoria VARCHAR(50) NOT NULL -- aqui, temos a segunda coluna da nossa table
);