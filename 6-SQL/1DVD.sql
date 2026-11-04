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

SELECT *

SELECT MIN(replacement_cost) FROM film;
SELECT Max(replacement_cost) FROM film;
SELECT Max(replacement_cost),MIN(replacement_cost)
FROM film;


SELECT * FROM payment

SELECT customer_id,staff_id,SUM(amount) FROM payment
GROUP BY staff_id,customer_id


SELECT staff_id,customer_id,SUM(amount) FROM payment
GROUP BY staff_id,customer_id 
ORDER BY staff_id



SELECT staff_id,customer_id,SUM(amount) FROM payment
GROUP BY staff_id,customer_id 
ORDER BY staff_id,customer_id


SELECT staff_id,customer_id,SUM(amount) FROM payment
GROUP BY staff_id,customer_id 
ORDER BY SUM(amount)


SELECT * FROM payment


SELECT DATE(payment_date) FROM payment

SELECT DATE(payment_date),SUM(amount) FROM payment
GROUP BY DATE(payment_date)

SELECT DATE(payment_date),SUM(amount) FROM payment
GROUP BY DATE(payment_date)
ORDER BY SUM(amount)

SELECT DATE(payment_date),SUM(amount) FROM payment
GROUP BY DATE(payment_date)
ORDER BY SUM(amount) DESC


SELECT staff_id,COUNT(amount)
FROM payment
GROUP BY staff_id


SELECT rating, AVG(replacement_cost)
FROM film
GROUP BY rating


SELECT rating,
ROUND(AVG(replacement_cost),2)
FROM film
GROUP BY rating


SELECT customer_id, SUM(amount)
FROM payment
GROUP BY customer_id
ORDER BY SUM(amount) DESC
LIMIT 5























