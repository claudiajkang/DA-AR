#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    tc = 0
    energy = 100
    e = 0
    tr = []

    for i in range(n):
        energy -= 1
        tc += k
        if tc >= (len(c)):
            tc = tc - (len(c))
        tr.append(tc)
        if c[tc] == 1:
            energy -= 2

        if tc == 0:
            break

    return energy



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
