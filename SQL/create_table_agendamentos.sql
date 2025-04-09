CREATE TABLE agendamentos (
    id SERIAL PRIMARY KEY,

    cliente_cod VARCHAR(20),
    cliente_razao_social VARCHAR(150),
    cliente_cnpj_cpf VARCHAR(20),
    cidade VARCHAR(100),
    uf CHAR(2),
    telefone VARCHAR(20),

    produto VARCHAR(60),
    descricao_ocorrencia TEXT,
    area_responsavel VARCHAR(50),

    responsavel_pos_vendas INTEGER REFERENCES users(id),
    data_agendamento DATE DEFAULT CURRENT_DATE,
    data_prevista_atendimento DATE DEFAULT (CURRENT_DATE + INTERVAL '3 days'),
    status VARCHAR(30) DEFAULT 'pendente',

    observacoes TEXT
);
