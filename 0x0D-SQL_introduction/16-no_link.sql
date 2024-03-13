-- script that lists all records but not rows without a name value
SELECT score, name FROM second_table WHERE name!="" OR name IS NOT NULL ORDER BY score DESC;
