#!/bin/python3

import math
import os
import random
import re
import sys


def circularArrayRotation(a, k, queries):
    rarray = list()
    tl = len(a)

    if k > tl:
        k %= tl

    for i in range(k):
        idx = tl - i - 1
        rarray.insert(0, a[idx])

    tr = rarray + a[:tl-k]
    res = list()

    for j in queries:
        res.append(tr[j])

    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nkq = input().split()

    n = int(nkq[0])

    k = int(nkq[1])

    q = int(nkq[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
