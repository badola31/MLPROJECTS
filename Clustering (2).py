# -*- coding: utf-8 -*-
"""B20MT012_Task1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BFYUi5AmMBG_jxaw1SVqQpQwGV2qOvrF
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""i. Download the dataset from the given link.
ii. Perform K Means clustering using the scikit learn library, try at least three different values of n_clusters, and use random_state = 2021.
iii. Print the cluster_centers_ obtained.
iv. Plot a scatter plot after performing the K means clustering between any two attributes/features of the dataset.

"""

file=pd.read_csv("milk.csv")
file=file.drop('Unnamed: 0',axis=1)

from sklearn.cluster import KMeans

kmodel = KMeans(n_clusters=2, init='random',n_init=10, max_iter=300, random_state=2021)
y_label = kmodel.fit_predict(file)
kmodel2 = KMeans(n_clusters=3, init='random',n_init=10, max_iter=300, random_state=2021)
y2_label = kmodel2.fit_predict(file[['water','protein','fat','lactose','ash']])
kmodel3 = KMeans(n_clusters=4, init='random',n_init=10, max_iter=300, random_state=2021)
y3_label = kmodel3.fit_predict(file[['water','protein','fat','lactose','ash']])

file['predicted']=y_label
file['predicted2']=y2_label
file['predicted3']=y3_label

print(kmodel.cluster_centers_)

print(kmodel2.cluster_centers_)

print(kmodel3.cluster_centers_)

file

plt.scatter(kmodel.cluster_centers_[:, 0], kmodel.cluster_centers_[:, 1],
    s=100, marker='o',
    c='red',
    label='centroids'
)
plt.legend(scatterpoints=1)
plt.grid()
plt.show()

plt.scatter(kmodel2.cluster_centers_[:, 0], kmodel2.cluster_centers_[:, 1],
    s=100, marker='o',
    c='blue',
    label='centroids'
)
plt.legend(scatterpoints=1)
plt.grid()
plt.show()

plt.scatter(kmodel3.cluster_centers_[:, 0], kmodel3.cluster_centers_[:, 1],
    s=100, marker='o',
    c='green',
    label='centroids'
)
plt.legend(scatterpoints=1)
plt.grid()
plt.show()

X=file.iloc[:,2:4].values

kmodel = KMeans(n_clusters=2, init='random',n_init=10, max_iter=300, random_state=2021)
y_label = kmodel.fit_predict(X)

# plot the 2 clusters
plt.scatter(X[y_label == 0, 0], X[y_label == 0, 1],s=50, c='lightgreen',marker='s',label='cluster 1')

plt.scatter(X[y_label == 1, 0], X[y_label == 1, 1],s=50, c='orange',marker='*',label='cluster 2')

plt.scatter(kmodel.cluster_centers_[:, 0], kmodel.cluster_centers_[:, 1],
    s=100, marker='o',
    c='red',
    label='centroids'
)
plt.legend(scatterpoints=1)
plt.grid()
plt.show()

