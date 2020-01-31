#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    pmsg = ['No', 'Yes']
    slen = len(s)
    tlen = len(t)
    continuous = 1
    same = 0

    for i in range(slen+tlen):
        if i < slen and i < tlen and continuous and (s[i] == t[i]):
            same += 1
        else:
            break

    poplen = slen - same
    appendlen = tlen - same

    if (poplen + appendlen) == k:
        return pmsg[1]

    elif (poplen + appendlen) > k:
        return pmsg[0]

    elif poplen == 0 and appendlen == 0:
        if (slen+tlen) <= k:
            return pmsg[1]

        else:
            if k % 2 == 0:
                return pmsg[1]
            else:
                return pmsg[0]

    elif poplen > appendlen:
        tk = k - poplen
        if tk % 2 == 0:
            return pmsg[1]
        else:
            tk = tk - tlen
            if tk % 2 == 0:
                return pmsg[1]
            return pmsg[0]

    elif appendlen > poplen:
        tk = k - appendlen
        if tk % 2 == 0:
            return pmsg[1]
        else:
            return pmsg[0]

    elif (poplen + appendlen) < k:
        return pmsg[1]

    else:
        return pmsg[0]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
