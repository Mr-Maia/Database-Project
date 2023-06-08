--1)
SELECT customer.cust_no, customer.name
FROM customer   --selecionamos um customer da tabela customer
JOIN pay on customer.cust_no = pay.cust_no -- que está presente na tabela de encomendas pagas
GROUP BY customer.cust_no, customer.name  -- agrupamos pelo cust_no e pelo name
HAVING COUNT(pay.cust_no) =( --esta comparação permite ver da tabela pay, qual é o customer que pagou mais encomendas
SELECT MAX(C.cust_count) FROM(
    SELECT COUNT(pay.cust_no) AS cust_count --conta todas as ocorrências de cada cust_no na tabela pay
    FROM pay
    GROUP BY pay.cust_no --agrupa por cust_no que deriva da tabela pay
) AS C);

--2)

SELECT e.name
FROM employee e
WHERE NOT EXISTS (
    SELECT date
    FROM orders o
    WHERE o.date NOT BETWEEN '2021-12-01' AND '2023-01-31'
    AND NOT EXISTS (
        SELECT 1
        FROM process p
        WHERE p.ssn = e.ssn AND p.order_no = o.order_no
    )
);

--3)
-- Conta todos os order_no que pertencem à tabela orders e que não pertençam à tabela pay, agrupados por mês
SELECT COUNT(*), EXTRACT(MONTH FROM orders.date) AS MONTH
FROM orders
WHERE EXTRACT(YEAR FROM orders.date) = '2022'
AND NOT EXISTS (    -- fazemos esta exclusão para ver quais são os elementos da tabela orders que não incluem os order_no da tabela pay
    SELECT pay.order_no
    FROM pay
    WHERE orders.order_no = pay.order_no --fazemos esta comparação para returnarmos a tabela pay em que apenas se confirme esta condição
)
GROUP BY MONTH;

SELECT COUNT(*), EXTRACT(MONTH FROM orders.date) AS MONTH
FROM orders
LEFT JOIN pay on orders.order_no = pay.order_no
WHERE EXTRACT(YEAR FROM orders.date) = '2022' AND pay.order_no is NULL
GROUP BY MONTH;
