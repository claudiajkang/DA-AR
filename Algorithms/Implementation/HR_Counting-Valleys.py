#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    slevel = 0
    trace = []
    res = 0

    for i in s:
        trace.append(slevel)

        if i == "U":
            slevel += 1

        elif i == "D":
            slevel -= 1

        if trace[-1] < 0 and slevel == 0:
            res += 1

    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
