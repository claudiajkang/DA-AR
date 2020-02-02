#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def minimumDistances(a):
    t = dict()
    vlist = set()
    alen = len(a)

    for i in range(alen):
        idx = a[i]
        if idx not in t.keys():
            t[idx] = list()

        t[idx].append(i)

        if len(t[idx]) >= 2:
            vlist.add(idx)

    if len(vlist) >= 1:
        res = list()

        for i in vlist:
            temp = t[i]
            d = abs(temp[0]-temp[1])
            res.append(d)

        return min(res)

    else:
        return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
