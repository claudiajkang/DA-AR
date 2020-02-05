#!/bin/python3

import math
import os
import random
import re
import sys


def strangeCounter(t):
    value = [3]
    si = 0
    time = [1]

    if t <= 3:
        c = 4
        for i in range(t):
            c -= 1

        return c

    for i in range(t):
        nv = value[-1] * 2
        value.append(nv)
        if t < (nv * 2):
            break

    for j in range(1, len(value)):
        time.append(time[j - 1] + value[j - 1])
        if time[j-1] <= t < time[j]:
            si = j
        elif t >= time[j]:
            si = j

    rvalue = value[si]

    for j in range(time[si], t+1):
        if j == t:
            return rvalue
        rvalue -= 1

    return 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    result = strangeCounter(t)

    fptr.write(str(result) + '\n')

    fptr.close()
