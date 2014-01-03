from gensimudata import PNUM
from gensimudata import SNUM
from gensimudata import PROC

import time
import pprint

def composeSoftware(maxcount, com, composition, accum):
    if len(composition) == PNUM-1:
        for i in range(SNUM):
            tempComposition = composition[:]
            tempComposition.append(i)
            
            tempAccum = accum
            idxProcess = len(tempComposition)-1
            matrix = PROC[idxProcess-1]
            row = tempComposition[idxProcess-1]
            col = tempComposition[idxProcess]
            tempAccum += matrix[row][col]
            
            if tempAccum > maxcount[0]:
                maxcount[0] = tempAccum
                com[0] = tempComposition
    else:
        for i in range(SNUM):
            tempComposition = composition[:]
            tempComposition.append(i)
            
            tempAccum = accum
            idxProcess = len(tempComposition)-1
            if idxProcess != 0:
                matrix = PROC[idxProcess-1]
                row = tempComposition[idxProcess-1]
                col = tempComposition[idxProcess]
                tempAccum += matrix[row][col]
            composeSoftware(maxcount, com, tempComposition[:], tempAccum)

# simple algorithm
# supposed complexity: O(SNUM^PNUM)
def simpleAlg():
    '''
    
    output:
        a tuple: the optimal composition of the PNUM processes
    '''
    maxcount = [-1]     # maximum value among all of the compositions
    com = [[]]            # software composition of the maxcount
    composition = []    # variable used for iteration
    accum = 0           # accumulation
    composeSoftware(maxcount, com, composition[:], accum)
    
    return com[0]

# optimized algorithm
# supposed complexity: O(PNUM*(SNUM^2))
def optimizedAlg():
    pass

if __name__=="__main__":
    print "process number: " + repr(PNUM)
    print "software number: " + repr(SNUM)
    
    # measure the simple algorithm
    starttime=time.time()
    com = simpleAlg()
    endtime=time.time()
    print "Simple Algorithm: " + repr(endtime-starttime)
    print com

    starttime=time.time()
    com = optimizedAlg()
    endtime=time.time()
    print "Optimized Algorithm: " + repr(endtime-starttime)
