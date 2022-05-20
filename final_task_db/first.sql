CREATE DATABASE cars_renting;

-- Creating tables

CREATE TABLE cities(
	city_id SERIAL PRIMARY KEY,
	city_name VARCHAR(255)
);

CREATE TABLE streets(
	street_id SERIAL PRIMARY KEY,
	city_id INTEGER REFERENCES cities(city_id),
    street_name VARCHAR(255)
);

CREATE TABLE addresses(
	address_id SERIAL PRIMARY KEY,
	street_id INTEGER REFERENCES streets(street_id),
    house_number INTEGER
);

CREATE TABLE branches(
	branch_id SERIAL PRIMARY KEY,
	number INTEGER,
	address_id INTEGER REFERENCES addresses(address_id),
    phone INTEGER
);

CREATE TABLE customers(
	customer_id SERIAL PRIMARY KEY,
	first_name VARCHAR(255),
	last_name VARCHAR(255),
	address_id INTEGER REFERENCES addresses(address_id),
	phone INTEGER
);

CREATE TABLE manufacturers(
	manufacturer_id SERIAL PRIMARY KEY,
	manufacturer_name VARCHAR(255)
);

CREATE TABLE models(
	model_id SERIAL PRIMARY KEY,
	manufacturer_id INTEGER REFERENCES manufacturers(manufacturer_id),
	name VARCHAR(255)
);

CREATE TABLE cars(
	car_id SERIAL PRIMARY KEY,
	model_id INTEGER REFERENCES models(model_id),
	number INTEGER UNIQUE,
	renting_price INTEGER,
	branch_id INTEGER REFERENCES branches(branch_id)
);

CREATE TABLE rentings(
	renting_id SERIAL PRIMARY KEY,
	date TIMESTAMP,
	period_days INTEGER,
	customer_id INTEGER REFERENCES customers(customer_id),
	car_id INTEGER REFERENCES cars(car_id)
);

-- Generating data

INSERT INTO cities(city_name)
	SELECT CONCAT('City ', i)
		FROM generate_series(1, 100) i;

INSERT INTO streets(city_id, street_name)
	SELECT i, CONCAT('City ', i)
		FROM generate_series(1, 100) i;

INSERT INTO addresses(street_id, house_number)
	SELECT i, i
		FROM generate_series(1, 100) i;

INSERT INTO customers(first_name, last_name, address_id, phone)
	SELECT CONCAT('First name ', i), CONCAT('Last name ', i), i, (i * 10000000 * RANDOM())::integer % 10000000000
		FROM generate_series(1, 100) i;

INSERT INTO branches(number, address_id, phone)
	SELECT i, i, (i * 10000000 * RANDOM())::integer % 10000000000
		FROM generate_series(1, 100) i;

INSERT INTO manufacturers(manufacturer_name)
	SELECT CONCAT('Manufacturer ', i)
		FROM generate_series(1, 50) i;

INSERT INTO models(manufacturer_id, name)
	SELECT i, CONCAT('Model ', i)
		FROM generate_series(1, 50) i;

INSERT INTO cars(model_id, number, renting_price, branch_id)
	SELECT i, floor(random() * (9999 - 1000 + 1) + 1000)::int, floor(random() * (100 - 10 + 1) + 10)::int,
			floor(random() * (100 - 1 + 1) + 1)::int
		FROM generate_series(1, 50) i;

INSERT INTO rentings(date, period_days, customer_id, car_id)
	SELECT CURRENT_TIMESTAMP, floor(random() * (10 - 1 + 1) + 1)::int, floor(random() * (100 - 1 + 1) + 1)::int,
			floor(random() * (50 - 1 + 1) + 1)::int
		FROM generate_series(1, 5000);
