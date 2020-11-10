CREATE TABLE transactions
(
    date DATE,
    order_id VARCHAR(4),
    client_id VARCHAR(3),
    prod_id VARCHAR(6),
    prod_price DECIMAL(6,2),
    prod_qty INT,
    PRIMARY KEY (order_id, client_id, prod_id)
);

INSERT INTO transactions (date, order_id, client_id, prod_id, prod_price, prod_qty)
VALUES 
('2019-01-01', '1234', '999', 490756, 50, 1),
('2019-01-01', '1234', '999', 389728, 3.56, 4),
('2019-01-01', '3456', '845', 490756, 50, 2),
('2019-01-01', '3456', '845', 549380, 300, 1),
('2019-01-01', '3456', '845', 293718, 10, 6),
('2019-01-01', '1689', '670', 293718, 10, 1),
('2019-01-02', '6789', '425', 741589, 30, 1),
('2019-01-02', '6789', '425', 854167, 25.99, 2),
('2019-01-02', '6789', '425', 293718, 10, 4),
('2019-01-02', '2563', '670', 644586, 20, 3),
('2019-01-02', '2563', '670', 293718, 10, 2),
('2019-01-02', '1214', '845', 389728, 3.56, 10),
('2019-01-02', '2574', '999', 389728, 3.56, 2);

select * from transactions;

-------------PART 1----------------------

SELECT date, SUM(prod_qty * prod_price) AS ventes
FROM transactions
WHERE date BETWEEN '2019-01-01' AND '2019-12-31'
GROUP BY date
ORDER BY date;

---> OK
-- 534.24: 01 janvier 2019
-- 244.7: 02 Janvier 2019


-------------PART 2----------------------

CREATE TABLE PRODUCT_NOMENCLATURE(
    product_id VARCHAR(6),
    product_type VARCHAR(20),
    product_name VARCHAR(50),
    PRIMARY KEY (product_id)
);

INSERT INTO PRODUCT_NOMENCLATURE (product_id, product_type, product_name)
VALUES
('490756', 'MEUBLE', 'chaise'),
('389728', 'DECO', 'boule de Noël'),
('549380', 'MEUBLE', 'Canapé'),
('293718', 'DECO', 'Mug'),
('741589', 'DECO', 'Cadran horloge'),
('854167', 'MEUBLE', 'Tabouret'),
('644586', 'DECO', 'Guirlandes électriques');


---- With Full Outer: not tested -----

SELECT COALESCE(t_meubles.client_id,t_deco.client_id) AS client_id,
IFNULL(t_meubles.ventes_meubles, 0) AS ventes_meubles,
IFNULL(t_deco.ventes_deco, 0) AS ventes_deco
FROM (
  SELECT tp.client_id, SUM(tp.prod_price * tp.prod_qty) AS ventes_meubles
  FROM (
  	SELECT * FROM transactions t JOIN PRODUCT_NOMENCLATURE p ON t.prod_id=p.product_id
  	WHERE product_type LIKE 'MEUBLE' AND t.date BETWEEN '2019-01-01' and '2019-12-31'
	    ) tp
	GROUP BY tp.client_id
  	) t_meubles
FULL OUTER JOIN (
  SELECT tp.client_id, SUM(tp.prod_price * tp.prod_qty) AS ventes_deco
  FROM (
  	SELECT * FROM transactions t JOIN PRODUCT_NOMENCLATURE p ON t.prod_id=p.product_id
  	WHERE product_type LIKE 'DECO' AND t.date BETWEEN '2019-01-01' and '2019-12-31'
	    ) tp
	GROUP BY tp.client_id
  	) t_deco
ON t_meubles.client_id = t_deco.client_id
where t_meubles.client_id IS NULL OR t_deco.client_id IS NULL ;




---- Without Full Outer: tested and approved in MySQL -----

SELECT COALESCE(t_meubles.client_id,t_deco.client_id) AS client_id
, IFNULL(t_meubles.ventes_meubles, 0) AS ventes_meubles
, IFNULL(t_deco.ventes_deco, 0) AS ventes_deco

FROM (SELECT tp.client_id, SUM(tp.prod_price * tp.prod_qty) AS ventes_meubles
  FROM (
  	SELECT * from transactions t JOIN PRODUCT_NOMENCLATURE p ON t.prod_id=p.product_id
  	WHERE product_type like 'MEUBLE' AND t.date BETWEEN '2019-01-01' and '2019-12-31'
	    ) tp
	GROUP BY client_id
  	) t_meubles
LEFT JOIN (SELECT tp.client_id, SUM(tp.prod_price * tp.prod_qty) AS ventes_deco FROM
	(
  	select * from transactions t JOIN PRODUCT_NOMENCLATURE p ON t.prod_id=p.product_id
  	WHERE product_type like 'DECO' AND t.date BETWEEN '2019-01-01' and '2019-12-31'
	) tp
	GROUP BY client_id
  	) t_deco
ON t_meubles.client_id = t_deco.client_id

UNION ALL

SELECT COALESCE(t_meubles.client_id,t_deco.client_id) AS client_id, IFNULL(t_meubles.ventes_meubles, 0) AS ventes_meubles, IFNULL(t_deco.ventes_deco, 0) AS ventes_deco
FROM (SELECT tp.client_id, SUM(tp.prod_price * tp.prod_qty) AS ventes_deco
  FROM (
  	SELECT * from transactions t JOIN PRODUCT_NOMENCLATURE p ON t.prod_id=p.product_id
  	WHERE product_type like 'DECO' AND t.date BETWEEN '2019-01-01' and '2019-12-31'
	    ) tp
	GROUP BY client_id
  	) t_deco
LEFT JOIN (SELECT tp.client_id, SUM(tp.prod_price * tp.prod_qty) AS ventes_meubles FROM
	(
  	select * from transactions t JOIN PRODUCT_NOMENCLATURE p ON t.prod_id=p.product_id
  	WHERE product_type like 'MEUBLE' AND t.date BETWEEN '2019-01-01' and '2019-12-31'
	) tp
	GROUP BY client_id
  	) t_meubles
ON t_deco.client_id = t_meubles.client_id
WHERE t_meubles.client_id IS NULL OR t_deco.client_id IS NULL;

