#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'minimizeCost' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY numPeople
#  2. INTEGER_ARRAY x
#  3. INTEGER_ARRAY y
#
import numpy as np

def minimizeCost(numPeople, x, y):
    # Write your code here
    xs = []
    ys = []
    for i in range(len(numPeople)):
        xs.extend([x[i]] * numPeople[i])
        ys.extend([y[i]] * numPeople[i])
    
    minX = int(np.median(xs))
    minY = int(np.median(ys))
    
    minDist = 0
    for i in range(len(numPeople)):
        minDist += (abs(minX - x[i]) + abs(minY - y[i])) * numPeople[i]
    
    return minDist
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    numPeople_count = int(input().strip())

    numPeople = []

    for _ in range(numPeople_count):
        numPeople_item = int(input().strip())
        numPeople.append(numPeople_item)

    x_count = int(input().strip())

    x = []

    for _ in range(x_count):
        x_item = int(input().strip())
        x.append(x_item)

    y_count = int(input().strip())

    y = []

    for _ in range(y_count):
        y_item = int(input().strip())
        y.append(y_item)

    result = minimizeCost(numPeople, x, y)

    fptr.write(str(result) + '\n')

    fptr.close()
