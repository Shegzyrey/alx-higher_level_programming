-- filer names without value
SELECT score, name FROM second_table WHERE name <> '' ORDER BY score DESC, name DESC;
