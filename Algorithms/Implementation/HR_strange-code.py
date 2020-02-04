#!/bin/python3

import math
import os
import random
import re
import sys


def strangeCounter(t):
    cycle = 0
    value = list()

    if len(str(t)) >= 10:
        cycle = 10

    for i in range(t):
        tv = 3 * (1 << cycle)
        if tv <= t:
            if tv not in value:
                value.append(tv)
                cycle += 1

        else:
            start_time = value[-1] + 1
            value.append(tv)
            break


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    result = strangeCounter(t)

    fptr.write(str(result) + '\n')

    fptr.close()
