SELECT
    date,
    period_days,
    renting_price,
    models.name AS model_name,
    first_name,
    last_name
FROM rentings
	LEFT JOIN cars
		USING (car_id)
	LEFT JOIN models
		ON models.model_id = cars.model_id
	LEFT JOIN customers
		USING (customer_id);

-------------

SELECT house_number, street_name, city_name FROM addresses
	LEFT JOIN streets
		USING (street_id)
	LEFT JOIN cities
		USING (city_id);

-------------

SELECT period_days, models.name AS car_model, date FROM rentings
	LEFT JOIN cars
		ON cars.car_id = rentings.car_id
	INNER JOIN models
		ON models.model_id = cars.model_id
			AND models.model_id = 25;

CREATE INDEX idx_cars_model_id ON cars(model_id);
CREATE INDEX idx_rentings_car_id ON rentings(car_id);
