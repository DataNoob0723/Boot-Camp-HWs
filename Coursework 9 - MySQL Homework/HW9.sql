USE sakila;

-- 1a. Display the first and last names of all actors from the table actor.
SELECT first_name, last_name FROM actor;

-- 1b. Display the first and last name of each actor in a single column in upper case letters. Name the column Actor Name.
SELECT UPPER(CONCAT(first_name, " ", last_name)) AS actor_name FROM actor;

-- 2a. You need to find the ID number, first name, and last name of an actor, of whom you know only the first name, "Joe." 
-- What is one query would you use to obtain this information?
SELECT actor_id, first_name, last_name FROM actor
WHERE first_name = "Joe";

-- 2b. Find all actors whose last name contain the letters GEN:
SELECT actor_id, first_name, last_name FROM actor
WHERE last_name LIKE "%GEN%";

-- 2c. Find all actors whose last names contain the letters LI. This time, order the rows by last name and first name, in that order:
SELECT actor_id, first_name, last_name FROM actor
WHERE last_name LIKE "%LI%"
ORDER BY last_name, first_name;

-- 2d. Using IN, display the country_id and country columns of the following countries: Afghanistan, Bangladesh, and China:
SELECT country_id, country FROM country
WHERE country IN ("Afghanistan", "Bangladesh", "China");

-- 3a. You want to keep a description of each actor. 
-- You don't think you will be performing queries on a description, so create a column in the table actor named description and use the data type BLOB (Make sure to research the type BLOB, as the difference between it and VARCHAR are significant).
ALTER TABLE actor ADD COLUMN description BLOB;

-- 3b. Very quickly you realize that entering descriptions for each actor is too much effort. Delete the description column.
ALTER TABLE actor
DROP COLUMN description;

-- 4a. List the last names of actors, as well as how many actors have that last name.
SELECT last_name, COUNT(last_name) FROM actor
GROUP BY last_name;

-- 4b. List last names of actors and the number of actors who have that last name, but only for names that are shared by at least two actors.
SELECT last_name, COUNT(last_name) FROM actor
GROUP BY last_name
HAVING COUNT(last_name) >= 2;

-- 4c. The actor HARPO WILLIAMS was accidentally entered in the actor table as GROUCHO WILLIAMS. Write a query to fix the record.
UPDATE actor SET first_name = "HARPO"
WHERE last_name = "WILLIAMS" AND first_name = "GROUCHO";

-- 4d. Perhaps we were too hasty in changing GROUCHO to HARPO. 
-- It turns out that GROUCHO was the correct name after all! In a single query, if the first name of the actor is currently HARPO, change it to GROUCHO.
UPDATE actor SET first_name = "GROUCHO"
WHERE first_name = "HARPO";

-- 5a. You cannot locate the schema of the address table. Which query would you use to re-create it?
SHOW CREATE TABLE address;

-- 6a. Use JOIN to display the first and last names, as well as the address, of each staff member. Use the tables staff and address:
SELECT * FROM staff;
SELECT * FROM address;

SELECT s.first_name, s.last_name, a.address, a.district, a.city_id, a.postal_code
FROM staff AS s
INNER JOIN address AS a
ON s.address_id = a.address_id;

-- 6b. Use JOIN to display the total amount rung up by each staff member in August of 2005. Use tables staff and payment.
SELECT * FROM staff;
SELECT * FROM payment;

SELECT s.staff_id, s.first_name, s.last_name, SUM(p.amount) AS rung_up
FROM payment AS p
JOIN staff AS s ON p.staff_id = s.staff_id
WHERE MONTH(p.payment_date) = 8
GROUP BY s.staff_id;

-- 6c. List each film and the number of actors who are listed for that film. Use tables film_actor and film. Use inner join.
SELECT * FROM film_actor;
SELECT * FROM film;

SELECT f.film_id, f.title, COUNT(fa.actor_id) AS num_of_actors
FROM film AS f
INNER JOIN film_actor AS fa ON f.film_id = fa.film_id
GROUP BY f.film_id;

-- 6d. How many copies of the film Hunchback Impossible exist in the inventory system?
SELECT * FROM inventory;
SELECT * FROM film;

SELECT COUNT(i.inventory_id) AS num_of_copies
FROM inventory AS i
INNER JOIN film AS f ON i.film_id = f.film_id
WHERE f.title = "Hunchback Impossible";

-- 6e. Using the tables payment and customer and the JOIN command, list the total paid by each customer. 
-- List the customers alphabetically by last name:
SELECT * FROM payment;
SELECT * FROM customer;

SELECT p.customer_id, c.first_name, c.last_name, SUM(p.amount) AS total_payment
FROM payment AS p
JOIN customer AS c ON p.customer_id = c.customer_id
GROUP BY p.customer_id
ORDER BY last_name, first_name;

-- 7a. The music of Queen and Kris Kristofferson have seen an unlikely resurgence. 
-- As an unintended consequence, films starting with the letters K and Q have also soared in popularity. 
-- Use subqueries to display the titles of movies starting with the letters K and Q whose language is English.
SELECT * FROM film;
SELECT * FROM language; 

