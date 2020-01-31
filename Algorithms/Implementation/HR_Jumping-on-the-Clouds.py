#!/bin/python3

import math
import os
import random
import re
import sys


def jumpingOnClouds(c):
    minc = 0

    cl = len(c) - 1
    d = 0

    while (d+1) <= cl:
        if (d+1) == cl:
            if c[d+1] == 0:
                d += 1
                minc += 1
        else:
            if (c[d + 1] == 0) and (c[d + 2] == 0):
                d += 2
            elif (c[d + 2] == 1) and (c[d + 1] == 0):
                d += 1
            elif (c[d + 1] == 1) and (c[d + 2] == 0):
                d += 2

            minc += 1

    return minc


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
