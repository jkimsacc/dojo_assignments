-- 1. city_id 312 

-- SELECT customer.first_name, customer.last_name, customer.email, address.address, address.address2
-- FROM customer
-- LEFT JOIN address
-- ON customer.address_id = address.address_id
-- WHERE city_id = 312;

-- 2. get all comedy films, display film title, description, release year, rating, special feature, and category

-- SELECT film.title, film.description, film.release_year,  film.rating, film.special_features
-- FROM film
-- LEFT JOIN film_category
-- ON film.film_id = film_category.film_id
-- LEFT JOIN category
-- ON category.category_id = film_category.category_id
-- WHERE category.name = 'Comedy'

-- 3. get all film by actor_id=5, select id, name, title, description, release year
-- 
-- SELECT film.title, actor.first_name, actor.last_name, film.description, film.release_year
-- FROM actor
-- LEFT JOIN film_actor
-- ON actor.actor_id = film_actor.actor_id
-- LEFT JOIN film
-- ON film.film_id = film_actor.film_id
-- WHERE actor.actor_id = 5;

-- 4. get all customers in store_id = 1 in cities 1, 42, 312, 459, return first name, last name, email, address

-- SELECT customer.first_name, customer.last_name, customer.email, address.address, customer.store_id, address.city_id
-- FROM customer
-- LEFT JOIN address
-- ON customer.address_id = address.address_id
-- LEFT JOIN city
-- ON city.city_id = address.city_id
-- WHERE customer.store_id = 1 and (address.city_id = 1 OR address.city_id = 42 OR address.city_id = 312 OR address.city_id = 459)

-- 5. all films rating G, special feature = behind the scenes, actor id 15
-- SELECT film.title, film.description, film.release_year, film.rating, film.special_features
-- FROM film
-- LEFT JOIN film_actor
-- ON film.film_id = film_actor.film_id
-- WHERE film.rating = "G" AND film.special_features = "Behind the Scenes" AND film_actor.actor_id = 15;

-- 6. jointed in film_id=369
-- SELECT film.film_id, film.title, film_actor.actor_id, actor.first_name, actor.last_name
-- FROM film
-- LEFT JOIN film_actor
-- ON film.film_id = film_actor.film_id
-- LEFT JOIN actor
-- ON actor.actor_id = film_actor.actor_id
-- WHERE film.film_id = 369;

-- 7. drama films, rental_rate of 2.99
-- SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name AS genre
-- FROM film
-- LEFT JOIN film_category
-- ON film.film_id = film_category.film_id
-- LEFT JOIN category
-- ON category.category_id = film_category.category_id
-- WHERE film.rental_rate = 2.99 AND category.name = 'Drama';

-- 8. 
SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name AS genre, actor.first_name, actor.last_name
FROM film
LEFT JOIN film_category
ON film.film_id = film_category.film_id
LEFT JOIN category
ON category.category_id = film_category.category_id
LEFT JOIN film_actor
ON film.film_id = film_actor.film_id
LEFT JOIN actor
ON actor.actor_id = film_actor.actor_id
WHERE actor.first_name = 'SANDRA' AND actor.last_name = 'KILMER';