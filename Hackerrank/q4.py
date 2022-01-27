#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'chooseFlask' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY requirements
#  2. INTEGER flaskTypes
#  3. 2D_INTEGER_ARRAY markings
#

def chooseFlask(requirements, flaskTypes, markings):
    # Write your code here
    reqDict = {}
    for mark in markings:
        if mark[0] in reqDict:
            reqDict[mark[0]].append(mark[1])
        else:
            reqDict[mark[0]] = [mark[1]]
    
    maxReq = max(requirements)
    totalDict = {}
    for req in reqDict:
        if max(reqDict[req]) < maxReq:
            continue
        n_sum = 0
        for r in requirements:
            n_min = 99999999
            for i in reqDict[req]:
                if n_min > abs(i - r):
                    n_min = abs(i - r)
            n_sum += n_min
        totalDict[req] = n_sum
    
    return min(totalDict, key=lambda x: totalDict[x])
    
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    requirements_count = int(input().strip())

    requirements = []

    for _ in range(requirements_count):
        requirements_item = int(input().strip())
        requirements.append(requirements_item)

    flaskTypes = int(input().strip())

    markings_rows = int(input().strip())
    markings_columns = int(input().strip())

    markings = []

    for _ in range(markings_rows):
        markings.append(list(map(int, input().rstrip().split())))

    result = chooseFlask(requirements, flaskTypes, markings)

    fptr.write(str(result) + '\n')

    fptr.close()
