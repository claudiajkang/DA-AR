#!/bin/python3

import math
import os
import random
import re
import sys

def repeatedString(s, n):
    ls = len(s)
    v = 'a'

    if ls == 1 and s == v:
        return n

    else:
        nc = s.count(v)
        repeat = int(n/ls)

        tc = n - (repeat*ls)
        res = nc * repeat

        if tc == 0:
            return res

        tlist = list()
        c = 0

        for i in range(tc):
            if c == ls:
                c = 0
            tlist.append(s[c])
            c += 1

        res = res + tlist.count(v)

        return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
