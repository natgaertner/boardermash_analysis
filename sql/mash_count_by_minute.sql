\copy (select count(uuid), date_trunc('minute',timestamp) from mashes group by date_trunc('minute',timestamp)) to 'mash_count_by_minute.csv' with CSV HEADER;
