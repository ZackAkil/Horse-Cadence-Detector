from __future__ import division
from scipy import optimize
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans

def fetchTrainingData():
    from numpy import genfromtxt
    a = genfromtxt('horse data with labels.csv', delimiter=',',skip_header =True)
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

def convertData3(data):
    currentPeakSum = 0
    time = 0
    time2 = 0
    output = []
    sampleWindow = 100
    subSampleWindow = 70
    currentArea = []
    currentSub = []

    for x in range(sampleWindow):
        output.append(0)
    
    for row in data:
        time += 1
        time2 += 1
        #enter peak
        
        #after sample wind passes log prediction to array
        if(time > sampleWindow):
            for i in range(int(sampleWindow)):
                calc = sum(currentArea)/len(currentArea)
                output.append(calc)
            currentArea = []
            time = 0

        currentSub.append(row)
        
        if(time2 > subSampleWindow):
            currentArea.append(max(currentSub))
            currentSub = []
            time2 = 0
            
    while(len(output) < len(data)):
        output.append(output[len(output)-1])
    return output

def convertData4(data):

    time = 0
    output = []
    subSampleCount = 4
    subSampleWindow = 25
    
    sampleSum = 0
    currentMax = 0
    sampleCount = 0

    #for x in range(subSampleWindow*subSampleCount):
     #   output.append(0)
    
    for row in data:
        time += 1
        
        if row > currentMax:
            currentMax = row
        
        if time == subSampleWindow:
            sampleSum += currentMax
            sampleCount += 1
            time = 0
            currentMax = 0
        
        if sampleCount == subSampleCount:
            val = sampleSum / subSampleCount
            for x in range(subSampleWindow*subSampleCount):
                output.append(val)
            sampleSum = 0
            sampleCount = 0
            
    while(len(output) < len(data)):
        output.append(output[len(output)-1])
    return output
    
    
def predict(data, still, walk, trot, cant):
    time = 0
    output = []
    subSampleCount = 4
    subSampleWindow = 25
    
    sampleSum = 0
    currentMax = 0
    sampleCount = 0

    #for x in range(subSampleWindow*subSampleCount):
     #   output.append(0)
    
    for row in data:
        time += 1
        
        if row > currentMax:
            currentMax = row
        
        if time == subSampleWindow:
            sampleSum += currentMax
            sampleCount += 1
            time = 0
            currentMax = 0
        
        if sampleCount == subSampleCount:
            val = sampleSum / subSampleCount
            setVal = 0
            if val < still:
                setVal = 0
            elif val < walk:
                setVal = 1
            elif val< trot:
                setVal = 2
            elif val < cant:
                setVal = 3
                
            for x in range(subSampleWindow*subSampleCount):
                output.append(setVal)
            sampleSum = 0
            sampleCount = 0
            
    while(len(output) < len(data)):
        output.append(output[len(output)-1])
    return output

fetch = fetchTrainingData()

data = fetch[:,0]

dataConvert = np.array(convertData4(data))


y_pred = KMeans(n_clusters=3, random_state=170).fit_predict(dataConvert.reshape(-1, 1))

index = np.arange(y_pred.shape[0])

#plt.plot(np.ones(y_pred.shape[0]))
plt.figure(0)
plt.scatter(index, data,c = y_pred,edgecolors='none')
plt.plot(index,fetch[:,2],linewidth=3)
plt.plot(index,fetch[:,3],c ='r',linewidth=3)
plt.plot(dataConvert,linewidth=2)

plt.figure(1)
plt.plot(data)
plt.plot(index,fetch[:,2])
plt.plot(index,fetch[:,3],c ='r')
plt.plot(dataConvert)
plt.plot(index,fetch[:,2])
plt.plot(index,fetch[:,3],c ='r')
plt.show()

predictVal = predict(data, 4500, 7000, 11500, 20000)
#print(predictVal)
plt.figure(2)
plt.scatter(index, data,c = predictVal,edgecolors='none')
plt.plot(index,fetch[:,2],linewidth=3)
plt.plot(index,fetch[:,3],c ='r',linewidth=3)
plt.plot(dataConvert,linewidth=2)
plt.show()

print(8)
