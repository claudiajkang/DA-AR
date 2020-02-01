#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(n):
    t = str(n)
    tn = list(t)
    digits = list()

    for i in tn:
        if int(i) == 0:
            continue

        if n % int(i) == 0:
            digits.append(i)

    return len(digits)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
