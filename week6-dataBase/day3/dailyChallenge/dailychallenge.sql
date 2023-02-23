-- 1
-- CREATE TABLE Customer(
-- 	id serial primary key,
-- 	first_name varchar (80),
-- 	last_name varchar(80) not null
-- );
-- CREATE TABLE Customer_Profile(
-- 	id serial primary key,
-- 	isLoggedIn boolean default false,
-- 	customer_id integer,
-- 	FOREIGN kEY (customer_id) REFERENCES Customer(id)
-- );

-- 2
-- select * from customer
-- select table_name,column_name,data_type from information_schema.columns where table_name='customer_profile'
-- insert into Customer(first_name,last_name) values ('Jhon','Doe'),('Jerome','Lalu'),('lea','Rive');

-- 3
-- INSERT INTO Customer_Profile (isLoggedIn, customer_id) 
-- SELECT true, id 
-- FROM Customer 
-- WHERE first_name='John' AND last_name='Doe';
-- INSERT INTO Customer_Profile (isLoggedIn, customer_id) 
-- SELECT false, id 
-- FROM Customer  
-- WHERE first_name IN ('Jerome', 'Lea');

-- 4
-- The first_name of the LoggedIn customers
-- SELECT customer.first_name
-- FROM customer
-- inner JOIn Customer_Profile
-- ON customer.id = Customer_Profile.Customer_id
-- WHERE customer_Profile.isLoggedIn = true;

-- All the customers first_name and isLoggedIn columns - even the customers those who don’t have a profile.
-- SELECT customer.first_name, customer_Profile.isLoggedIn
-- FROM customer 
-- LEFT JOIN Customer_Profile  
-- ON Customer.id = Customer_Profile.customer_id;

-- The number of customers that are not LoggedIn
-- SELECT COUNT (*) FROM Customer 
-- LEFT OUTER JOIN Customer_Profile 
-- On customer.id = Customer_Profile.customer_id 
-- WHERE customer_profile.isLoggedIn = false;

-- part 2
-- 1
-- CREATE TABLE Book(
-- 	book_id serial primary key,
-- 	title varchar(80) NOT NULL,
-- 	author varchar(80) NOT NULL
-- )
-- 2
-- insert into Book (title,author) Values ('Alice in WonderLand','Lewis Carrol')
-- ,('Harry Potter', 'J.K Rowling'),
-- ('to kill a mockingbird','Harper lee');

-- 3
-- CREATE TABLE Student(
-- 	student_id serial primary key,
-- 	name varchar(80) NOT NULL UNIQUE,
-- 	age int CHECK (age <=15)
-- )
-- 4
-- insert into Student (name,age) Values ('John','12')
-- ,('Lera', '10'),
-- ('Bob','14');

-- 5
-- CREATE TABLE Library(
-- 	book_fk_id INTEGER REFERENCES Book(Book_id)ON DELETE CASCADE ON UPDATE CASCADE,
-- 	student_id INTEGER REFERENCES Student(student_id) ON DELETE CASCADE ON UPDATE CASCADE,
-- 	borrowed_date DATE,
-- 	PRIMARY KEY (book_fk_id,student_id)
-- );
-- 6
INSERT INTO 
Library(book_fk_id,student_id,borrowed_date)
VALUES
((SELECT book_id FROM Book WHERE 'book.titile' = 'Alice in wonderland'),
(SELECT student_id FROM Student WHERE name='John'),'15/02/2022'),
((SELECT book_id FROM Book WHERE 'book.titile'  = 'To Kill A Mockingbird'),
 (SElECT Student_id FROM Student WHERE name='Bod'),'03/03/2021'),
 

((SELECT book_id FROM Book WHERE 'book.titile'  = 'Alice In Wonderland'),
(SELECT student_id FROM Student WHERE name = 'Lera'),
'23/05/2021'),
((SELECT book_id FROM Book WHERE 'book.titile'  = 'Harry Potter'),
(SELECT student_id FROM Student WHERE name = 'Bob'),
'12/08/2021');



