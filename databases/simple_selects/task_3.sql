SELECT * FROM products WHERE price > 80.00 AND price <= 150.00;
SELECT * FROM orders WHERE created_at > '01.10.2020';
SELECT * FROM orders WHERE created_at BETWEEN '01.01.2020' AND '06.30.2020';
SELECT * FROM products WHERE category_id IN (7, 11, 18);
SELECT * FROM orders WHERE order_status_id = 2 AND created_at = '12.31.2020';
SELECT * FROM carts WHERE id NOT IN (SELECT cart_id FROM orders);
