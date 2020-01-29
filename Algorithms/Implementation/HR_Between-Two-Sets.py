#!/bin/python3

import math
import os
import random
import re
import sys


def getTotalX(a, b):
    tlist = []
    res = []
    al = len(a)
    bl = len(b)

    for i in range(a[-1], b[0] + 1):
        c = 0
        for j in a:
            if i % j == 0:
                c += 1

        if c == al:
            tlist.append(i)

    for i, v in enumerate(tlist):
        c = 0

        for j in b:
            if j % v == 0:
                c += 1

        if c == bl:
            res.append(tlist[i])

    return len(res)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
