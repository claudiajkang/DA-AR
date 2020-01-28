#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the breakingRecords function below.
def breakingRecords(scores):
    high = None
    low = None
    res = [0, 0]

    for i in scores:
        if high is None:
            high = i
        elif (i > high) and (i != high):
            res[0] += 1
            high = i

        if low is None:
            low = i
        elif (i < low) and (i != low):
            res[1] += 1
            low = i

    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
