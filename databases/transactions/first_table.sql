BEGIN;

INSERT INTO categories(id, category_title, category_description) 
    VALUES(21, 'Test cat', 'Test category');

UPDATE categories SET category_description = 'Changed description' 
    WHERE id = 21;

SAVEPOINT no_deleted_all;

DELETE FROM categories;

SELECT * FROM categories;
ROLLBACK TO SAVEPOINT no_deleted_all;
SELECT * FROM categories;

SELECT * FROM users LIMIT 10;

COMMIT;
