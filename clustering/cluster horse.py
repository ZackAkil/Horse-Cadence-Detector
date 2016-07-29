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

def convertData(data):
    currentPeakSum = 0
    time = 0
    output = []
    sampleWindow = 100
    
    for row in data:
        time += 1
        #enter peak
        currentPeakSum += row
        
        #after sample wind passes log prediction to array
        if(time > sampleWindow):
            
            for i in range(int(sampleWindow)):
                output.append(currentPeakSum/sampleWindow)

            time = 0
            currentPeakSum = 0
    while(len(output) < len(data)):
        output.append(output[len(output)-1])
    return output

def convertData2(data):
    currentPeakSum = 0
    time = 0
    output = []
    sampleWindow = 100
    currentArea = []
    
    for row in data:
        time += 1
        #enter peak
        currentPeakSum += row
        currentArea.append(row)
        #after sample wind passes log prediction to array
        if(time > sampleWindow):
            
            for i in range(int(sampleWindow)):
                output.append(max(currentArea))
            currentArea = []
            time = 0
            currentPeakSum = 0
    while(len(output) < len(data)):
        output.append(output[len(output)-1])
    return output
    

data = (fetchTrainingData())[:10000]

dataConvert = np.array(convertData2(data))


#plt.plot(data)
index = np.arange(data.shape[0])

#index = np.ones(data.shape[0])

y_pred = KMeans(n_clusters=4, random_state=170).fit_predict(dataConvert.reshape(-1, 1))

#plt.plot(np.ones(y_pred.shape[0]))
plt.figure(0)
plt.scatter(index, data,c = y_pred,edgecolors='none')
plt.figure(1)
plt.plot(data)
plt.figure(2)
plt.plot(dataConvert)
plt.show()

print(8)
