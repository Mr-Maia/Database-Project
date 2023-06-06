-- Drop tables if they exist
DROP TABLE IF EXISTS Process CASCADE ;
DROP TABLE IF EXISTS Works CASCADE;
DROP TABLE IF EXISTS Employee CASCADE;
DROP TABLE IF EXISTS Department CASCADE;
DROP TABLE IF EXISTS Delivery CASCADE;
DROP TABLE IF EXISTS Office CASCADE;
DROP TABLE IF EXISTS Warehouse CASCADE;
DROP TABLE IF EXISTS Workplace CASCADE;
DROP TABLE IF EXISTS Supplier CASCADE;
DROP TABLE IF EXISTS Contain CASCADE;
DROP TABLE IF EXISTS EAN_Product CASCADE;
DROP TABLE IF EXISTS Product CASCADE;
DROP TABLE IF EXISTS Pay CASCADE;
DROP TABLE IF EXISTS Sale CASCADE;
DROP TABLE IF EXISTS Orders CASCADE;
DROP TABLE IF EXISTS Customer CASCADE;

-- Criação das tabelas
CREATE TABLE Customer (
  cust_no INT PRIMARY KEY,
  name VARCHAR(50),
  email VARCHAR(50) UNIQUE,
  phone VARCHAR(20),
  address VARCHAR(100)
);

CREATE TABLE Orders (
  order_no INT PRIMARY KEY,
  date DATE,
  cust_no INT,
  FOREIGN KEY (cust_no) REFERENCES Customer(cust_no)
);

CREATE TABLE Sale (
  order_no INT PRIMARY KEY,
  FOREIGN KEY (order_no) REFERENCES Orders(order_no)
);

CREATE TABLE Pay (
  order_no INT PRIMARY KEY,
  FOREIGN KEY (order_no) REFERENCES Orders(order_no)
);

CREATE TABLE Product (
  sku INT PRIMARY KEY,
  name VARCHAR(50),
  description VARCHAR(100),
  price DECIMAL(10,2)
);

CREATE TABLE EAN_Product (
  sku INT,
  ean VARCHAR(50),
  PRIMARY KEY (sku, ean),
  FOREIGN KEY (sku) REFERENCES Product(sku)
);

CREATE TABLE Contain (
  order_no INT,
  sku INT,
  qty INT,
  PRIMARY KEY (order_no, sku),
  FOREIGN KEY (order_no) REFERENCES Orders(order_no),
  FOREIGN KEY (sku) REFERENCES Product(sku)
);

CREATE TABLE Supplier (
  TIN INT,
  sku INT,
  name VARCHAR(50),
  address VARCHAR(100),
  date DATE,
  PRIMARY KEY (TIN, sku),
  UNIQUE (TIN),
  FOREIGN KEY (sku) REFERENCES Product(sku)
);

CREATE TABLE Workplace (
  address VARCHAR(100),
  lat DECIMAL(9,6),
  long DECIMAL(9,6),
  PRIMARY KEY (address),
  UNIQUE (lat, long)
);

CREATE TABLE Warehouse (
  address VARCHAR(100),
  FOREIGN KEY (address) REFERENCES Workplace(address)
);

CREATE TABLE Office (
  address VARCHAR(100),
  FOREIGN KEY (address) REFERENCES Workplace(address)
);

CREATE TABLE Delivery (
  address VARCHAR(100),
  sku INT,
  TIN INT,
  FOREIGN KEY (address) REFERENCES Workplace(address),
  FOREIGN KEY (sku) REFERENCES Product(sku),
  FOREIGN KEY (TIN) REFERENCES Supplier(TIN)
);

CREATE TABLE Department (
  name VARCHAR(50),
  PRIMARY KEY (name)
);

CREATE TABLE Employee (
  ssn INT PRIMARY KEY,
  TIN INT UNIQUE,
  bdate DATE,
  name VARCHAR(50),
  FOREIGN KEY (TIN) REFERENCES Supplier(TIN)
);

CREATE TABLE Works (
  address VARCHAR(100),
  name VARCHAR(50),
  ssn INT,
  FOREIGN KEY (address) REFERENCES Workplace(address),
  FOREIGN KEY (name) REFERENCES Department(name),
  FOREIGN KEY (ssn) REFERENCES Employee(ssn)
);

CREATE TABLE Process (
  ssn INT,
  order_no INT,
  FOREIGN KEY (ssn) REFERENCES Employee(ssn),
  FOREIGN KEY (order_no) REFERENCES Orders(order_no)
);
