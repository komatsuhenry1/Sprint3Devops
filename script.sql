--AiCommerceTables

--criando tabela cliente
CREATE TABLE cliente(
    id_clie INT,
    nm_clie VARCHAR(40),
    email_clie VARCHAR(40),
    endereco_clie VARCHAR(80),
    senha_clie VARCHAR(40)
);

--5 insert de dados na tabela cliente 
INSERT INTO cliente (id_clie, nm_clie, email_clie, endereco_clie, senha_clie) 
VALUES (1, 'João Silva', 'joao@email.com', 'Rua das Flores, 123', 'senha123');

INSERT INTO cliente (id_clie, nm_clie, email_clie, endereco_clie, senha_clie) 
VALUES (2, 'Maria Santos', 'maria@email.com', 'Av. das Graças, 456', 'senha456');

INSERT INTO cliente (id_clie, nm_clie, email_clie, endereco_clie, senha_clie) 
VALUES (3, 'Pedro Oliveira', 'pedro@email.com', 'Rua Sorriso, 789', 'senha789');

INSERT INTO cliente (id_clie, nm_clie, email_clie, endereco_clie, senha_clie) 
VALUES (4, 'Ana Pereira', 'ana@email.com', 'Av. Felicidade, 1011', 'senha1011');

INSERT INTO cliente (id_clie, nm_clie, email_clie, endereco_clie, senha_clie) 
VALUES (5, 'Carla Costa', 'carla@email.com', 'Rua Feliz, 1213', 'senha1213');

--criando tabela pedido
CREATE TABLE pedido(
    id_pedido INT,
    dt_pedido DATE,
    status_pedido VARCHAR(50),
    preco_total DECIMAL(6,2),
    id_clie INT, 
    FOREIGN KEY (id_clie) REFERENCES cliente(id_clie) 
);

--5 insert de dados na tabela cliente 
INSERT INTO pedido (id_pedido, dt_pedido, status_pedido, preco_total, id_clie) 
VALUES (1, '2024-01-06', 'Em andamento', 200.00, 1);

INSERT INTO pedido (id_pedido, dt_pedido, status_pedido, preco_total, id_clie) 
VALUES (2, '2024-02-14', 'Concluído', 150.00, 2);

INSERT INTO pedido (id_pedido, dt_pedido, status_pedido, preco_total, id_clie) 
VALUES (3, '2024-03-22', 'Em andamento', 300.00, 3);

INSERT INTO pedido (id_pedido, dt_pedido, status_pedido, preco_total, id_clie) 
VALUES (4, '2024-04-18', 'Concluído', 180.00, 4);

INSERT INTO pedido (id_pedido, dt_pedido, status_pedido, preco_total, id_clie) 
VALUES (5, '2024-05-30', 'Em andamento', 250.00, 5);

