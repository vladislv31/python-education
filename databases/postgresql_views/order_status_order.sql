SELECT orders.id, orders.shipping_total, orders.total, order_statuses.status_name FROM orders
	LEFT JOIN order_statuses
		ON order_statuses.id = orders.order_status_id;
		
CREATE OR REPLACE VIEW orders_with_statuses AS
	SELECT orders.id, orders.shipping_total, orders.total, order_statuses.status_name FROM orders
		LEFT JOIN order_statuses
			ON order_statuses.id = orders.order_status_id;
			
SELECT * FROM orders_with_statuses;

DROP VIEW IF EXISTS orders_with_statuses;
