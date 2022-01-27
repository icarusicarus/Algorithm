#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getMaxUnits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER_ARRAY boxes
#  2. LONG_INTEGER_ARRAY unitsPerBox
#  3. LONG_INTEGER truckSize
#

def getMaxUnits(boxes, unitsPerBox, truckSize):
    # Write your code here
    pairs = list(zip(boxes, unitsPerBox))
    
    sorted_list = sorted(pairs, key= lambda item: item[1], reverse=True)
    
    numBoxes = 0
    numUnits = 0
    
    for i in range(len(sorted_list)):
        if numBoxes + sorted_list[i][0] < truckSize:
            numUnits += sorted_list[i][0] * sorted_list[i][1]
            numBoxes += sorted_list[i][0]
        else:
            numUnits += (truckSize - numBoxes) * sorted_list[i][1]
            break
    return numUnits
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    boxes_count = int(input().strip())

    boxes = []

    for _ in range(boxes_count):
        boxes_item = int(input().strip())
        boxes.append(boxes_item)

    unitsPerBox_count = int(input().strip())

    unitsPerBox = []

    for _ in range(unitsPerBox_count):
        unitsPerBox_item = int(input().strip())
        unitsPerBox.append(unitsPerBox_item)

    truckSize = int(input().strip())

    result = getMaxUnits(boxes, unitsPerBox, truckSize)

    fptr.write(str(result) + '\n')

    fptr.close()
