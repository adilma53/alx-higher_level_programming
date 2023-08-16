-- order states by names with each state max temperature --
SELECT state, MAX(temp) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state;