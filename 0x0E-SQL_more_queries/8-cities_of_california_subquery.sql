-- script that lists all the cities of California that can be found in the database
SELECT cities.name AS city_name
FROM cities
JOIN states ON cities.state_id = states.id
WHERE states.name = 'California';