SELECT title
FROM film
WHERE language_id IN
(
	SELECT language_id
    FROM language
    WHERE name = "English"
)
AND (title LIKE "K%" OR title LIKE "Q%");

-- 7b. Use subqueries to display all actors who appear in the film Alone Trip.
SELECT * FROM actor;
SELECT * FROM film;
SELECT * FROM film_actor;

SELECT actor_name FROM actor
WHERE actor_id IN
(
	SELECT actor_id FROM film_actor
    WHERE film_id IN
    (
		SELECT film_id FROM film
        WHERE title = "Alone Trip"
    )
);

-- 7c. You want to run an email marketing campaign in Canada, for which you will need the names and email addresses of all Canadian customers. 
-- Use joins to retrieve this information.
SELECT * FROM customer;
SELECT * FROM address;
SELECT * FROM city;
SELECT * FROM country;

SELECT first_name, last_name, email
FROM customer
WHERE address_id IN
(
	SELECT address_id
    FROM address
    WHERE city_id IN
    (
		SELECT city_id
        FROM city
        WHERE country_id IN
        (
			SELECT country_id
            FROM country
            WHERE country = "Canada"
        )
    )
);

-- 7d. Sales have been lagging among young families, and you wish to target all family movies for a promotion. 
-- Identify all movies categorized as family films.
SELECT * FROM film;
SELECT * FROM film_category;
SELECT * FROM category;

SELECT * 
FROM film
WHERE film_id IN
(
	SELECT film_id
    FROM film_category
    WHERE category_id IN
    (
		SELECT category_id
        FROM category
        WHERE name = "Family"
    )
);

-- 7e. Display the most frequently rented movies in descending order.
SELECT * FROM rental;
SELECT * FROM inventory;
SELECT * FROM film;

SELECT f.film_id, f.title, COUNT(f.film_id) AS num_of_rented
FROM rental AS r
LEFT JOIN inventory AS i ON r.inventory_id = i.inventory_id
LEFT JOIN film AS f ON i.film_id = f.film_id
GROUP BY f.film_id
ORDER BY COUNT(f.film_id) DESC, f.film_id;

-- 7f. Write a query to display how much business, in dollars, each store brought in.
SELECT * FROM store;
SELECT * FROM payment;
SELECT * FROM staff;
SELECT * FROM customer;

-- If using staff to calculate:
SELECT s.store_id, SUM(p.amount) AS total
FROM payment AS p
LEFT JOIN staff AS s
ON p.staff_id = s.staff_id
GROUP BY s.store_id;

-- If using customer to calculate:
SELECT c.store_id, SUM(p.amount) AS total
FROM payment AS p
LEFT JOIN customer AS c
ON p.customer_id = c.customer_id
GROUP BY c.store_id;

-- The results are a little different. I am not sure why.

-- 7g. Write a query to display for each store its store ID, city, and country.
SELECT * FROM store;
SELECT * FROM address;
SELECT * FROM city;
SELECT * FROM country;

SELECT s.store_id, c.city, ct.country
FROM store AS s
LEFT JOIN address AS a ON s.address_id = a.address_id
LEFT JOIN city AS c ON a.city_id = c.city_id
LEFT JOIN country AS ct ON c.country_id = ct.country_id;

-- 7h. List the top five genres in gross revenue in descending order. 
-- (Hint: you may need to use the following tables: category, film_category, inventory, payment, and rental.)
SELECT * FROM category;
SELECT * FROM film_category;
SELECT * FROM inventory;
SELECT * FROM payment;
SELECT * FROM rental;

SELECT c.category_id, c.name, SUM(p.amount) AS gross_revenue
FROM payment AS p
LEFT JOIN rental AS r ON p.rental_id = r.rental_id
LEFT JOIN inventory AS i ON r.inventory_id = i.inventory_id
LEFT JOIN film_category AS f ON i.film_id = f.film_id
LEFT JOIN category AS c ON f.category_id = c.category_id
GROUP BY c.category_id
ORDER BY SUM(p.amount) DESC
LIMIT 5;

-- 8a. In your new role as an executive, you would like to have an easy way of viewing the Top five genres by gross revenue. 
-- Use the solution from the problem above to create a view. If you haven't solved 7h, you can substitute another query to create a view.
CREATE VIEW top_five_genres AS
(
	SELECT c.category_id, c.name, SUM(p.amount) AS gross_revenue
	FROM payment AS p
	LEFT JOIN rental AS r ON p.rental_id = r.rental_id
	LEFT JOIN inventory AS i ON r.inventory_id = i.inventory_id
	LEFT JOIN film_category AS f ON i.film_id = f.film_id
	LEFT JOIN category AS c ON f.category_id = c.category_id
	GROUP BY c.category_id
	ORDER BY SUM(p.amount) DESC
	LIMIT 5
);

-- 8b. How would you display the view that you created in 8a?
SELECT * FROM top_five_genres;

-- 8c. You find that you no longer need the view top_five_genres. Write a query to delete it.
DROP VIEW IF EXISTS top_five_genres;
