-- Handler validates price. Price must be more than more. Also it refreshing total rows in orders
CREATE OR REPLACE FUNCTION recount_total_when_change_price()
RETURNS TRIGGER
AS $$
DECLARE
	price_difference integer;
	orders_ids integer ARRAY;
BEGIN
	price_difference := NEW.price - OLD.price;
	
	-- Refresh total in orders
	SELECT array_agg(orders.id) INTO orders_ids FROM orders
	INNER JOIN cart_products
		ON cart_products.cart_id = orders.cart_id
			AND cart_products.product_id = NEW.id;
			
	UPDATE orders SET total = total + price_difference
		WHERE id = ANY(orders_ids);
		
	IF NEW.price <= 0 THEN
		RAISE EXCEPTION 'Price must be more than zero.';
	END IF;
	
	RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Trigger executes handler for each row before insert or update product
CREATE OR REPLACE TRIGGER validate_product_price_trigger
	BEFORE INSERT OR UPDATE
	ON products
	FOR EACH ROW
	EXECUTE PROCEDURE recount_total_when_change_price();
