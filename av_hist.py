import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import csv

av_scores = [float(row.strip()) for row in open('scores/av_scores.csv')]
av_std = np.std(av_scores)
av_mean = np.mean(av_scores)
no_av_scores = [float(row.strip()) for row in open('scores/no_av_scores.csv')]
no_av_std = np.std(no_av_scores)
no_av_mean = np.mean(no_av_scores)

n, bins, patches = plt.hist(av_scores,50,normed=1,facecolor='green',alpha=0.5)
y = mlab.normpdf(bins,av_mean,av_std)
plt.plot(bins,y,'g--')
n, bins, patches = plt.hist(no_av_scores,25,normed=1,facecolor='blue',alpha=0.5)
y = mlab.normpdf(bins,no_av_mean,no_av_std)
plt.plot(bins,y,'b--')
plt.xlabel('score')
plt.title(r'green: has av $\mu={av_mean:.2f}$, $\sigma={av_std:.2f}$, blue: no av $\mu={no_av_mean:.2f}$, $\sigma={no_av_std:.2f}$'.format(av_mean=av_mean,av_std=av_std,no_av_mean=no_av_mean,no_av_std=no_av_std))
plt.savefig('av_hist.png')

