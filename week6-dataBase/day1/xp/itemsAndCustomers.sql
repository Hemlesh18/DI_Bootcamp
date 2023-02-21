-- CREATE TABLE items(
-- 	id serial Primary Key,
-- 	item varchar(50) NOT Null,
-- 	item_Price integer NOT null
-- )
-- CREATE TABLE customers(
-- 	id serial Primary Key,
-- 	First_name varchar(50),
-- 	Last_name varchar(50) 
-- )
-- insert into items(item, item_price) values('small Desk',100),('large Desk',300),('fan',80)
-- insert into customers(first_name, last_name) values('Greg','Jones'),('Sandra','Jones'),('scott','scott'),('Trevor','Green'),('Melanie','Johnson');
-- SELECT *FROM item
-- SELECT *FROM items where item_Price>80
-- SELECT * FROM items where item_Price<=300
-- SELECT * FROM customers where last_name like '%Smith'
-- SELECT * FROM customers where last_name like 'Jones'
SELECT * FROM customers where last_name not like 'Jones'


