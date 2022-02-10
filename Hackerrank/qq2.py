#!/bin/python3

# input output
# 001100011 6
# 000110    3
# 010101010 8

import math
import os
import random
import re
import sys


#
# Complete the 'getSubstringCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#


def getSubstringCount(s):
    # Write your code here
    count_list = []
    cnt = 1
    for i in range(1, len(s)):
        if s[i - 1] == s[i]:
            cnt += 1
        else:
            count_list.append(cnt)
            cnt = 1
    count_list.append(cnt)

    result = 0
    for i in range(1, len(count_list)):
        result += min(count_list[i - 1], count_list[i])

    return result


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    s = input()

    result = getSubstringCount(s)

    fptr.write(str(result) + "\n")

    fptr.close()
