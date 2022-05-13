SELECT
		products.product_title,
		products.product_description,
		products.in_stock,
		products.price,
		COUNT(orders) AS used_in_orders
	FROM products
	LEFT JOIN cart_products
		ON cart_products.product_id = products.id
	LEFT JOIN carts
		ON carts.id = cart_products.cart_id
	LEFT JOIN orders
		ON orders.cart_id = carts.id
	GROUP BY
		products.product_title,
		products.product_description,
		products.in_stock,
		products.price;
		
CREATE MATERIALIZED VIEW products_stat AS
	SELECT
			products.product_title,
			products.product_description,
			products.in_stock,
			products.price,
			COUNT(orders) AS used_in_orders
		FROM products
		LEFT JOIN cart_products
			ON cart_products.product_id = products.id
		LEFT JOIN carts
			ON carts.id = cart_products.cart_id
		LEFT JOIN orders
			ON orders.cart_id = carts.id
		GROUP BY
			products.product_title,
			products.product_description,
			products.in_stock,
			products.price
	WITH NO DATA;

REFRESH MATERIALIZED VIEW products_stat;

SELECT * FROM products_stat;

DROP MATERIALIZED VIEW products_stat;
