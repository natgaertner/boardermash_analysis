\copy (select count(uuid), date_trunc('hour',timestamp) from mashes group by date_trunc('hour',timestamp)) to 'mash_count_by_hour.csv' with CSV HEADER;
