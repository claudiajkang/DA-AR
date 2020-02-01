#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):
    res = list()

    for i in range(p, q+1):
        il = len(str(i))
        d = pow(10, il)
        n = i * i

        l = int(n / d)
        r = int(n % d)

        if (l+r) == i:
            res.append(str(i))

    if len(res) == 0:
        print("INVALID RANGE")

    else:
        pr = ' '.join(res)

        print(pr)

if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)
