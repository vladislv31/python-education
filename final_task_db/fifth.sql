CREATE OR REPLACE PROCEDURE add_car(car_model_id INTEGER, car_number INTEGER, car_renting_price INTEGER, car_branch_id INTEGER)
AS $$
BEGIN
	INSERT INTO cars (model_id, number, renting_price, branch_id)
		VALUES (car_model_id, car_number, car_renting_price, car_branch_id);
		
	IF car_renting_price <= 0 THEN
		ROLLBACK;
	END IF;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE PROCEDURE change_car_branch_with_clean_up(car_id_ INTEGER, new_branch_id INTEGER)
AS $$
DECLARE
	old_branch_id INTEGER;
	old_branch_using INTEGER;
BEGIN
	SELECT branch_id INTO old_branch_id
		FROM cars
		WHERE car_id = car_id_;
		
	UPDATE cars
		SET branch_id = new_branch_id
		WHERE car_id = car_id_;
		
	SELECT COUNT(*) INTO old_branch_using
		FROM cars
		WHERE branch_id = old_branch_id;
		
	IF old_branch_using < 1 THEN
		DELETE FROM branches WHERE branch_id = old_branch_id;
	END IF;
END;
$$ LANGUAGE plpgsql;
