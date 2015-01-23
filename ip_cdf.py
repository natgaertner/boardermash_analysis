import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import csv

counts = [int(row['count']) for row in csv.DictReader(open('data/ip_counts.csv'))]
total_mashes = sum(counts)
sums = [sum(counts[:i+1])/float(total_mashes) for i in range(len(counts))]
first_quartile = .25
half = .5
third_quartile = .75
ninety = .9
for i,s in enumerate(sums):
    if s < first_quartile:
        first_quartile_count = i
    if s < half:
        half_count = i
    if s < third_quartile:
        third_quartile_count = i
    if s < ninety:
        ninety_count = i
fig,ax = plt.subplots()

ax.plot(range(len(sums)),sums,'b-')
ax.plot(range(len(sums)),[first_quartile for _ in range(len(sums))],'k--')
ax.plot(range(len(sums)),[half for _ in range(len(sums))],'k--')
ax.plot(range(len(sums)),[third_quartile for _ in range(len(sums))],'k--')
ax.plot(range(len(sums)),[ninety for _ in range(len(sums))],'k--')
ax.axvline(first_quartile_count,color='k',linestyle='--')
ax.axvline(half_count,color='k',linestyle='--')
ax.axvline(third_quartile_count,color='k',linestyle='--')
ax.axvline(ninety_count,color='k',linestyle='--')
ax.set_yticks([0.0,0.25,0.5,0.75,1.0])
ax.set_xticks(range(0,801,50))
plt.title('cumulative mashes by ip')
plt.savefig('images/ip_cdf.png')
