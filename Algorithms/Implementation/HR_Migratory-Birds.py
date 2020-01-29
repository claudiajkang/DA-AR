#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    res = dict()

    for i in arr:
        if i not in res.keys():
            res[i] = 0

        res[i] += 1

    max = 0
    results = 0
    sorted_keys = sorted(res.keys())

    for j in sorted_keys:
        if res[j] > max:
            results = j
            max = res[j]

    return results


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
