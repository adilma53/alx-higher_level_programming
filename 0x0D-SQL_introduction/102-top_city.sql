
-- list top cities by temperature in July and August --
SELECT city, AVG(temp) AS avg_temp
FROM temperatures
WHERE MONTH(date) BETWEEN 7 AND 8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
