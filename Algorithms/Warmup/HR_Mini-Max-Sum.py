#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    res = [0 for i in range(len(arr))]

    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == j:
                continue
            else:
                res[j] += arr[i]

    print(min(res), end = ' ')
    print(max(res), end = ' ')

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
