#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the plusMinus function below.
def plusMinus(arr):
    alen = len(arr)
    dec = []
    neg = []
    zero = []

    for i in arr:
        if i > 0:
            dec.append(i)
        elif i < 0:
            neg.append(i)
        else:
            zero.append(i)

    print(round((len(dec) / alen), 6))
    print(round((len(neg) / alen), 6))
    print(round((len(zero) / alen), 6))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
