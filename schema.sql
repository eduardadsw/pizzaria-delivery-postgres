CREATE TABLE pizzas (
    id SERIAL PRIMARY KEY,
    sabor VARCHAR(50) NOT NULL,
    descricao TEXT,
    preco NUMERIC(10, 2) NOT NULL
);

CREATE TABLE pedido (
    id SERIAL PRIMARY KEY,
    nome_cliente VARCHAR(100) NOT NULL,
    telefone VARCHAR(20) NOT NULL,
    endereco TEXT NOT NULL,
    pagamento VARCHAR(30) NOT NULL,
    id_pizza INT REFERENCES pizzas(id),
    data_pedido TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
