-- create table product_orders(
-- 	order_id serial primary key,
-- 	order_name varchar(250) not null
-- );

-- create table items (
-- item_id int primary key,
-- item_name varchar(50),
-- item_quantity int,
-- item_price int,
-- order_id int,
-- foreign key (order_id) references product_orders (order_id)
-- );

insert into product_orders (order_id, order_name)
values
(1,'Hem'),
(2,'Nid');


insert into items
values
(1, 'shirt', 2, 800, 1),
(2, 'Shoe', 1, 1800, 3),
(3, 'Trouser', 6, 2000, 2);

create or replace function total_price(id int)
returns int as $calculation$
begin
return (select sum(item_price * item_quantity) from items where order_id = id);
end;
$calculation$ language plpgsql;
select * from total_price (1)