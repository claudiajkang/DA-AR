#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    tstack = list()
    start = ['(', '{', '[']
    end = [')', '}', ']']

    for t in range(len(s)):
        value = s[t]

        if len(tstack) == 0:
            tstack.append(value)
            continue

        if value in start:
            tstack.append(value)
            continue

        if value in end:
            svalue = tstack[-1]
            if svalue in start:
                index = start.index(svalue)
                if (svalue == start[index]) and (value == end[index]):
                    n = tstack.pop()
                    continue

            tstack.append(value)

    if len(tstack) == 0:
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()
        result = isBalanced(s)
        print(result)
        # fptr.write(result + '\n')

    # fptr.close()
