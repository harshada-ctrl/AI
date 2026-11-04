--
SELECT * FROM actor
select first_name FROM actor;
select first_name, last_name FROM actor;
select  last_name, first_name FROM actor;
select first_name, last_name, email FROM customer;

SELECT customer_id,SUM(amount) FROM payment
GROUP BY customer_id


SELECT customer_id,SUM(amount) FROM payment
WHERE customer_id NOT IN(184,87,477)
GROUP BY customer_id


SELECT customer_id,SUM(amount) FROM payment
GROUP BY customer_id
HAVING SUM(amount) > 100   

SELECT store_id,COUNT(customer_id) FROM customer
GROUP BY store_id

SELECT store_id,COUNT(*) FROM customer
GROUP BY store_id


SELECT store_id,COUNT(*) FROM customer
GROUP BY store_id
HAVING COUNT(*) > 300

SELECT store_id,COUNT(customer_id) FROM customer
GROUP BY store_id
HAVING COUNT(customer_id) > 300

SELECT customer_id,COUNT(*) FROM payment
GROUP BY customer_id
HAVING COUNT(*) >= 40;


SELECT customer_id,SUM(amount) FROM payment
WHERE staff_id = 2
GROUP BY customer_id
HAVING SUM(amount) > 100

SELECT SUM(column) AS new_name
FROM table --error

SELECT COUNT(amount) AS num_transactions
FROM payment

SELECT customer_id,SUM(amount) 
FROM payment
GROUP BY customer_id

SELECT customer_id,SUM(amount) AS total_spent 
FROM payment
GROUP BY customer_id


SELECT customer_id,SUM(amount) 
FROM payment
GROUP BY customer_id
HAVING SUM(amount) > 100


SELECT customer_id,SUM(amount) AS total_spent 
FROM payment
GROUP BY customer_id
HAVING SUM(amount) > 100

SELECT customer_id,SUM(amount) AS total_spent 
FROM payment
GROUP BY customer_id
HAVING total_spent > 100   -- it get error

SELECT customer_id,amount
FROM payment
WHERE amount > 2

SELECT customer_id,amount AS new_name
FROM payment
WHERE new_name > 2 --error

SELECT * FROM payment

SELECT * FROM customer

SELECT payment_id,payment.custome

SELECT * FROM film

SELECT * FROM inventory

SELECT film.film_id,title,inventory_id,store_id
FROM film
LEFT JOIN inventory ON
inventory.film_id = film.film_id
WHERE inventory.film_id IS null


SELECT * FROM customer

SELECT * FROM address
INNER JOIN customer
ON address.address_id = customer.address_id
WHERE district = 'California'


SELECT district,email FROM address
INNER JOIN customer
ON address.address_id = customer.address_id
WHERE district = 'California'

SELECT * FROM film
SELECT * FROM actor
SELECT * FROM film_actor

SELECT * FROM actor
INNER JOIN film_actor
ON actor.actor_id = film_actor.actor_id
INNER JOIN film
ON film_actor.film_id = film.film_id


SELECT title,first_name,last_name FROM actor
INNER JOIN film_actor
ON actor.actor_id = film_actor.actor_id
INNER JOIN film
ON film_actor.film_id = film.film_id
WHERE first_name = 'Nick' AND
last_name = 'Wahlberg'


