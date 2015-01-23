\copy (select * from mashes_obscured where ip_id in (258,294,368,579,409,582,520,231,569,273)) to 'top_10_mashes.csv' with CSV HEADER;
