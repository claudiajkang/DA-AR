#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the equalizeArray function below.
def equalizeArray(arr):
    td = dict()

    for i in arr:
        if i not in td.keys():
            td[i] = 0
        td[i] += 1

    tdkeys = sorted(td.keys())

    res = [0 for i in range(len(tdkeys))]
    c = 0

    for i in tdkeys:
        for j in tdkeys:
            if i != j:
                res[c] += td[j]

        c += 1

    return min(res)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
