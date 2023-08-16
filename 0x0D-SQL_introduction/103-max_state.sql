-- order states by names with each state max temperature
SELECT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state