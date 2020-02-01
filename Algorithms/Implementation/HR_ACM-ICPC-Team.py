#!/bin/python3

import math
import os
import random
import re
import sys


def acmTeam(topic):
    res = [0, 0]
    n = len(topic)

    for i in range(n):
        for j in range(i+1, n):
            v = str(bin(int(topic[i], 2) | int(topic[j], 2))).count('1')
            if v > res[0]:
                res[0] = v
                res[1] = 1
            elif v == res[0]:
                res[1] += 1

    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
