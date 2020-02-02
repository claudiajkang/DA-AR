  #!/bin/python3

import math
import os
import random
import re
import sys

def howManyGames(p, d, m, s):
    r = 0
    c = 0
    b4 = p

    while r <= s:
        r += b4
        c += 1
        b4 -= d
        if b4 <= m:
            b4 = m
        if r > s:
            c -= 1

    return c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    pdms = input().split()

    p = int(pdms[0])

    d = int(pdms[1])

    m = int(pdms[2])

    s = int(pdms[3])

    answer = howManyGames(p, d, m, s)

    fptr.write(str(answer) + '\n')

    fptr.close()
