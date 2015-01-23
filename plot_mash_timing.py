import matplotlib.pyplot as plt
from numpy import arange
import numpy as np
from matplotlib.dates import HourLocator, DateFormatter
from matplotlib import dates

counts,hours = np.loadtxt('data/mash_count_by_hour.csv',unpack=True, converters={1:dates.strpdate2num('%Y-%m-%d %H:%M:%S')}, skiprows=1,delimiter=',')
fig, ax = plt.subplots()
ax.plot_date(hours, counts,fmt="r-")
ax.xaxis.set_major_locator(HourLocator(arange(0,25,4)))
ax.xaxis.set_major_formatter( DateFormatter('%m-%d %H:%M'))

ax.fmt_xdata = DateFormatter('%m-%d %H:%M')
fig.autofmt_xdate()

plt.savefig('mash_counts_by_hour.png')
