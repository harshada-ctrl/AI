SELECT * FROM film;
select * from actor
select * from city
select count(category_id) from film_category
select max(amount) from payment
select * from payment;
select count(*) 
--21 august 2026 friday
SELECT * FROM customer
WHERE first_name = 'Jared';

SELECT * FROM film
Where rental_rate > 4 AND replacement_cost >= 19.99
AND rating='R';






SELECT count(title) FROM film
Where rental_rate > 4 AND replacement_cost >= 19.99
AND rating='R';


SELECT count(*) FROM film
Where rental_rate > 4 AND replacement_cost >= 19.99
AND rating='R';


SELECT count(*) FROM film
Where rating = 'R' OR rating = 'PG-13';


SELECT * FROM film
where rating != 'R'



