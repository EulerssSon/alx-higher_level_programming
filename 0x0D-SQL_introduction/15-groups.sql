-- script script is to delete all records from the table where scr is <= 5
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
