from scipy import optimize
import matplotlib.pyplot as plt
import numpy as np

def model(peakThresholdMin, peakFrequencyThresholdMin,sampleWindow, data):

    #return np.array([1,1,1,1,1,1,1])
    #print("raw",peakThresholdMin,peakThresholdRange, peakWidthThresholdMin,peakWidthThresholdRange, peakFrequencyThresholdMin, peakFrequencyThresholdRange,sampleWindow)
    inPeakFlag = False

    validPeaks = 0
    #sampleWindow = 20
    time = 0;
    output = []

    for row in data:

        time += 1

        #enter peak
        if(row > peakThresholdMin) and (not inPeakFlag):
            inPeakFlag = True
            #print("peaked")
        #exit peak
        elif(row < peakThresholdMin) and inPeakFlag:
            inPeakFlag = False
            #count if peak width is valid
            validPeaks += 1


        #after sample wind passes log prediction to array
        if(time > sampleWindow):
            label = 1 if(peakFrequencyThresholdMin < validPeaks) else 0
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

    sol = optimize.minimize(costFunction,x0=[0.0001,0.1],method='Powell')#Nelder-Mead
    return sol

def predict(theta):
    scaledTheta = scaleFeatures(theta)
    return model(scaledTheta[0],scaledTheta[1],100,trainingData[:,0])
    
def scaleFeatures(theta):
    return [theta[0]*70000000,theta[1]*30]
    

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
#plt.axhline(y=finalTop)
#plt.axhline(y=finalBottom)
print("bttom line",finalBottom)

plt.show()


