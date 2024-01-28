-- selecionando o sellers 
SELECT 
	*
FROM public.olist_sellers_dataset

-- selecionando o seller_id e seller_satate
SELECT 
	seller_id,
	seller_state
FROM public.olist_sellers_dataset

-- seleciona somente o seller_id e a city
SELECT
	seller_id, 
	seller_city
FROM public.olist_sellers_dataset 


-- buscando todas as tabelas do products 
SELECT 
	*
FROM public.olist_products_dataset


-- seleciona o product_id, product_category_name, product_photos_qty 
SELECT
	product_id,
	product_category_name,
	product_photos_qty
FROM public.olist_products_dataset

-- filtrando as linhas de somente produtos que são bebes e contem mais do que uma foto 
SELECT 
	product_id,
	product_category_name,
	product_photos_qty
FROM public.olist_products_dataset
WHERE product_category_name = 'bebes' and product_photos_qty > 1



-- filtrando as linhas de produtos que contem bebes e perfumes e mais de 1 
SELECT 
	product_id, 
	product_category_name, 
	product_photos_qty
FROM public.olist_products_dataset
WHERE (product_category_name = 'bebes' or product_category_name = 'perfumaria') 
AND product_photos_qty > 1


-- selecionadno perfumaria e bebes, bebes tem que ser acima de 1 e perfumaria acima de 5 
SELECT 
	t1.product_id,	
	t1.product_category_name,
	t1.product_photos_qty
FROM public.olist_products_dataset as t1 
WHERE (t1.product_category_name = 'bebes' and t1.product_photos_qty >1)
or (t1.product_category_name = 'perfumaria' and t1.product_photos_qty > 5)