#!/bin/python3

import math
import os
import random
import re
import sys

def largestRectangle(h):
    sortedh = sorted(h, reverse=True)
    k = []
    tmax = 0
    th = 0

    for i in sortedh:
        for j in range(len(h)):
            if h[j] >= i:
                if len(k) == 0:
                    k.append(j)
                elif (j-k[-1]) == abs(1):
                    k.append(j)
            else:
                res = i * len(k)
                if res > tmax:
                    tmax = res
                k = []

        res = i * len(k)
        if res > tmax:
            tmax = res

        k = []
    return tmax


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
