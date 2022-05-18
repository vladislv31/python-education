/* Firstly, procedure clears current potential customers.
	Then comparing users orders shipping_total with argument, inserts new potential customers.
*/

CREATE OR REPLACE PROCEDURE refresh_potential_customers(min_shipping_total integer)
AS $$
DECLARE
	usr record;
BEGIN
	TRUNCATE potential_customers;
	
	FOR usr IN
		SELECT users.*, sum(shipping_total) AS shipping_total
			FROM users
			LEFT JOIN carts
				ON carts.user_id = users.id
			LEFT JOIN orders
				ON orders.cart_id = carts.id
			GROUP BY users.id
	LOOP
		IF usr.shipping_total > min_shipping_total
		THEN
			INSERT INTO potential_customers(email, name, surname, second_name, city)
				VALUES (usr.email, usr.first_name, usr.last_name, usr.middle_name, usr.city);
		END IF;
	END LOOP;
	
	COMMIT;
END;
$$ LANGUAGE plpgsql;

CALL refresh_potential_customers(100);
