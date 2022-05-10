CREATE TABLE potential_customers(
	id SERIAL PRIMARY KEY,
	email VARCHAR(255),
	name VARCHAR(255),
	surname VARCHAR(255),
	second_name VARCHAR(255),
	city VARCHAR(255)
);

INSERT INTO potential_customers(email, name, surname, second_name, city) VALUES
	('email1@gmail.com', 'Potential Customer 1', 'Surname', 'Second name', 'city 1'),
	('email2@gmail.com', 'Potential Customer 2', 'Surname', 'Second name', 'city 2'),
	('email3@gmail.com', 'Potential Customer 3', 'Surname', 'Second name', 'city 3'),
	('email4@gmail.com', 'Potential Customer 4', 'Surname', 'Second name', 'city 4'),
	('email5@gmail.com', 'Potential Customer 5', 'Surname', 'Second name', 'city 5'),
	('email6@gmail.com', 'Potential Customer 6', 'Surname', 'Second name', 'city 16'),
	('email7@gmail.com', 'Potential Customer 7', 'Surname', 'Second name', 'city 17'),
	('email8@gmail.com', 'Potential Customer 8', 'Surname', 'Second name', 'city 18'),
	('email9@gmail.com', 'Potential Customer 9', 'Surname', 'Second name', 'city 19'),
	('email10@gmail.com', 'Potential Customer 10', 'Surname', 'Second name', 'city 17'),
	('email11@gmail.com', 'Potential Customer 11', 'Surname', 'Second name', 'city 17'),
	('email12@gmail.com', 'Potential Customer 12', 'Surname', 'Second name', 'city 12'),
	('email13@gmail.com', 'Potential Customer 13', 'Surname', 'Second name', 'city 16'),
	('email14@gmail.com', 'Potential Customer 14', 'Surname', 'Second name', 'city 17'),
	('email15@gmail.com', 'Potential Customer 15', 'Surname', 'Second name', 'city 9'),
	('email16@gmail.com', 'Potential Customer 16', 'Surname', 'Second name', 'city 8'),
	('email17@gmail.com', 'Potential Customer 17', 'Surname', 'Second name', 'city 3'),
	('email18@gmail.com', 'Potential Customer 18', 'Surname', 'Second name', 'city 17'),
	('email19@gmail.com', 'Potential Customer 19', 'Surname', 'Second name', 'city 2'),
	('email20@gmail.com', 'Potential Customer 20', 'Surname', 'Second name', 'city 1');

SELECT first_name, last_name, email FROM users WHERE users.city = 'city 17'
UNION
SELECT name, surname, email FROM potential_customers WHERE potential_customers.city = 'city 17';
