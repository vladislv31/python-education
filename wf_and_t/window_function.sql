SELECT
	category_title,
	product_title,
	price,
	AVG(price)
		OVER(PARTITION BY category_id) 
	FROM products
	LEFT JOIN categories
		ON categories.id = products.category_id;
