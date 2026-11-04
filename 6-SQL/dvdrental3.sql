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

SELECT payment_id,payment.customer_id,first_name
FROM payment
INNER JOIN customer
ON payment.customer_id = customer.customer_id


SELECT * FROM customer
FULL OUTER JOIN payment
ON customer.customer_id = payment.customer_id