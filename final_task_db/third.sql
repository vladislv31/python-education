CREATE OR REPLACE VIEW addresses_view AS
	SELECT house_number, street_name, city_name FROM addresses
		LEFT JOIN streets
			USING (street_id)
		LEFT JOIN cities
			USING (city_id);

CREATE OR REPLACE VIEW cars_view AS
	SELECT
		models.name AS model_name,
		manufacturers.manufacturer_name,
		cars.number AS car_number
	FROM cars
		LEFT JOIN models
			USING (model_id)
		LEFT JOIN manufacturers
			USING (manufacturer_id);

CREATE MATERIALIZED VIEW rentings_statistics AS
	SELECT
		date,
		period_days,
		first_name,
		last_name,
		phone,
		models.name AS model_name,
		cars.number AS car_number,
		cars.renting_price
	FROM rentings
		LEFT JOIN cars
			USING (car_id)
		LEFT JOIN models
			ON models.model_id = cars.model_id
		LEFT JOIN customers
			USING (customer_id)
	ORDER BY period_days DESC
WITH NO DATA;
