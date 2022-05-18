/* Makes user as manager if he has order total's value more than argument*/

CREATE OR REPLACE PROCEDURE make_user_staff_by_total(min_total integer)
AS $$
DECLARE
	user_id integer;
BEGIN
	FOR user_id IN
		SELECT users.id FROM orders
			INNER JOIN orders o2
				ON o2.id = orders.id
					AND o2.total > min_total
			LEFT JOIN carts
				ON carts.id = orders.cart_id
			LEFT JOIN users
				ON users.id = carts.user_id
	LOOP
		UPDATE users
			SET is_staff = 1
			WHERE id = user_id;
	END LOOP;
	COMMIT;
END;
$$ LANGUAGE plpgsql;

CALL make_user_staff_by_total(100);
