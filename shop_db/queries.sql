CREATE TABLE users(id SERIAL PRIMARY KEY, email VARCHAR(255), password VARCHAR(255), first_name VARCHAR(255), last_name VARCHAR(255), middle_name VARCHAR(255), is_staff SMALLINT, country VARCHAR(255), city VARCHAR(255), address TEXT);

CREATE TABLE carts(id SERIAL PRIMARY KEY, user_id INTEGER, subtotal DECIMAL, total DECIMAL, timestamp TIMESTAMP(2), FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE);

CREATE TABLE order_statuses(id SERIAL PRIMARY KEY, status_name VARCHAR(255));

CREATE TABLE orders(id SERIAL PRIMARY KEY, cart_id INTEGER, order_status_id INTEGER, shipping_total DECIMAL, total DECIMAL, created_at TIMESTAMP(2), updated_at TIMESTAMP(2), FOREIGN KEY (cart_id) REFERENCES carts(id) ON DELETE CASCADE, FOREIGN KEY (order_status_id) REFERENCES order_statuses(id) ON DELETE CASCADE);

CREATE TABLE categories(id SERIAL PRIMARY KEY, category_title VARCHAR(255), category_description TEXT);

CREATE TABLE products(id SERIAL PRIMARY KEY, product_title VARCHAR(255), product_description TEXT, in_stock INTEGER, price DECIMAL, slug VARCHAR(255), category_id INTEGER, FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE CASCADE);

CREATE TABLE cart_products(cart_id INTEGER, product_id INTEGER, FOREIGN KEY (cart_id) REFERENCES carts(id) ON DELETE CASCADE, FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE);

COPY users FROM '/usr/src/users.csv' DELIMITER ',' CSV;
COPY categories FROM '/usr/src/categories.csv' DELIMITER ',' CSV;
COPY order_statuses FROM '/usr/src/order_statuses.csv' DELIMITER ',' CSV;
COPY products FROM '/usr/src/products.csv' DELIMITER ',' CSV;
COPY carts FROM '/usr/src/carts.csv' DELIMITER ',' CSV;
COPY cart_products FROM '/usr/src/cart_products.csv' DELIMITER ',' CSV;
COPY orders FROM '/usr/src/orders.csv' DELIMITER ',' CSV;

ALTER TABLE users ADD COLUMN phone_number INTEGER;
ALTER TABLE users ALTER COLUMN phone_number TYPE VARCHAR(255);

UPDATE products SET price = price * 2;
