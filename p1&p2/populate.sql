-- Inserir dados na tabela Customer
INSERT INTO Customer (cust_no, name, email, phone, address)
VALUES (1, 'John Doe', 'john.doe@example.com', '123456789', '123 Main St'),
       (2, 'BOB', 'bob@yahoo.com', '917284081', 'Ponte 25 de Abril'),
       (3, 'Vasquinho', 'vascograndao@gmail.com', '964252298','Madorna');


-- Inserir dados na tabela Orders
INSERT INTO Orders (order_no, date, cust_no)
VALUES (1, '2023-01-01', 1),
       (2, '2023-01-01', 2),
       (3, '2023-03-03', 3);

-- Inserir dados na tabela Sale
INSERT INTO Sale (order_no)
VALUES (1),
       (2),
       (3);

-- Inserir dados na tabela Pay
INSERT INTO Pay (order_no)
VALUES (1),
       (2),
       (3);

-- Inserir dados na tabela Product
INSERT INTO Product (sku, name, description, price)
VALUES (1, 'Product 1', 'Description 1', 100.99),
       (2, 'Product 2', 'Description 2', 200.99),
       (3, 'Product 3', 'Description 3', 300.99),
       (4, 'LoliPop', 'CHUPA', 0.99);

-- Inserir dados na tabela EAN_Product
INSERT INTO EAN_Product (sku, ean)
VALUES (1, 'EAN1'),
       (2, 'EAN2'),
       (3, 'EAN3');

-- Inserir dados na tabela Contain
INSERT INTO Contain (order_no, sku, qty)
VALUES (1, 1, 2),
       (1, 2, 1),
       (1, 3, 3),
       (2, 1, 100),
       (3, 4, 2);

-- Inserir dados na tabela Supplier
INSERT INTO Supplier (TIN, sku, name, address, date)
VALUES (1, 1, 'Supplier 1', 'Supplier Address 1', '2022-01-01'),
       (2, 2, 'Supplier 2', 'Supplier Address 2', '2022-02-01'),
       (3, 3, 'Supplier 3', 'Supplier Address 3', '2022-03-01');

-- Inserir dados na tabela Workplace
INSERT INTO Workplace (address, lat, long)
VALUES ('Warehouse Address', 123.456, -78.90),
       ('Office Address', 12.345, -67.89);

-- Inserir dados na tabela Warehouse
INSERT INTO Warehouse (address)
VALUES ('Warehouse Address');

-- Inserir dados na tabela Office
INSERT INTO Office (address)
VALUES ('Office Address');

-- Inserir dados na tabela Delivery
INSERT INTO Delivery (address, sku, TIN)
VALUES ('Warehouse Address', 1, 1),
       ('Office Address', 2, 2);

-- Inserir dados na tabela Department
INSERT INTO Department (name)
VALUES ('Department 1'),
       ('Department 2');

-- Inserir dados na tabela Employee
INSERT INTO Employee (ssn, TIN, bdate, name)
VALUES (123456789, 1, '1990-01-01', 'FÃ¡bio'),
       (987654321, 2, '1995-02-01', 'Employee 2');

-- Inserir dados na tabela Works
INSERT INTO Works (address, name, ssn)
VALUES ('Warehouse Address', 'Department 1', 123456789),
       ('Office Address', 'Department 2', 987654321);

-- Inserir dados na tabela Process
INSERT INTO Process (ssn, order_no)
VALUES (123456789, 1);