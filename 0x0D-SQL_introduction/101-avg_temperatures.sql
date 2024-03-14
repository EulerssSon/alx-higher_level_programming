-- this script is to display the avg temperature of each city in the world desc
SELECT `city`, AVG(`value`) AS `avf_temperature`
FROM `temperature`
GROUP BY `city`
ORDER BY `avg_temperature` DESC;
