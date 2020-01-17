#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the largestRectangle function below.
def largestRectangle(h):
    sortedH = sorted(list(set(h)), reverse=True)
    SORT = dict()
    tmax = min(h) * len(h)

    for idx, val in enumerate(h):
        if val not in SORT.keys():
            SORT[val] = list()

        SORT[val].append(idx)

    tlist = []
    for i in range(len(sortedH)):
        th = sortedH[i]
        tlist = tlist + SORT[th]
        tlist = sorted(tlist)

        if len(tlist) > 1:
            k = 0
            ta = 0
            c = 0
            for j in range(len(tlist)):
                if j == 0:
                    if (tlist[j+1] - tlist[j]) == abs(1):
                        k = 1
                        c = 1
                    continue

                if (tlist[j] - tlist[j-1]) == abs(1):
                    if c == 0:
                        c = 1
                    k += 1
                else:
                    ta = k
                    k = 0
                    c = 0

            if k <= 1:
                continue

            if ta > k:
                k = ta

            res = k * th

            if res > tmax:
                tmax = res

    return tmax

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
