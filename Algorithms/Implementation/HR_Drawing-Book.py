#!/bin/python3

import os
import sys


#
# Complete the pageCount function below.
#
def pageCount(n, p):
    res = [0, 0]
    bc = 0
    c = 0

    for i in range(1, p + 1):
        if i == 1:
            bc = 2
        else:
            if bc == 2:
                c += 1
                bc = 0
            bc += 1

    res[0] = c
    c = 0
    bc = 0

    for i in range(n, p - 1, -1):
        if i == n:
            if i % 2 == 1:
                bc = 1
            else:
                bc = 2
        else:
            if bc == 2:
                c += 1
                bc = 0

            bc += 1

    res[1] = c

    return min(res)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
