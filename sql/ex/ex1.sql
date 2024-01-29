-- quantos produtos temos na categoria artes
SELECT 
	COUNT(*) as qtd_itens
FROM public.olist_products_dataset as contagem
WHERE product_category_name = 'artes'

-- quantos produtos tem mais de 5 litos
SELECT
	*
FROM public.olist_products_dataset