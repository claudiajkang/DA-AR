#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the chocolateFeast function below.
def chocolateFeast(n, c, m):
    choco = int(n / c)
    remain = choco

    while True:
        returns = int(remain / m)

        if returns == 0:
            break

        remain = remain - (m * returns) + returns
        choco += returns

    return choco


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        ncm = input().split()

        n = int(ncm[0])

        c = int(ncm[1])

        m = int(ncm[2])

        result = chocolateFeast(n, c, m)

        fptr.write(str(result) + '\n')

    fptr.close()
