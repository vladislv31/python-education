SELECT users.first_name, users.last_name, carts.id AS cart_id, array_agg(cart_products.product_id) FROM users
	LEFT JOIN
		carts ON carts.user_id = users.id
	LEFT JOIN
		cart_products ON cart_products.cart_id = carts.id
	WHERE users.first_name = 'first_name 1115'
	GROUP BY (users.first_name, users.last_name, carts.id);

-- EXPLAIN

-- GroupAggregate  (cost=338.08..338.20 rows=5 width=65)
--    Group Key: users.first_name, users.last_name, carts.id
--    ->  Sort  (cost=338.08..338.09 rows=5 width=37)
--          Sort Key: users.last_name, carts.id
--          ->  Hash Right Join  (cost=137.79..338.02 rows=5 width=37)
--                Hash Cond: (cart_products.cart_id = carts.id)
--                ->  Seq Scan on cart_products  (cost=0.00..158.95 rows=10995 width=8)
--                ->  Hash  (cost=137.77..137.77 rows=1 width=33)
--                      ->  Hash Right Join  (cost=97.51..137.77 rows=1 width=33)
--                            Hash Cond: (carts.user_id = users.id)
--                            ->  Seq Scan on carts  (cost=0.00..35.00 rows=2000 width=8)
--                            ->  Hash  (cost=97.50..97.50 rows=1 width=33)
--                                  ->  Seq Scan on users  (cost=0.00..97.50 rows=1 width=33)
--                                        Filter: ((first_name)::text = 'first_name 1115'::text)
-- (14 rows)

CREATE INDEX users_first_name_index ON users(first_name);
CREATE INDEX carts_user_id_index ON carts(user_id);
CREATE INDEX cart_products_cart_id_index ON cart_products(cart_id);

-- RESULT EXPLAIN

-- GroupAggregate  (cost=17.22..17.34 rows=5 width=65)
--    Group Key: users.first_name, users.last_name, carts.id
--    ->  Sort  (cost=17.22..17.23 rows=5 width=37)
--          Sort Key: users.last_name, carts.id
--          ->  Nested Loop Left Join  (cost=0.84..17.16 rows=5 width=37)
--                ->  Nested Loop Left Join  (cost=0.56..16.60 rows=1 width=33)
--                      ->  Index Scan using users_first_name_index on users  (cost=0.28..8.30 rows=1 width=33)
--                            Index Cond: ((first_name)::text = 'first_name 1115'::text)
--                      ->  Index Scan using carts_user_id_index on carts  (cost=0.28..8.29 rows=1 width=8)
--                            Index Cond: (user_id = users.id)
--                ->  Index Scan using cart_products_cart_id_index on cart_products  (cost=0.29..0.51 rows=5 width=8)
--                      Index Cond: (cart_id = carts.id)
-- (12 rows)
