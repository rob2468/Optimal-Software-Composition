from data import PNUM
from data import SNUM

import random
import pprint

''' generate simulate data
1. model structure
    P0    P1    P2    P3    P4

    S00   S10   S20   S30   S40
    S01   S11   S21   S31   S41
    S02   S12   S22   S32   S42
    S03   S13   S23   S33   S43
    S04   S14   S24   S34   S44
    
2. storage structure
a. There is a list PROC that stores PNUM-1 items. Each item is a matrix.
b. For the matrix[i], it is SNUM*SNUM and stores the softwareCO information between PROC[i] and PROC[i+1].
'''

PROC = []
for i in range(PNUM-1):
    ''' construct matrixes'''
    matrix = []
    for j in range(SNUM):
        row = []
        for m in range(SNUM):
            row.append(random.randint(0, 50))
        matrix.append(row)
    PROC.append(matrix)

if __name__=="__main__":
    pprint.pprint(PROC)

