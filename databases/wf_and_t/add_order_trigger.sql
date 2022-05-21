-- Trigger handler for adding order. Check initial order status and inserted total for true.
CREATE OR REPLACE FUNCTION add_order_trigger_handler()
RETURNS TRIGGER
AS $$
DECLARE
	total_price numeric;
BEGIN
	IF NEW.order_status_id <> 1 THEN
		RAISE EXCEPTION 'Wrong initial order status.';
	END IF;
	
	SELECT SUM(products.price) INTO total_price FROM cart_products
		INNER JOIN cart_products c2
			ON c2.product_id = cart_products.product_id
				AND c2.product_id = 4
		LEFT JOIN products
			ON products.id = cart_products.product_id;
			
	IF NEW.total <> NEW.shipping_total + total_price THEN
		RAISE 'Order total must be %!', total_price + NEW.shipping_total;
	END IF;
	
	RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Calling trigger handler before insert.
CREATE OR REPLACE TRIGGER validate_adding_new_order
	BEFORE INSERT
	ON orders
	FOR EACH ROW
	EXECUTE PROCEDURE add_order_trigger_handler();
