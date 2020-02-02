#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulTriplets function below.
def beautifulTriplets(d, arr):
    res = 0

    for i in range(len(arr)):
        c = 0
        tlist = list()

        for j in range(i, len(arr)):
            v = arr[i] + d * c
            try:
                idx = arr.index(v)
            except ValueError:
                break

            if len(tlist) == 3:
                break

            tlist.append(v)
            c += 1

        if len(tlist) == 3:
            res += 1

    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
