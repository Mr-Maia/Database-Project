-- Inserção de dados na tabela customer
INSERT INTO customer (cust_no, name, email, phone, address)
VALUES
    (1, 'João Silva', 'joao@example.com', '123456789', 'Rua A, 2635-003, Rio de Mouro'),
    (2, 'Maria Santos', 'maria@example.com', '987654321', 'Avenida B, 2755-067, Alcabideche'),
    (3, 'Pedro Almeida', 'pedro@example.com', '555555550', 'Rua C, 2785-343, São Domingos de Rana'),
    (4, 'Ana Rodrigues', 'ana@example.com', '555555551', 'Rua D, 2785-343, São Domingos de Rana'),
    (5, 'Rui Ferreira', 'rui@example.com', '555555552', 'Rua E, 2785-343, São Domingos de Rana'),
    (6, 'Marta Carvalho', 'marta@example.com', '555555553', 'Rua F, 2785-343, São Domingos de Rana'),
    (7, 'António Costa', 'antonio@example.com', '555555554', 'Rua G, 2785-343, São Domingos de Rana'),
    (8, 'Sofia Santos', 'sofia@example.com', '555555555', 'Rua H, 2785-343, São Domingos de Rana'),
    (9, 'Carlos Martins', 'carlos@example.com', '555555556', 'Rua I, 2785-343, São Domingos de Rana'),
    (10, 'Inês Ferreira', 'ines@example.com', '555555557', 'Rua J, 2785-343, São Domingos de Rana'),
    (11, 'Manuel Gomes', 'manuel@example.com', '555555558', 'Rua K, 2785-343, São Domingos de Rana'),
    (12, 'Filipa Sousa', 'filipa@example.com', '555555559', 'Rua L, 2785-343, São Domingos de Rana'),
    (13, 'Ricardo Alves', 'ricardo@example.com', '555555560', 'Rua M, 2785-343, São Domingos de Rana');

-- Inserção de dados na tabela orders
INSERT INTO orders (order_no, cust_no, date)
VALUES
    (1, 1, '2022-01-05'),
    (2, 1, '2022-02-10'),
    (3, 2, '2022-03-15'),
    (4, 3, '2022-03-14'),
    (5, 4, '2022-04-20'),
    (6, 4, '2022-05-25'),
    (7, 5, '2022-06-30'),
    (8, 6, '2022-07-10'),
    (9, 7, '2022-08-15'),
    (10, 8, '2022-09-20'),
    (11, 9, '2022-10-25'),
    (12, 10, '2022-11-30'),
    (13, 11, '2022-12-05');

-- Inserção de dados na tabela pay
INSERT INTO pay (order_no, cust_no)
VALUES
    (1, 1),
    (2, 4),
    (3, 2),
    (4, 3),
    (5, 1),
    (6, 1),
    (7, 5),
    (8, 6),
    (9, 7),
    (10, 8),
    (11, 9),
    (12, 10),
    (13, 11);

-- Inserção de dados na tabela employee
INSERT INTO employee (ssn, TIN, bdate, name)
VALUES
    ('111111111', '1234567190', '1990-01-01', 'Fulano de Tal'),
    ('222222222', '0987654320', '1995-05-05', 'Beltrano Silva'),
    ('333333333', '9876543260', '1985-10-10', 'Ciclano Souza'),
    ('444444444', '0123456789', '1992-07-15', 'Isabel Santos'),
    ('555555555', '9876543010', '1998-03-20', 'Rui Pereira'),
    ('666666666', '1234567890', '1987-09-25', 'Ana Costa'),
    ('777777777', '0987654221', '1994-02-05', 'Miguel Rodrigues'),
    ('888888888', '9876543210', '1991-06-10', 'Carla Ferreira'),
    ('999999999', '0123450789', '1996-12-15', 'Hugo Gomes'),
    ('101010101', '9871543210', '1989-08-20', 'Sara Almeida'),
    ('111111112', '1232567890', '1993-04-25', 'Ricardo Silva'),
    ('111111113', '0987604321', '1997-11-05', 'Inês Sousa'),
    ('111111114', '9876543211', '1990-05-10', 'Gonçalo Santos');

-- Inserção de dados na tabela process
INSERT INTO process (ssn, order_no)
VALUES
    ('111111111', 1),
    ('111111111', 2),
    ('999999999', 3),
    ('111111111', 4),
    ('222222222', 5),
    ('222222222', 6),
    ('222222222', 7),
    ('999999999', 8),
    ('999999999', 9),
    ('111111113', 10),
    ('111111113', 11),
    ('111111113', 12),
    ('101010101', 13);

-- Inserção de dados na tabela department
INSERT INTO department (name)
VALUES
    ('Financeiro'),
    ('Recursos Humanos'),
    ('Vendas');

-- Inserção de dados na tabela workplace
INSERT INTO workplace (address, lat, long)
VALUES
    ('Rua D, 987', 10.123456, -20.654321),
    ('Avenida E, 654', 30.987654, -40.123456),
    ('Travessa F, 321', 50.246810, -60.864202),
    ('Praça G, 123', 70.369258, -80.493827),
    ('Largo H, 456', 90.482736, -29.617283),
    ('Avenida I, 789', 10.596174, -10.740741),
    ('Rua J, 654', 30.609612, -40.864198),
    ('Avenida K, 321', 50.523459, -60.987654),
    ('Travessa L, 123', 10.437306, -81.111111),
    ('Praça M, 456', 90.351153, -01.234568),
    ('Largo N, 789', 10.265123, -21.358025),
    ('Avenida O, 654', 30.179123, -41.481481),
    ('Rua P, 321', 50.093123, -61.604938);

