-- count the frequency of a record
SELECT score, COUNT(score) number FROM second_table GROUP BY score ORDER BY 2 DESC;
