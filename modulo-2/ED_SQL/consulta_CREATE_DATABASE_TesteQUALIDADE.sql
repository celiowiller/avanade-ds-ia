CREATE DATABASE TesteQUALIDADE
GO

USE TesteQUALIDADE
GO

-- criação da table
CREATE TABLE Staging_Vendas_Auditoria(
    ID_Transacao INT IDENTITY(1, 1) PRIMARY KEY,
    Data_Venda DATETIME,
    CPF_Cliente VARCHAR(20),
    Valor_Venda DECIMAL(10, 2) NOT NULL,
    Email_Cliente VARCHAR(50) NOT NULL,
    UF_Cliente VARCHAR(50) NOT NULL
);

-- INSERÇÃO DE DADOS
INSERT INTO Staging_Vendas_Auditoria(Data_Venda, CPF_Cliente, Valor_Venda, Email_Cliente,UF_Cliente)
VALUES
('20260928', '11122233344', 150.00, 'ana@email.com',   'SP'),
('20260928', '11122233344', 150.00, 'ana@email.com',   'SP'), -- "cena de crime": duplicidade absoluta
('20260928', '22233344455', -50.00, 'bruno@email.com', 'RJ'), -- "cena de crime": Acucaria + Validade
(NULL,         '33344455566', 200.00, 'carla@emial.com', 'SÃO PAULO'), -- "cena de crime": Completude + Validade
('20260928', '44455566677', 0.00,   'diego@email.com', 'MG');

SELECT * FROM Staging_Vendas_Auditoria

-- AJUSTANDO A TABLE PARA SIMULAR OS "CRIMES"
DROP TABLE Staging_Vendas_Auditoria
--                                                              '28-09-2026'
-- o SQL SERVER aceita valores para DATETIME da seguinte forma: '2026-09-28', '2026/09/28' e '20260928' syslanguages/SET DATEFORMAT 

-- ===============================================================================================

-- 1. pericia tecnica: consulta identificar as duplicidades (UNICIDADE) OK
SELECT
    CPF_Cliente,
    COUNT(*) AS Qtd_Ocorrencias
FROM  Staging_Vendas_Auditoria
GROUP BY CPF_Cliente
HAVING COUNT(*) > 1;

-- 2. "painel de diagnostico" - observar a qualidade dos dados 
SELECT
    ID_Transacao,

    -- a. Teste de completude
    CASE
        WHEN Data_Venda IS NULL THEN 'Falha: Data nula'
        ELSE 'OK'
    END AS Check_Completude_Data,

    -- b. Teste de acuracia
    CASE 
        WHEN Valor_Venda <= 0 THEN 'FALHA: Valor invalido!'
        ELSE 'OK'
    END AS Check_Acuracia_Valor,

    -- c. Teste de validade do email
    CASE
        WHEN Email_Cliente NOT LIKE '%@%.%' THEN 'FALHA: Email invalido'
        ELSE 'OK'
    END AS Check_Validade_Email,

    -- d. Teste de validade UF
    CASE
        WHEN LEN(UF_Cliente) <> 2 THEN  'FALHA: UF Fora do Padrão'
        ELSE 'OK'
    END AS Check_Validade_UF
FROM Staging_Vendas_Auditoria;