from number_gen import numberGen
import numpy as np

#Inverse CDF of X that generates realizations of X based on u
def invCDF(u):
    return -12*np.log(1-u)

numGen = numberGen()

#Defines some constants related to the experiment
probAvail = 0.5
probBusy = 0.2
probUnavail = 0.3
dialTime = 6
endCall = 1
detectBusy = 3
maxRing = 25

sample = []
sampleSize = 1000
for i in range(sampleSize):
    #Sets calling time and number of calls to 0.
    w = 0
    n = 0
    while(n < 4):
        #Increments number of calls
        n += 1
        #Increments dial time
        w += dialTime
        u = numGen.getNext()

        #If u is < 0.5 the customer is available to pick up the phone in X time
        if(u <= probAvail):
            u = numGen.getNext()
            x = invCDF(u)
            if(x > 25):
                w += maxRing
                w += endCall
            else:
                w += x
                n = 4
        #If u is between 0.5 and 0.8, the customer is not available to pick up the phone
        elif(u > probAvail and u <= (probAvail+probUnavail)):
            w += maxRing
            w += endCall
    
        #If u is between 0.8 and 1, the line is busy
        else:
            w += detectBusy
            w += endCall

    #Adds amount of call time to the sample
    sample.append(w)

np.savetxt('data.txt', sample)
