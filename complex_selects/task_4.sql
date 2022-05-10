SELECT products.* FROM products
	LEFT JOIN cart_products ON cart_products.product_id = products.id
	WHERE cart_products.cart_id is NULL;

SELECT * FROM products WHERE id NOT IN
	(SELECT cart_products.product_id FROM orders
	 	LEFT JOIN cart_products
	 	ON cart_products.cart_id = orders.cart_id);

SELECT products.* FROM products
	LEFT JOIN cart_products ON cart_products.product_id = products.id
	GROUP BY products.id ORDER BY COUNT(cart_products.cart_id)
	DESC LIMIT 10;

SELECT products.*, COUNT(orders.id) FROM products
	LEFT JOIN cart_products ON cart_products.product_id = products.id
	LEFT JOIN orders ON orders.cart_id = cart_products.cart_id
	GROUP BY products.id ORDER BY COUNT(orders.id) DESC
	LIMIT 10;

SELECT users.* FROM orders
	LEFT JOIN carts ON carts.id = orders.cart_id
	LEFT JOIN users ON users.id = carts.user_id
	GROUP BY users.id ORDER BY sum(orders.total) DESC
	LIMIT 5;

SELECT users.* FROM orders
	LEFT JOIN carts ON carts.id = orders.cart_id
	LEFT JOIN users ON users.id = carts.user_id
	GROUP BY users.id ORDER BY cardinality(array_agg(orders.id)) DESC
	LIMIT 5;

SELECT users.* FROM users
	LEFT JOIN carts ON carts.user_id = users.id
	WHERE carts.id NOT IN (SELECT cart_id FROM orders)
	GROUP BY users.id ORDER BY sum(carts.total) DESC
	LIMIT 5;
