#!/bin/python3

import math
import os
import random
import re
import sys

def fairRations(B):
    blen = len(B)
    even = 0
    c = 0

    def is_even(v):
        if v % 2 == 0:
            return True
        return False

    for i in range(blen):
        if i != (blen-1) and not is_even(B[i]):
            B[i] += 1
            c += 2
            B[i+1] += 1
        if is_even(B[i]):
            even += 1

    if even == len(B):
        return c

    else:
        return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)

    fptr.write(str(result) + '\n')

    fptr.close()
