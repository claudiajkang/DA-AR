#!/bin/python3

import os
import sys


def twoStacks(x, a, b):
    ta = []
    tas = 0
    tb = []
    tbs = 0
    s = 0
    res = []

    for tav in a:
        if tav == 0:
            ta.append(tav)
        elif tas >= x:
            break
        else:
            ta.append(tav)
            tas += tav

    if tas > x:
        v = ta.pop(0)

    for tbv in b:
        if tbv == 0:
            tb.append(tbv)
        elif tbs >= x:
            break
        else:
            tb.append(tbv)
            tbs += tbv

    if tbs > x:
        v = tb.pop(0)

    while s <= x:
        if (len(a) == 0) and (len(b) == 0):
            break
        elif (len(a) > 0) and (len(b) > 0):
            if a[0] == 0:
                v = a.pop(0)
            elif b[0] == 0:
                v = b.pop(0)
            elif a[0] > b[0]:
                v = b.pop(0)
            elif a[0] < b[0]:
                v = a.pop(0)
            else:
                if len(a) > 2 and len(b) > 2:
                    tv = ''
                    for i in range(len(a)):
                        if a[i] > b[i]:
                            tv = 'b'
                            break
                        elif a[i] < b[i]:
                            tv = 'a'
                            break

                    if tv == 'a':
                        v = a.pop(0)
                    elif tv == 'b':
                        v = b.pop(0)
                else:
                    v = a.pop(0)

        elif (len(a) > 0) and (len(b) == 0):
            v = a.pop(0)
        elif (len(b) > 0) and (len(a) == 0):
            v = b.pop(0)

        res.append(v)
        s += v

    if s > x:
        s -= res.pop()

    t = [len(ta), len(tb), len(res)]

    t.sort(reverse=True)

    return t[0]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        nmx = input().split()

        n = int(nmx[0])

        m = int(nmx[1])

        x = int(nmx[2])

        a = list(map(int, input().rstrip().split()))

        b = list(map(int, input().rstrip().split()))

        result = twoStacks(x, a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
