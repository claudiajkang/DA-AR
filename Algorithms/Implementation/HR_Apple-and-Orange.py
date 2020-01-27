
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    apoint = []
    opoint = []
    ares = 0
    ores = 0

    for i in apples:
        apoint.append(a+i)

    for j in oranges:
        opoint.append(b+j)

    for k in apoint:
        if s <= k <= t:
            ares += 1

    for h in opoint:
        if s <= h <= t:
            ores += 1

    print(ares)
    print(ores)

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
