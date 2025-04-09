CREATE TABLE produtos_por_nf (
    id SERIAL PRIMARY KEY,
    prod_data DATE NOT NULL,
    prod_nota_fiscal VARCHAR(20) NOT NULL,
    prod_codigo VARCHAR(30) NOT NULL,
    prod_referencia VARCHAR(50),
    prod_descricao TEXT,
    prod_quantidade INTEGER NOT NULL CHECK (prod_quantidade >= 0)
);
