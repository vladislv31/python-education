SELECT users.first_name, users.last_name, status_name as status, orders.total
	FROM orders
	LEFT JOIN order_statuses
		ON order_statuses.id = orders.order_status_id
	LEFT JOIN carts
		ON carts.id = orders.cart_id
	LEFT JOIN users
		ON users.id = carts.user_id
    WHERE city = 'city 2761';

-- EXPLAIN

-- Nested Loop Left Join  (cost=137.93..171.62 rows=1 width=551) (actual time=2.593..3.445 rows=1 loops=1)
--    ->  Hash Join  (cost=137.79..171.42 rows=1 width=39) (actual time=2.575..3.425 rows=1 loops=1)
--          Hash Cond: (orders.cart_id = carts.id)
--          ->  Seq Scan on orders  (cost=0.00..28.00 rows=1500 width=14) (actual time=0.017..0.428 rows=1500 loops=1)
--          ->  Hash  (cost=137.77..137.77 rows=1 width=33) (actual time=2.424..2.427 rows=1 loops=1)
--                Buckets: 1024  Batches: 1  Memory Usage: 9kB
--                ->  Hash Join  (cost=97.51..137.77 rows=1 width=33) (actual time=1.337..2.423 rows=1 loops=1)
--                      Hash Cond: (carts.user_id = users.id)
--                      ->  Seq Scan on carts  (cost=0.00..35.00 rows=2000 width=8) (actual time=0.006..0.491 rows=2000 loops=1)
--                      ->  Hash  (cost=97.50..97.50 rows=1 width=33) (actual time=1.201..1.203 rows=1 loops=1)
--                            Buckets: 1024  Batches: 1  Memory Usage: 9kB
--                            ->  Seq Scan on users  (cost=0.00..97.50 rows=1 width=33) (actual time=0.094..1.197 rows=1 loops=1)
--                                  Filter: ((city)::text = 'city 200'::text)
--                                  Rows Removed by Filter: 2999
--    ->  Index Scan using order_statuses_pkey on order_statuses  (cost=0.14..0.19 rows=1 width=520) (actual time=0.012..0.012 rows=1 loops=1)
--          Index Cond: (id = orders.order_status_id)
--  Planning Time: 0.777 ms
--  Execution Time: 3.525 ms
-- (18 rows)

CREATE INDEX users_city_index ON users(city);
CREATE INDEX orders_cart_id_index ON orders(cart_id);
CREATE INDEX carts_user_id_index ON carts(user_id);

-- RESULT EXPLAIN

-- Nested Loop Left Join  (cost=0.98..17.14 rows=1 width=551) (actual time=0.133..0.141 rows=1 loops=1)
--    ->  Nested Loop  (cost=0.84..16.95 rows=1 width=39) (actual time=0.124..0.131 rows=1 loops=1)
--          ->  Nested Loop  (cost=0.56..16.60 rows=1 width=33) (actual time=0.104..0.108 rows=1 loops=1)
--                ->  Index Scan using users_city_index on users  (cost=0.28..8.30 rows=1 width=33) (actual time=0.078..0.079 rows=1 loops=1)
--                      Index Cond: ((city)::text = 'city 200'::text)
--                ->  Index Scan using carts_user_id_index on carts  (cost=0.28..8.29 rows=1 width=8) (actual time=0.018..0.019 rows=1 loops=1)
--                      Index Cond: (user_id = users.id)
--          ->  Index Scan using orders_cart_id_index on orders  (cost=0.28..0.33 rows=1 width=14) (actual time=0.016..0.018 rows=1 loops=1)
--                Index Cond: (cart_id = carts.id)
--    ->  Index Scan using order_statuses_pkey on order_statuses  (cost=0.14..0.19 rows=1 width=520) (actual time=0.005..0.006 rows=1 loops=1)
--          Index Cond: (id = orders.order_status_id)
--  Planning Time: 2.017 ms
--  Execution Time: 0.211 ms
-- (13 rows)
