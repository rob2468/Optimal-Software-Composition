#!/usr/bin/env python

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
def simpleAlg(maxcount):
    '''
    output:
        a tuple: the optimal composition of the PNUM processes
    '''
    maxcount[0] = -1     # maximum value among all of the compositions
    com = [[]]            # software composition of the maxcount
    composition = []    # variable used for iteration
    accum = 0           # accumulation
    composeSoftware(maxcount, com, composition[:], accum)
    
    return com[0]


# optimized algorithm
# supposed complexity: O(PNUM*(SNUM^2))
def optimizedAlg(maxcount):
    c = []
    pre = []
    for i in range(PNUM):
        var1 = []
        for j in range(SNUM):
            var1.append(0)
        c.append(var1[:])
        pre.append(var1[:])
    
    maxcount[0] = -1
    nextVar = -1
    com = []
    
    for i in range(1, PNUM):
        for j in range(SNUM):
            for k in range(SNUM):
                matrix = PROC[i-1]
                var = matrix[k][j]
                if c[i-1][k] + var > c[i][j]:
                    c[i][j]=c[i-1][k] + var
                    pre[i][j] = k
    
    # find he longest path
    for i in range(SNUM):
        if maxcount[0] < c[PNUM-1][i]:
            nextVar = i
            maxcount[0] = c[PNUM-1][i]
    for i in range(PNUM-1, -1, -1):
        com.insert(0, nextVar)
        nextVar = pre[i][nextVar]        
    return com

if __name__=="__main__":
    print "process number: ", (PNUM)
    print "software number: " , (SNUM)
    
    maxcount = [-1]
    # measure the simple algorithm
    starttime=time.time()
    com = simpleAlg(maxcount)
    endtime=time.time()
    print "Simple Algorithm: ", (endtime-starttime)*1000, "ms"
    print "maxcount: ", maxcount[0]
    print "the optimal software composition: ", com
    print ""

    # measure the optimized algorithm
    starttime=time.time()
    com = optimizedAlg(maxcount)
    endtime=time.time()
    print "Optimized Algorithm: ", (endtime-starttime)*1000, "ms"
    print "maxcount: ", maxcount[0]
    print "the optimal software composition: ", com
    print ""
