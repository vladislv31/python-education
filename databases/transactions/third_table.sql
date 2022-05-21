BEGIN;

INSERT INTO order_statuses(id, status_name)
    VALUES(6, 'Customer escaped');

SAVEPOINT no_updated;
UPDATE order_statuses SET status_name = 'Some shit' WHERE id = 6;
SELECT * FROM order_statuses;
ROLLBACK TO SAVEPOINT no_updated;

SELECT * FROM order_statuses;

SAVEPOINT no_deleted;
DELETE FROM order_statuses;

SELECT * FROM order_statuses;
ROLLBACK TO SAVEPOINT no_deleted;
SELECT * FROM order_statuses;

COMMIT;
