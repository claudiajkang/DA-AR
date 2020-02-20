#!/bin/python3

import math
import os
import random
import re
import sys


def dynamicArray(n, queries):
    # Write your code here
    seq = [[] for i in range(n)]
    lastAnswer = 0
    res = []

    for i in queries:
        q, x, y = i[0], i[1], i[2]

        v = (x ^ lastAnswer) % n
        if q == 1:
            seq[v].append(y)

        elif q == 2:
            idx = y % len(seq[v])
            lastAnswer = seq[v][idx]
            res.append(str(lastAnswer))

    return res


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    print('\n'.join(result))

