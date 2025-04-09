CREATE TABLE ocorrencias (
    id SERIAL PRIMARY KEY,

    ocorr_data_do_pedido DATE,
    ocorr_cod_cliente VARCHAR(20),
    ocorr_razao_social VARCHAR(150),
    ocorr_cnpj_cpf VARCHAR(20),
    ocorr_nota_fiscal_aton VARCHAR(20),
    ocorr_nota_fiscal_key VARCHAR(60),
    ocorr_nota_fiscal_guarani INTEGER, -- FK para produtos_por_nf
    ocorr_valor_total_s_imp NUMERIC(12, 2),

    ocorr_forma_de_pagamento VARCHAR(50),
    ocorr_cidade VARCHAR(100),
    ocorr_uf CHAR(2),
    ocorr_cod_transportadora VARCHAR(20),
    ocorr_transportadora VARCHAR(100),
    ocorr_representante VARCHAR(100),
    ocorr_telefone VARCHAR(20),

    ocorr_responsavel_pos_vendas INTEGER, -- FK para users(id)
    ocorr_descricao TEXT,
    ocorr_tipo_de_ocorrencia VARCHAR(50),
    ocorr_area_responsavel VARCHAR(50),
    ocorr_nivel_de_criticidade VARCHAR(50),

    ocorr_produto VARCHAR(60), -- Apenas informativo, sem FK
    ocorr_valor NUMERIC(12, 2),
    ocorr_valor_frete NUMERIC(12, 2),

    ocorr_inicio_da_tratativa DATE,
    ocorr_finalizacao DATE,
    ocorr_decorrido INTERVAL,

    ocorr_informacoes_adicionais TEXT,
    ocorr_resolvido BOOLEAN DEFAULT FALSE,
    ocorr_solucao TEXT,
    ocorr_processo_de_nota_fiscal TEXT,

    -- FKs funcionais
    CONSTRAINT fk_guarani FOREIGN KEY (ocorr_nota_fiscal_guarani) REFERENCES produtos_por_nf(id),
    CONSTRAINT fk_responsavel FOREIGN KEY (ocorr_responsavel_pos_vendas) REFERENCES users(id)
);
