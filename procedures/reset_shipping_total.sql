CREATE OR REPLACE FUNCTION reset_shipping_total(user_city varchar(255))
RETURNS integer
AS $$
DECLARE
	shipping_total integer := 10;
	orders_ids integer ARRAY;
BEGIN
	SELECT array_agg(orders.id) INTO orders_ids
		FROM users
		INNER JOIN users u2
			ON u2.id = users.id
				AND u2.city = user_city
		LEFT JOIN carts
			ON carts.user_id = users.id
		LEFT JOIN orders
			ON orders.cart_id = carts.id;
			
	SELECT sum(orders.shipping_total) INTO shipping_total
		FROM orders
		WHERE
			id = ANY(orders_ids);
			
	if shipping_total <> 0
	THEN
		UPDATE orders
			SET shipping_total = 0
			WHERE
				id = ANY(orders_ids);
	END IF;
				
	RETURN shipping_total;
END;
$$ LANGUAGE plpgsql;

SELECT reset_shipping_total('city 13');
