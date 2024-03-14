-- this script is to display the avg temperature of each city in the world desc
SELECT `state`, MAX(`value`) AS `avg_temp`
FROM `temperatures`
GROUP BY `state`
ORDER BY `state`;
