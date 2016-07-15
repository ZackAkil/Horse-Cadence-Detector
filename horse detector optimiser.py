from scipy import special, optimize
import matplotlib.pyplot as plt
import numpy as np

def model(peakThresholdMin,peakThresholdRange, peakWidthThresholdMin,peakWidthThresholdRange, peakFrequencyThresholdMin, peakFrequencyThresholdRange,sampleWindow, data):

    #return np.array([1,1,1,1,1,1,1])
    #print("raw",peakThresholdMin,peakThresholdRange, peakWidthThresholdMin,peakWidthThresholdRange, peakFrequencyThresholdMin, peakFrequencyThresholdRange,sampleWindow)
    inPeakFlag = False
    validPeakAmp = True
    currentPeakWidth = 0
    validPeaks = 0
    #sampleWindow = 20
    time = 0;
    output = []

    for row in data:

        time += 1
        feed = row

        #enter peak
        if(feed > peakThresholdMin) and (not inPeakFlag):
            inPeakFlag = True
            #print("peaked")
        #exit peak
        elif(feed < peakThresholdMin) and inPeakFlag:
            inPeakFlag = False
            #count if peak width is valid
            if((peakWidthThresholdMin < currentPeakWidth < (peakWidthThresholdMin + peakWidthThresholdRange)) and validPeakAmp ):
                validPeaks += 1
                #print("valid peak", currentPeakWidth,time)
            currentPeakWidth = 0
            validPeakAmp = True

        #time peak width
        if inPeakFlag:
            currentPeakWidth += 1

        #if feed > (peakThresholdRange):
         #   validPeakAmp = False

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
    actual =  trainingData[:,2] #+ trainingData[:,1] 
    
    #print("pred",sum(prediction), sum(actual))
    
    absCost = np.absolute(prediction - actual)
    finalCost = sum(absCost)/len(absCost)
    #print('ran',finalCost,theta)
    progress.append(finalCost)
    return finalCost

def optimizeTheta():

    sol = optimize.minimize(costFunction,x0=[0.1,0.1,0.1,0.1,0.1,0.1],method='Powell')#Nelder-Mead
    return sol

def predict(theta):
    scaledTheta = scaleFeatures(theta)
    return model(scaledTheta[0],scaledTheta[1],scaledTheta[2],scaledTheta[3],scaledTheta[4],scaledTheta[5],100,trainingData[:,0])
    
def scaleFeatures(theta):
    return [theta[0]*70000,theta[1]*150000,theta[2]*10,theta[3]*40,theta[4]*30,theta[5]*30]
    

trainingData = fetchTrainingData()
progress = []
#plt.plot(trainingData)
#plt.show()

sol = optimizeTheta()
plt.figure(0)
plt.plot(progress)


plt.figure(1)
plt.plot(trainingData[:,0])
plt.plot(np.array(trainingData[:,2])*10000,linewidth=4)
plt.plot(np.array(predict(sol.x))*10000,linewidth=2)

finalBottom = sol.x[0]*700000
finalTop = finalBottom + sol.x[1]*50000

num = int(len(trainingData[:,2])/100)
for i in range(num):
    plt.axvline(x=i*100,linestyle='dashed',color='r') 

#plt.axhline(y=finalTop)
#plt.axhline(y=finalBottom)
output = scaleFeatures(sol.x)
#plt.axhline(y=finalTop)
#plt.axhline(y=finalBottom)
print("bttom line",finalBottom, "top line",finalTop)

plt.show()


