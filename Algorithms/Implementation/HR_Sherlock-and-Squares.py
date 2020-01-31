#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the squares function below.
def squares(a, b):
    s = list()
    c = 0
    i = 1

    while True:
        v = i * i
        if v <= b:
            s.append(v)
            i += 1
        else:
            break

    for j in range(b):
        if len(s) == j:
            break
        elif a <= s[j] <= b:
            c += 1
        elif s[j] > b:
            break

    return c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
