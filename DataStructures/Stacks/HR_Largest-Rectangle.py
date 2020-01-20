#!/bin/python3

import math
import os
import random
import re
import sys


def largestRectangle(_h):
    _h.insert(0, 0)
    _h.append(0)

    def get_ri(th):
        hstack = []
        ri = [0 for t in range(len(th))]
        for i in range(len(th)):
            if i > 0:
                for t in range(len(hstack)):
                    if hstack[-1]['h'] > h[i]:
                        v = hstack.pop()
                        ti = v['i']
                        ri[ti] = i

            tv = {'i': i, 'h': h[i]}
            hstack.append(tv)
        return ri

    def get_li(th):
        hstack = []
        li = [0 for t in range(len(th))]
        for i in range(len(th)-1,-1,-1):
            if i > 0:
                for t in range(len(hstack)):
                    if hstack[-1]['h'] > h[i]:
                        v = hstack.pop()
                        ti = v['i']
                        li[ti] = i

            tv = {'i': i, 'h': h[i]}
            hstack.append(tv)
        return li

    def get_s(ri, li, th):
        w = [0 for t in range(len(th))]
        s = [0 for t in range(len(th))]
        for i in range(len(th)):
            w[i] = ri[i] - li[i] - 1
            s[i] = w[i] * h[i]
        return s

    ri = get_ri(_h)
    li = get_li(_h)
    s = get_s(ri, li, _h)

    return max(s)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
