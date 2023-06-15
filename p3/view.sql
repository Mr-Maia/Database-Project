CREATE VIEW product_sales AS
SELECT c.cust_no, c.name, p.SKU, o.order_no, con.qty, (p.price * con.qty) AS total_price,
       EXTRACT(YEAR FROM o.date) AS year, EXTRACT(MONTH FROM o.date) AS month,
       EXTRACT(DAY FROM o.date) AS day_of_month, EXTRACT(DOW FROM o.date) AS day_of_week,
       TRIM(SUBSTRING(c.address, POSITION(',' IN c.address) + 11)) AS city --TRIM VAI RETIRAR OS ESPAÇOS

FROM customer c
JOIN orders o ON c.cust_no = o.cust_no
JOIN pay py ON o.order_no = py.order_no
JOIN contains con ON o.order_no = con.order_no
JOIN product p ON con.SKU = p.SKU;


SELECT sku, order_no, qty, total_price, year, month, day_of_month, day_of_week, city
FROM product_sales;
