-- filer names without value
SELECT * FROM second_table WHERE name <> '' GROUP BY score DESC, name DESC;
