#!/bin/python3

import math
import os
import random
import re
import sys


def flatlandSpaceStations(n, c):
    res = list()
    c = sorted(c)

    if n == len(c):
        return 0

    for i in range(len(c)):
        if i == 0:
            if 0 < c[i]:
                for j in range(0, c[i]):
                    v = abs(j - c[i])
                    res.append(v)
            continue
        else:
            for j in range(c[i-1], c[i]):
                v1 = abs(j-c[i-1])
                v2 = abs(j-c[i])
                v = min(v1, v2)
                res.append(v)

    if c[-1] < n:
        for j in range(c[-1], n):
            v = abs(j - c[-1])
            res.append(v)

    return max(res)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()
