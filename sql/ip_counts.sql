\copy (select ip_id,count(uuid) from mashes_obscured group by ip_id order by count(uuid) desc) to 'ip_counts.csv' with CSV HEADER;

