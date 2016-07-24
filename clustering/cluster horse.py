# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 16:35:23 2016

@author: zackakil
"""

from __future__ import division
from scipy import optimize
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans

def fetchTrainingData():
    from numpy import genfromtxt
    a = genfromtxt('horse cluster data.csv', delimiter=',',skip_header =True)
    return a

data = (fetchTrainingData())[:10000]

#plt.plot(data)
index = np.arange(data.shape[0])

#index = np.ones(data.shape[0])

y_pred = KMeans(n_clusters=4, random_state=170).fit_predict(data.reshape(-1, 1))

#plt.plot(np.ones(y_pred.shape[0]))
plt.figure(0)
plt.scatter(index, data,c = y_pred)
plt.figure(1)
plt.plot(data)

plt.show()

print(8)