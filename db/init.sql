CREATE TABLE pedido (
    id SERIAL PRIMARY KEY,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    descricao TEXT
);

INSERT INTO  pedido (nome, email, descricao) VALUES ('Kil', 'kil.teste@inteli.com', 'Ferias');