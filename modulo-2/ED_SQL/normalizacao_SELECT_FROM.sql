USE LogiTechDB

SELECT * FROM Clientes

SELECT * FROM Vendedores

SELECT * FROM Vendas

SELECT * FROM Produtos

SELECT * FROM Itens_Venda

-- ====================================================================

SELECT 
    v.ID_Venda,
    v.Data_Venda,

    c.ID_Cliente,
    c.Nome_Cliente,
    c.Cidade_Cliente,
    c.Estado_Cliente,

    p.Cod_Produto,
    p.Nome_Produto,
    p. Categoria,

    vi.Quantidade,
    vi.Preco_Praticado AS Preco_Unitario,

    vend.ID_Vendedor,
    vend.Filial_Vendedor
FROM Vendas v
INNER JOIN Clientes c ON v.ID_Cliente = c.ID_Cliente
INNER JOIN Vendedores vend ON v.ID_Vendedor = vend.ID_Vendedor
INNER JOIN Itens_Venda vi ON v.ID_Venda = vi.ID_Venda
INNER JOIN Produtos p ON vi.Cod_Produto = p.Cod_Produto
ORDER BY v.ID_Venda, p.Cod_Produto;
