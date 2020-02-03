#!/bin/python3

import math
import os
import random
import re
import sys

def cavityMap(grid):
    res = list()
    glen = len(grid)

    for g in range(glen):
        res.append(str(grid[g]))

    for i in range(1, glen-1):
        for j in range(1, glen-1):
            v = res[i][j]
            c = 0

            if (v > res[i-1][j]) and (v > res[i+1][j]):
                c += 1

            if (v > res[i][j-1]) and (v > res[i][j+1]):
                c += 1

            if c == 2:
                results = str(res[i][0:j]) + 'X' + str(res[i][j+1:])
                res[i] = results

    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