-- Inserção de dados na tabela office
INSERT INTO office (address)
VALUES
    ('Rua D, 987'),
    ('Avenida E, 654'),
    ('Travessa L, 123'),
    ('Praça G, 123'),
    ('Largo H, 456'),
    ('Avenida I, 789'),
    ('Rua J, 654');


-- Inserção de dados na tabela warehouse
INSERT INTO warehouse (address)
VALUES
    ('Avenida K, 321'),
    ('Travessa F, 321'),
    ('Praça M, 456'),
    ('Largo N, 789'),
    ('Avenida O, 654'),
    ('Rua P, 321');

-- Inserção de dados na tabela works
INSERT INTO works (ssn, name, address)
VALUES
    ('111111111', 'Financeiro', 'Rua D, 987'),
    ('222222222', 'Financeiro', 'Avenida E, 654'),
    ('333333333', 'Vendas', 'Travessa F, 321'),
    ('444444444', 'Recursos Humanos', 'Praça G, 123'),
    ('555555555', 'Recursos Humanos', 'Largo H, 456'),
    ('666666666', 'Recursos Humanos', 'Avenida I, 789'),
    ('777777777', 'Financeiro', 'Rua J, 654'),
    ('888888888', 'Vendas', 'Avenida K, 321'),
    ('999999999', 'Financeiro', 'Travessa L, 123'),
    ('101010101', 'Vendas', 'Praça M, 456'),
    ('111111112', 'Vendas', 'Largo N, 789'),
    ('111111113', 'Vendas', 'Avenida O, 654'),
    ('111111114', 'Vendas', 'Rua P, 321');


-- Inserção de dados na tabela product
INSERT INTO product (SKU, name, description, price, ean)
VALUES
    ('SKU001', 'Produto 1', 'Descrição do Produto 1', 10.99, 1234567890123),
    ('SKU002', 'Produto 2', 'Descrição do Produto 2', 20.99, 9876543210987),
    ('SKU003', 'Produto 3', 'Descrição do Produto 3', 15.99, 5555555555555),
    ('SKU004', 'Produto 4', 'Descrição do Produto 4', 12.99, 1111111111111),
    ('SKU005', 'Produto 5', 'Descrição do Produto 5', 18.99, 2222222222222),
    ('SKU006', 'Produto 6', 'Descrição do Produto 6', 9.99, 3333333333333),
    ('SKU007', 'Produto 7', 'Descrição do Produto 7', 14.99, 4444444444444),
    ('SKU008', 'Produto 8', 'Descrição do Produto 8', 16.99, 6666666666666),
    ('SKU009', 'Produto 9', 'Descrição do Produto 9', 11.99, 7777777777777),
    ('SKU010', 'Produto 10', 'Descrição do Produto 10', 13.99, 8888888888888),
    ('SKU011', 'Produto 11', 'Descrição do Produto 11', 19.99, 9999999999999),
    ('SKU012', 'Produto 12', 'Descrição do Produto 12', 8.99, 0000000000000),
    ('SKU013', 'Produto 13', 'Descrição do Produto 13', 17.99, 1111111011111);


-- Inserção de dados na tabela contains
INSERT INTO contains (order_no, SKU, qty)
VALUES
    (1, 'SKU001', 2),
    (4, 'SKU002', 1),
    (2, 'SKU001', 3),
    (3, 'SKU003', 1),
    (5, 'SKU004', 2),
    (6, 'SKU005', 1),
    (7, 'SKU006', 3),
    (8, 'SKU007', 1),
    (9, 'SKU008', 2),
    (10, 'SKU009', 1),
    (11, 'SKU010', 3),
    (12, 'SKU011', 1),
    (13, 'SKU012', 2);

-- Inserção de dados na tabela supplier
INSERT INTO supplier (TIN, name, address, SKU, date)
VALUES
    ('1234567890', 'Fornecedor A', 'Avenida K, 321', 'SKU001', '01/01/2022'),
    ('0987654321', 'Fornecedor B', 'Avenida K, 321', 'SKU002', '02/02/2022'),
    ('9876543210', 'Fornecedor C', 'Avenida K, 321', 'SKU003', '03/03/2022'),
    ('0123456789', 'Fornecedor D', 'Avenida K, 321', 'SKU004', '04/04/2022'),
    ('5555555555', 'Fornecedor E', 'Travessa F, 321', 'SKU005', '05/05/2022'),
    ('8888888888', 'Fornecedor F', 'Travessa F, 321', 'SKU006', '06/06/2022'),
    ('2222222222', 'Fornecedor G', 'Praça M, 456', 'SKU007', '07/07/2022'),
    ('3333333333', 'Fornecedor H', 'Largo N, 789', 'SKU008', '08/08/2022'),
    ('4444444444', 'Fornecedor I', 'Largo N, 789', 'SKU009', '09/09/2022'),
    ('6666666666', 'Fornecedor J', 'Avenida O, 654', 'SKU010', '10/10/2022'),
    ('9999999999', 'Fornecedor K', 'Avenida O, 654', 'SKU011', '11/11/2022'),
    ('7777777777', 'Fornecedor L', 'Rua P, 321', 'SKU012', '12/12/2022');

-- Inserção de dados na tabela delivery
INSERT INTO delivery (address, TIN)
VALUES
    ('Avenida K, 321', '1234567890'),
    ('Avenida K, 321', '0987654321'),
    ('Avenida K, 321', '9876543210'),
    ('Avenida K, 321', '0123456789'),
    ('Travessa F, 321', '5555555555'),
    ('Travessa F, 321', '8888888888');