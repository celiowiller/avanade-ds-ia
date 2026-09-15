-- passo 1. indicar o DB no qual queremos criar a nova table
USE TreinamentosDB;
GO

-- passo 2. definir a criação da table
CREATE TABLE Produtos(
    -- passo 3. definir a estrutura da table (as colunas)
    ProdutoID INT IDENTITY(1, 1) PRIMARY KEY,
    -- NomeProduto NVARCHAR(100) NOT NULL, National Unicode / NVARCHAR(MAX) NVARCHAR(4000)
    -- observa todos os idiomas do mundo (inclusive com seus caracteres  expeciais)
    NomeProduto VARCHAR(100) NOT NULL, -- Non-Unicode(ASCII/ANSI)/ VARCHAR(MAX) VARCHAR(8000)
    -- VARCHAR (caracteres ocidentais A-Z, acentos da lingua portuguesa)
    Preco DECIMAL(10, 2) NOT NULL CHECK (Preco >= 0),
    DataCadastro DATETIME DEFAULT GETDATE(),
    CategoriaID INT NOT NULL,

    -- Restrição (Constraint) de Integridade Referencial -> determina que o DB não sofra/passe por um processo de "corrupção" de dados, ou seja, é necessario que a integridade dos dados seja intacta.
    CONSTRAINT FK_Produtos_Categorias FOREIGN KEY(CategoriaID)
        REFERENCES Categorias(CategoriaID)

);

-- DECIMAL(10, 2): tipo numérico exato com alta precisão, ou seja, a coluna aceitará qualquer numero até 10 digitos totais e sendo, 2 destes digitos, reservados para as casas decimais do numero (ex: 000000000.00). Dessa forma, é possivel evitar arredondamentos, por exemplo, para numeros float.

-- CHECK(Preco >= 0): aqui, estabelecemos uma regra de INTEGRIDADE DE DOMINIO; significa que estamos "impedindo", fisicamente, qualquer tentativa de inserir um valor numerioc inconsistente (por exemplo, um valor negativo = -50)

-- DATETIME: aqui, nossa coluna irá armazena dados de data e hora combinados

-- DEFAULT GETDATE(): se, caso o script de inserção não indicar uma data hora especifica, o SGBD (SQL SERVER) executa a função GETDATE() no exato milissegundo em que a gravação, do registro no DB, é feita. 