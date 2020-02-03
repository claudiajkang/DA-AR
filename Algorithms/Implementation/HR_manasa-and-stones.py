#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the stones function below.
def stones(n, a, b):
    res = list()
    width = n - 1
    cases = list()
    c = 0

    for i in range(width+1):
        plist = list()
        for j in range(c):
            plist.append(1)

        for k in range(c, width):
            plist.append(0)

        c += 1
        cases.append(plist)

    for k in cases:
        p = 0
        for i in k:
            if i:
                p += a
            else:
                p += b
        res.append(p)

    results = sorted(list(set(res)))

    return results


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        n = int(input())

        a = int(input())

        b = int(input())

        result = stones(n, a, b)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
