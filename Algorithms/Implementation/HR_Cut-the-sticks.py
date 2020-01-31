#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    tarr = arr
    res = list()

    while True:
        tl = len(tarr)
        if tl == 0:
            return res

        plist = []
        m = min(tarr)
        res.append(len(tarr))

        for i in range(tl):
            tarr[i] -= m
            if tarr[i] <= 0:
                plist.append(i)

        for p in range(len(plist)-1, -1, -1):
            v = tarr.pop(plist[p])



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
