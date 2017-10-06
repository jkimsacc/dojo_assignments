-- 1. display countries that speakes slovene and percentage of the poplulation
-- 
-- SELECT name, language, percentage
-- FROM countries
-- LEFT JOIN languages
-- ON  countries.id = country_id
-- WHERE language = 'Slovene';

-- 2. display total number of cities in each coutry

-- SELECT countries.name, COUNT(cities.name)
-- FROM countries
-- LEFT JOIN cities
-- ON countries.id = country_id
-- GROUP BY countries.name
-- ORDER BY COUNT(cities.name) DESC;

-- 3. get all the cities in Mexico with poplulation greater than 500,000? in DESC order
-- SELECT cities.name, cities.population
-- FROM cities
-- LEFT JOIN countries
-- ON country_id = countries.id
-- WHERE countries.name = 'Mexico' AND cities.population > 500000;

-- 4. get all languages where percentage > 89, DESC order
-- SELECT countries.name, languages.language, languages.percentage
-- FROM countries
-- LEFT JOIN languages
-- ON countries.id = country_id
-- WHERE languages.percentage > 89
-- ORDER BY languages.percentage DESC;

-- 5. all countries where area < 501 and popluation >100000
-- SELECT name, surface_area, population
-- FROM countries
-- WHERE surface_area < 501 and population > 100000;

-- 6. Constitutional Monarchy && capital > 200 && life expectancy > 75
-- SELECT name
-- FROM countries
-- WHERE government_form = 'Constitutional Monarchy' and capital > 200 and life_expectancy > 75;

-- 7. all Cities in Argentina inside Buenos Aires district & poplulation > 500000
-- SELECT countries.name, cities.name, cities.district, cities.population
-- FROM cities
-- LEFT JOIN countries
-- ON country_id = countries.id
-- WHERE countries.name = 'Argentina' and cities.district = 'Buenos Aires' and cities.population > 500000;

-- 8. number of countries in each region display name of region, # of countries, desc
-- SELECT region, COUNT(name)
-- FROM countries
-- GROUP BY region
-- ORDER BY COUNT(name) DESC;

