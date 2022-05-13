SELECT products.product_title, array_agg(carts.id) AS inside_carts FROM products
	LEFT JOIN cart_products
		ON cart_products.product_id = products.id
	LEFT JOIN carts
		ON carts.id = cart_products.cart_id
	WHERE products.product_title = 'Product 1146'
	GROUP BY products.product_title;

-- EXPLAIN

-- GroupAggregate  (cost=162.29..350.78 rows=1 width=44) (actual time=8.312..8.317 rows=1 loops=1)
--    Group Key: products.product_title
--    ->  Nested Loop Left Join  (cost=162.29..350.75 rows=3 width=16) (actual time=1.511..8.296 rows=3 loops=1)
--          ->  Hash Right Join  (cost=162.01..349.86 rows=3 width=16) (actual time=1.495..8.250 rows=3 loops=1)
--                Hash Cond: (cart_products.product_id = products.id)
--                ->  Seq Scan on cart_products  (cost=0.00..158.95 rows=10995 width=8) (actual time=0.015..2.949 rows=10995 loops=1)
--                ->  Hash  (cost=162.00..162.00 rows=1 width=16) (actual time=1.350..1.351 rows=1 loops=1)
--                      Buckets: 1024  Batches: 1  Memory Usage: 9kB
--                      ->  Seq Scan on products  (cost=0.00..162.00 rows=1 width=16) (actual time=0.394..1.344 rows=1 loops=1)
--                            Filter: ((product_title)::text = 'Product 1146'::text)
--                            Rows Removed by Filter: 3999
--          ->  Index Only Scan using carts_pkey on carts  (cost=0.28..0.30 rows=1 width=4) (actual time=0.012..0.012 rows=1 loops=3)
--                Index Cond: (id = cart_products.cart_id)
--                Heap Fetches: 0
--  Planning Time: 0.755 ms
--  Execution Time: 8.395 ms
-- (16 rows)

CREATE INDEX products_product_title_index ON products(product_title);
CREATE INDEX cart_products_product_id_index ON cart_products(product_id);

-- RESULT EXPLAIN

-- GroupAggregate  (cost=4.88..22.95 rows=1 width=44) (actual time=0.206..0.210 rows=1 loops=1)
--    Group Key: products.product_title
--    ->  Nested Loop Left Join  (cost=4.88..22.92 rows=3 width=16) (actual time=0.161..0.193 rows=3 loops=1)
--          ->  Index Scan using products_product_title_index on products  (cost=0.28..8.30 rows=1 width=16) (actual time=0.092..0.094 rows=1 loops=1)
--                Index Cond: ((product_title)::text = 'Product 1146'::text)
--          ->  Nested Loop Left Join  (cost=4.60..14.60 rows=3 width=8) (actual time=0.064..0.091 rows=3 loops=1)
--                ->  Bitmap Heap Scan on cart_products  (cost=4.31..14.12 rows=3 width=8) (actual time=0.038..0.047 rows=3 loops=1)
--                      Recheck Cond: (product_id = products.id)
--                      Heap Blocks: exact=3
--                      ->  Bitmap Index Scan on cart_products_product_id_index  (cost=0.00..4.31 rows=3 width=0) (actual time=0.026..0.026 rows=3 loops=1
-- )
--                            Index Cond: (product_id = products.id)
--                ->  Memoize  (cost=0.29..0.31 rows=1 width=4) (actual time=0.009..0.009 rows=1 loops=3)
--                      Cache Key: cart_products.cart_id
--                      Cache Mode: logical
--                      Hits: 0  Misses: 3  Evictions: 0  Overflows: 0  Memory Usage: 1kB
--                      ->  Index Only Scan using carts_pkey on carts  (cost=0.28..0.30 rows=1 width=4) (actual time=0.005..0.005 rows=1 loops=3)
--                            Index Cond: (id = cart_products.cart_id)
--                            Heap Fetches: 0
--  Planning Time: 0.757 ms
--  Execution Time: 0.320 ms
-- (20 rows)

