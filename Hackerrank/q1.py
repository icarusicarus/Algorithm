#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'maxDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY px as parameter.
#

def maxDifference(px):
    # Write your code here
    n_max = 0
    n_min = px[0]
    for i in range(1, len(px)):
        if px[i] < n_min:
            n_min = px[i]
        if px[i] > px[i-1]:
            if n_max < px[i] - n_min:
                n_max = px[i] - n_min
    
    return n_max if n_max > 0 else -1
                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    px_count = int(input().strip())

    px = []

    for _ in range(px_count):
        px_item = int(input().strip())
        px.append(px_item)

    result = maxDifference(px)

    fptr.write(str(result) + '\n')

    fptr.close()
