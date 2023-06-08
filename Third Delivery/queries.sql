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



SELECT COUNT(*), EXTRACT(MONTH FROM orders.date) AS MONTH
FROM orders
WHERE EXTRACT(YEAR FROM orders.date) = '2022'
AND NOT EXISTS (
    SELECT pay.order_no
    FROM pay
    JOIN orders on orders.order_no = pay.order_no
)
GROUP BY MONTH;
