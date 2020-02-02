#!/bin/python3

import math
import os
import random
import re
import sys


def workbook(n, k, arr):
    res = list()
    special = 0

    for i in arr:
        q = int(i/k)
        r = i % k
        pn = 0
        for j in range(q):
            pn += k
            res.append(pn)

        if r:
            res.append(pn+r)

    for i in range(1, len(res)+1):
        if (i == 1) and (i <= res[i-1]):
            special += 1
        else:
            if res[i-1] <= k:
                base = 1
            else:
                base = res[i-2] + 1

            if base <= i <= res[i-1]:
                special += 1

    return special


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
