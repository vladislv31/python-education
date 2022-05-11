BEGIN;

INSERT INTO potential_customers(email, name, surname, second_name, city)
    VALUES('testuser@gmail.com', 'Ivan', 'Ivanov', 'Ivanovich', 'New york');

SELECT * FROM potential_customers ORDER BY id DESC LIMIT 1;

UPDATE potential_customers SET surname = 'Ivanovsky' WHERE id = 41;
SELECT * FROM potential_customers ORDER BY id DESC LIMIT 1;
SAVEPOINT no_bad_data;

UPDATE potential_customers SET surname = 'Bad surname' WHERE id = 41;
SELECT * FROM potential_customers ORDER BY id DESC LIMIT 1;
ROLLBACK TO SAVEPOINT no_bad_data;
SELECT * FROM potential_customers ORDER BY id DESC LIMIT 1;

SAVEPOINT no_deleted;
DELETE FROM potential_customers;
ROLLBACK TO SAVEPOINT no_deleted;

COMMIT;
