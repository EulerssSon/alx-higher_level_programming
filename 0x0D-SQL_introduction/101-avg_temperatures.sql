-- this script is to display the avg temperature of each city in the world desc
SELECT `city`, AVG(`value`) AS `avg_temperature`
FROM `temperatures`
GROUP BY `city`
ORDER BY `avg_temperature` DESC;
