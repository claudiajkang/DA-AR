#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    res = dict()
    candle = 0

    for idx, val in enumerate(ar):
        if val not in res.keys():
            res[val] = 0
        res[val] += 1

    sorted_key = sorted(res.keys(), reverse=True)

    for r in sorted_key:
        candle = res[r]
        break

    return candle


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
