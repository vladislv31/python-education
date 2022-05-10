SELECT categories.category_title, COUNT(products.id) AS "products_count" FROM categories
LEFT JOIN products ON products.category_id = categories.id
GROUP BY categories.category_title
ORDER BY products_count DESC;
