CREATE TABLE cars_numbers_audit(car_id INTEGER, number INTEGER);

CREATE OR REPLACE FUNCTION update_car_number_trigger_handler()
RETURNS TRIGGER
AS $$
BEGIN
	IF NEW.number <> OLD.number THEN
		INSERT INTO cars_numbers_audit(car_id, number)
			VALUES(OLD.car_id, OLD.number);
	END IF;
	RETURN NULL;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER after_car_update
	AFTER UPDATE
	ON cars
	FOR EACH ROW
	EXECUTE PROCEDURE update_car_number_trigger_handler();

------------

CREATE OR REPLACE FUNCTION update_customer_phone_trigger_handler()
RETURNS TRIGGER
AS $$
BEGIN
	IF NEW.phone >= 9999999999 THEN
		RAISE 'Bad phone.';
	END IF;
	RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER before_update_customer_phone
	BEFORE UPDATE
	ON customers
	FOR EACH ROW
	EXECUTE PROCEDURE update_customer_phone_trigger_handler();
