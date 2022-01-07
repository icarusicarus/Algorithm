#!/bin/python3

import math
import os
import random
import re
import sys


def arraySum(a):
    sum = 0
    for i in range(len(a)):
        sum += a[i]

    return sum


def formingMagicSquare(s):
    # Write your code here
    min = 999
    for i in range(3):
        sum = arraySum(s[i])

        if i == 0:
            # print(sum)
            distance = abs(sum - arraySum(s[1]))
            distance += abs(sum - arraySum(s[2]))
            # print("0: " + str(distance))
            if min > distance:
                min = distance

        if i == 1:
            # print(sum)
            distance = abs(sum - arraySum(s[0]))
            distance += abs(sum - arraySum(s[2]))
            # print("1: " + str(distance))
            if min > distance:
                min = distance

        if i == 2:
            # print(sum)
            distance = abs(sum - arraySum(s[0]))
            distance += abs(sum - arraySum(s[1]))
            # print("2: " + str(distance))
            if min > distance:
                min = distance
    return min


if __name__ == "__main__":
    s = [[4, 9, 2], [3, 5, 7], [8, 1, 5]]

    result = formingMagicSquare(s)

    # print(result)
