#!/bin/python3

import math
import os
import random
import re
import sys


def happyLadybugs(b):
    if b.count('_') == 0:
        if len(b) == 1:
            return "NO"

        if len(b) > 1 and len(set(list(b))) == 1:
            return "YES"

        fres = list()
        rcheck = dict()
        ALPABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        for idx, val in enumerate(b):
            if val == '_':
                continue
            if val in ALPABET:
                if val not in rcheck.keys():
                    rcheck[val] = list()
                rcheck[val].append(idx)
            else:
                return "YES"

        for i in rcheck.keys():
            c = 0
            tttv = rcheck[i]
            if len(tttv) == 1:
                c = 1
                fres.append(c)
                continue

            for j in range(len(tttv) - 1):
                if abs(tttv[j] - tttv[j + 1]) != 1:
                    c = 1

            fres.append(c)

        if sum(fres) > 0:
            return "NO"

        return "YES"

    def rearrange(s, e, tempv):
        for j in range(s, e):
            temp = tempv[j]
            tempv[j] = tempv[v]
            tempv[v] = temp

        return tempv

    bl = list(b)
    vs = dict()

    for idx, val in enumerate(bl):
        if val not in vs.keys():
            vs[val] = list()

        vs[val].append(idx)

    for k in vs.keys():
        if k == '_':
            continue
        if len(vs[k]) == 1:
            return "NO"

    cidx = vs['_']

    for i in range(len(bl)):
        try:
            v = cidx.pop(0)
            if (bl[i] != bl[i+1]) and (bl[i+1] != '_'):
                tv = bl[i]

                if (i > 0) and (bl[i-1] == bl[i]):
                    cidx.append(v)
                    continue

                bl = rearrange(i + 1, v, bl)

                v = i+1
                tidx = bl[i+1:].index(tv) + i + 1

                if tidx != i:
                    temp = bl[tidx]
                    bl[tidx] = bl[v]
                    bl[v] = temp

                    vs[tv].append(v)
                    cidx.append(tidx)
                else:
                    vs.pop(tv)
                    cidx.append(v)

        except IndexError:
            break
        except ValueError:
            continue


    rcheck = dict()
    ALPABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for idx, val in enumerate(b):
        if val == '_':
            continue
        if val in ALPABET:
            if val not in rcheck.keys():
                rcheck[val] = list()
            rcheck[val].append(idx)

    fres = list()

    for i in rcheck.keys():
        if i == '_':
            continue
        c = 0
        if len(i) == 1:
            c = 1
            continue

        for j in range(len(i)-1):
            if abs(i[j]-i[j-1]) != 1:
                c = 1

        fres.append(c)

    if sum(fres) > 0:
        return "NO"

    return "YES"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        n = int(input())

        b = input()

        result = happyLadybugs(b)

        fptr.write(result + '\n')

    fptr.close()
