/* Increasing product price according to in_stock and total in orders rows */

CREATE OR REPLACE PROCEDURE increase_products_price()
AS $$
DECLARE
	product record;
BEGIN
	FOR product IN
		SELECT cart_products.product_id, products.in_stock FROM orders
			INNER JOIN orders o2
				ON o2.id = orders.id
					AND o2.total > 1000
			LEFT JOIN carts
				ON carts.id = orders.cart_id
			LEFT JOIN cart_products
				ON cart_products.cart_id = carts.id
			LEFT JOIN products
				ON products.id = cart_products.product_id
	LOOP
		IF product.in_stock > 40
		THEN
			UPDATE products
				SET price = price * 1.25
				WHERE id = product.product_id;
		END IF;
	END LOOP;
	COMMIT;
END;
$$ LANGUAGE plpgsql;

CALL increase_products_price();
