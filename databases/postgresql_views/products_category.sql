SELECT products.product_title, products.product_description,
	products.in_stock, products.price, categories.category_title,
	categories.category_description FROM products
	LEFT JOIN categories
		ON categories.id = products.category_id;
		
CREATE OR REPLACE VIEW products_with_cats AS
	SELECT products.product_title, products.product_description,
		products.in_stock, products.price, categories.category_title,
		categories.category_description FROM products
		LEFT JOIN categories
			ON categories.id = products.category_id;
			
SELECT * FROM products_with_cats;
SELECT * FROM products_with_cats
	WHERE in_stock > 10;
	
DROP VIEW IF EXISTS products_with_cats;
