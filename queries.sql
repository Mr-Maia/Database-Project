-- 1)π Customer.name((Customer ⨝ Order ⨝ Contain ⨝ Product) σ (price > 50)(Product) σ(date.year = 2023)(Order))

SELECT DISTINCT C.name
FROM Customer AS C
JOIN Orders AS O ON C.cust_no = O.cust_no
JOIN Contain AS Con ON O.order_no = Con.order_no
JOIN Product AS P ON Con.sku = P.sku
WHERE P.price > 50 AND EXTRACT(YEAR FROM O.date) = 2023;


-- 2)π Employee.name (Employee ⨝( process ⨝ Order)) σ(date.year = 2023 and date.month = 01)(Order)) - π Employee.name (Employee⨝(Works ⨝ Office))

SELECT DISTINCT Employee.name
FROM Employee
JOIN Process ON Employee.ssn = Process.ssn
JOIN Orders ON Process.order_no = Orders.order_no
WHERE EXTRACT(YEAR FROM Orders.date) = 2023 AND EXTRACT(MONTH FROM Orders.date) = 1
EXCEPT
SELECT Employee.name
FROM Employee
JOIN Works ON Employee.ssn = Works.ssn
JOIN Office ON Works.address = Office.address
LIMIT(1);


-- 3) π product_name (σ qty=max(total_qty)(Product ⨝ Contain ⨝ (sum(Contain.qty)->total_qty)))

SELECT product.name
FROM Product
JOIN Contain ON Product.sku = Contain.sku
GROUP BY Product.name, Contain.qty
HAVING Contain.qty = (SELECT MAX(qty) FROM Contain);


-- 4) π (Sale.order_no, SUM(Contain.qty * Product.price) AS total_value) (Sale ⨝ Contain ⨝ Product)

SELECT Sale.order_no, SUM(Contain.qty * Product.price) AS total_value
FROM Sale
JOIN Contain ON Sale.order_no = Contain.order_no
JOIN Product ON Contain.sku = Product.sku
GROUP BY Sale.order_no;