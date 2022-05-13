SELECT id, product_title, product_description, in_stock, price, slug
	FROM products
	WHERE category_id = 10 AND price >= 100;
	
CREATE OR REPLACE VIEW expensive_products_10_cat AS
	SELECT id, product_title, product_description, in_stock, price, slug
		FROM products
		WHERE category_id = 10 AND price >= 100;
		
SELECT * FROM expensive_products_10_cat;
SELECT * FROM expensive_products_10_cat
	WHERE in_stock >= 5;

DROP VIEW IF EXISTS expensive_products_10_cat;
