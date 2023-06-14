SELECT
    SUM(ps.qty) AS total_quantity,
    SUM(ps.total_price) AS total_value,
    ps.city,
    ps.year,
    ps.month,
    ps.day_of_month,
    ps.day_of_week
FROM
    product_sales ps
WHERE
    ps.year = 2022
GROUP BY
    GROUPING SETS (
        (ps.city, ps.year, ps.month, ps.day_of_month, ps.day_of_week)
    )
ORDER BY
    ps.city, ps.year, ps.month, ps.day_of_month, ps.day_of_week;


SELECT month, day_of_week, AVG(total_price) as medium_value
FROM product_sales
WHERE year = '2022'
GROUP BY
    ROLLUP(month, day_of_week)
ORDER BY month, day_of_week
