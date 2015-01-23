#!/bin/bash
source "/home/local/ANT/gaertnen/code/mash_analysis/bin/activate"
for i in `seq 1 4` ; do
    (python "/home/local/ANT/gaertnen/code/mash_analysis/compute_user_excluding_mashes.py" "ip_counts$i.csv" &)
done
