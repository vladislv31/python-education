CREATE OR REPLACE FUNCTION get_rentings_by_period(low integer, high integer)
RETURNS TABLE (
	renting_date TIMESTAMP,
	period_days INTEGER,
	renting_price INTEGER,
	model_name VARCHAR(255),
	first_name VARCHAR(255),
	last_name VARCHAR(255)
)
AS $$
BEGIN
	RETURN QUERY
		SELECT
			rentings.date AS renting_date,
			rentings.period_days,
			cars.renting_price,
			models.name AS model_name,
			customers.first_name,
			customers.last_name
		FROM rentings
			LEFT JOIN cars
				ON cars.car_id = rentings.car_id
			LEFT JOIN models
				ON models.model_id = cars.model_id
			LEFT JOIN customers
				ON customers.customer_id = rentings.customer_id
		WHERE rentings.period_days BETWEEN low AND high;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION increase_renting_price(model_name VARCHAR(255), percentage NUMERIC)
RETURNS INTEGER
AS $$
DECLARE
	car_id_ INTEGER;
	cars_updated INTEGER := 0;
BEGIN
	FOR car_id_ IN
		SELECT cars.car_id
		FROM cars
			LEFT JOIN models
				ON models.model_id = cars.car_id
		WHERE models.name = model_name
	LOOP
		UPDATE cars
			SET renting_price = renting_price + renting_price * percentage
			WHERE cars.car_id = car_id_;
		cars_updated := cars_updated + 1;
	END LOOP;
	
	RETURN cars_updated;
END;
$$ LANGuAGE plpgsql;

CREATE OR REPLACE FUNCTION rise_in_price(percentage NUMERIC, rise_from INTEGER)
RETURNS INTEGER
AS $$
DECLARE
	car_rec record;
	car_cur CURSOR FOR
		SELECT * FROM cars;
	cars_updated INTEGER := 0;
BEGIN
	OPEN car_cur;
	
	LOOP
		FETCH car_cur INTO car_rec;
		EXIT WHEN NOT FOUND;
		IF car_rec.renting_price >= rise_from THEN
			UPDATE cars
				SET renting_price = renting_price + renting_price * percentage
				WHERE CURRENT OF car_cur;
			cars_updated := cars_updated + 1;
		END IF;
	END LOOP;
	CLOSE car_cur;
	RETURN cars_updated;
END;
$$ LANGUAGE plpgsql;
