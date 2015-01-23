\copy (select name, score, row_number() over (order by score desc) from players) to 'rank.csv' with CSV HEADER;
