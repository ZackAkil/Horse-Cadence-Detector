from __future__ import division
from scipy import optimize
import matplotlib.pyplot as plt
import numpy as np

def model(peakCantThreshold,peakTrotThreshold, peakCantFrequencyThreshold, peakTrotFrequencyThreshold,sampleWindow, data):
    
    inTrotPeakFlag = False
    inCantPeakFlag = False
    validTrotPeaks = 0
    validCantPeaks = 0
    time = 0;
    output = []
    
    for row in data:
        time += 1
        #enter peak
        if(row > peakTrotThreshold) and (not inTrotPeakFlag):
            inTrotPeakFlag = True
        elif(row < peakTrotThreshold) and inTrotPeakFlag:
            inTrotPeakFlag = False
            validTrotPeaks += 1
            
        if(row > peakCantThreshold) and (not inCantPeakFlag):
            inCantPeakFlag = True
        elif(row < peakCantThreshold) and inCantPeakFlag:
            inCantPeakFlag = False
            validCantPeaks += 1
        
        #after sample wind passes log prediction to array
        if(time > sampleWindow):
            label = 0
            if(validCantPeaks > peakCantFrequencyThreshold):
                label = 2
            elif(validTrotPeaks > peakTrotFrequencyThreshold):
                label = 1
            
            for i in range(int(sampleWindow)):
                output.append(label)
            validTrotPeaks = 0
            validCantPeaks = 0
            time = 0
    while(len(output) < len(data)):
        output.append(0)
    return output


def fetchTrainingData():
    from numpy import genfromtxt
    a = genfromtxt('horse trianing data.csv', delimiter=',',skip_header =True)
    return a

def costFunction(theta):
    prediction = predict(theta)
    actual =  (trainingData[:,2] *2) + trainingData[:,1] 
    absCost = ((np.absolute(prediction - actual)) >= 1).astype(int)
    finalCost = sum(absCost)/len(absCost)
    progress.append(finalCost)
    return finalCost

def optimizeTheta():
    sol = optimize.minimize(costFunction,x0=[0.00001,0.00001,0.01,0.01],method='Powell',options={'maxiter' : 100000})#Nelder-Mead
    return sol

def predict(theta):
    scaledTheta = scaleFeatures(theta)
    return model(scaledTheta[0],scaledTheta[1],scaledTheta[2],scaledTheta[3],100,trainingData[:,0])
    
def scaleFeatures(theta):
    return [theta[0]*700000000,theta[1]*700000000,theta[2]*300,theta[3]*300]
    

trainingData = fetchTrainingData()
progress = []
#plt.plot(trainingData)
#plt.show()

sol = optimizeTheta()
plt.figure(0)
plt.plot(progress)


plt.figure(1)
plt.plot(trainingData[:,0])
plt.plot(np.array(trainingData[:,2] )*10000,linewidth=4)
plt.plot(np.array(predict(sol.x))*10000,linewidth=2)

finalBottom = sol.x[0]*700000

num = int(len(trainingData[:,2])/100)
for i in range(num):
    plt.axvline(x=i*100,linestyle='dashed',color='r') 

#plt.axhline(y=finalTop)
#plt.axhline(y=finalBottom)
output = scaleFeatures(sol.x)
plt.axhline(y=output[0])
#plt.axhline(y=finalBottom)
print("bttom line",finalBottom)

plt.show()