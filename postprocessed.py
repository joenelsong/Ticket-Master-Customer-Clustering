import numpy as np
import pandas

data = pandas.read_csv('preprocessed_cluster_data.csv', engine='python', encoding='latin-1')



data['avg_totals_hits']=data.totals_hits/data.totals_visits
data['avg_timeonsite']=data.totals_timeonsite/data.totals_visits

reduced = data.drop(['Unnamed: 0','fullvisitorid','geonetwork_region', 'totals_pageviews', 'totals_timeonsite', 'totals_hits'], axis=1)
# Remove outliers



## Scitkit
from sklearn.cluster import KMeans
X = reduced.values
means = [ np.mean(X[:,0]), np.mean(X[:,1]), np.mean(X[:,2]) ]
stdevs = [ np.std(X[:,0]), np.std(X[:,1]), np.std(X[:,2]) ]

# remove outliers
out_thresh = 3
data_outs_removed = reduced[ reduced.totals_visits <= means[0]+out_thresh*stdevs[0] ]
data_outs_removed = data_outs_removed[ reduced.totals_visits <= means[1]+out_thresh*stdevs[1] ]
X_no_outs = data_outs_removed[ reduced.totals_visits <= means[2]+out_thresh*stdevs[2] ]

# Run algorithms, and capture classifications
kmm = KMeans(n_clusters=3, random_state=1).fit(X_no_outs)
y = kmm.labels_

# Classification Counts
out = kmm.labels_
counts=3*[0]
for i in out:
    if i == 0:
        counts[0]+=1
    elif i == 1:
        counts[1]+=1
    elif i == 2:
        counts[2]+=1
        
        
'''        
# 50 rows by 4 columns
new_data = [[0]*4 for i in range(50)] 


states = ['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY']
states_count = 50*[0]

for i in range( len(X) ):
    s = data.geonetwork_region[i]
    stats_count[states.index(s)]+=1
    
'''

## PLOT

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


fig = plt.figure(1, figsize=(4, 3))
plt.clf()
ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134)

plt.cla()
#KMeans(n_clusters=3, random_state=1).fit(X)

XX = X_no_outs.values[0:10000]
y = kmm.labels_[0:10000]
ax.scatter(XX[:,0], XX[:,1], XX[:,2],s=15, c=y.astype(np.float))

ax.w_xaxis.set_ticklabels([])
ax.w_yaxis.set_ticklabels([])
ax.w_zaxis.set_ticklabels([])
ax.set_xlabel(reduced.columns[0])
ax.set_ylabel(reduced.columns[1])
ax.set_zlabel(reduced.columns[2])

#ax.set_xlim([min(XX), max(XX)])
#ax.set_ylim


plt.show()


#KMeans(n_clusters=3, random_state=1).fit(newd4.values)