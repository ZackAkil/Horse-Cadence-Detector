from scipy import special, optimize
import matplotlib.pyplot as plt
import numpy as np

def model(peakThreshold, peakWidthThresholdMin,peakWidthThresholdRange, peakFrequencyThresholdMin, peakFrequencyThresholdRange,sampleWindow, data):

    #return np.array([1,1,1,1,1,1,1])
    print("raw",peakThreshold, peakWidthThresholdMin,peakWidthThresholdRange, peakFrequencyThresholdMin, peakFrequencyThresholdRange,sampleWindow)
    inPeakFlag = False
    currentPeakWidth = 0
    validPeaks = 0
    #sampleWindow = 20
    time = 0;
    output = []

    for row in data:

        time += 1
        feed = row

        #enter peak
        if(feed > peakThreshold) and (not inPeakFlag):
            inPeakFlag = True
            #print("peaked")
        #exit peak
        elif(feed < peakThreshold) and inPeakFlag:
            inPeakFlag = False
            #count if peak width is valid
            if(peakWidthThresholdMin < currentPeakWidth < (peakWidthThresholdMin + peakWidthThresholdRange) ):
                validPeaks += 1
                #print("valid peak", currentPeakWidth,time)
            currentPeakWidth = 0

        #time peak width
        if inPeakFlag:
            currentPeakWidth += 1

        #after sample wind passes log prediction to array
        if(time > sampleWindow):
            label = 1 if(peakFrequencyThresholdMin < validPeaks < (peakFrequencyThresholdMin + peakFrequencyThresholdRange) ) else 0
            for i in range(int(sampleWindow)):
                output.append(label)

            validPeaks = 0
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
    
    #actual = np.array([0,1,1,1,0,1,1])
    actual = trainingData[:,2]
    
    print("pred",sum(prediction), sum(actual))
    
    absCost = np.absolute(prediction - actual)
    finalCost = sum(absCost)/len(absCost)
    print('ran',finalCost,theta)
    progress.append(finalCost)
    return finalCost

def optimizeTheta():

    sol = optimize.minimize(costFunction,x0=[0.1,0.1,0.1,0.1,0.1],method='Powell')
    return sol

def predict(theta):
    return model(theta[0]*70000,theta[1]*10,theta[2]*40,theta[3]*30,theta[4]*30,100,trainingData[:,0])
    

trainingData = fetchTrainingData()
progress = []
#plt.plot(trainingData)
#plt.show()

sol = optimizeTheta()
plt.figure(0)
plt.plot(progress)


plt.figure(1)
plt.plot(np.array(predict(sol.x))*10000)
plt.plot(np.array(trainingData[:,2])*10000)
plt.plot(trainingData[:,0])
plt.show()



