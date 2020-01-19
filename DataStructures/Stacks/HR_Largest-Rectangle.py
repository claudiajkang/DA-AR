#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the largestRectangle function below.
def largestRectangle(_h):
    heights = sorted(list(set(_h)), reverse=True)
    total_idx = len(_h) - 1
    curr_level = 0
    max_size = 0
    rects = dict()

    for idx, val in enumerate(_h):
        if val not in rects.keys():
            rects[val] = list()

        rects[val].append(idx)

    def lookup_idx_exist(idx):
        upper_level = heights[:curr_level + 1]
        found = False

        if upper_level:
            for lookup_h in upper_level:
                if idx in rects[lookup_h]:
                    found = True
                    return found

        return found

    def lower(i):
        lower_idx = i - 1
        if lower_idx >= 0:
            if lookup_idx_exist(lower_idx):
                return lower(lower_idx)
        return i

    def higher(i):
        higher_idx = i + 1
        if higher_idx <= total_idx:
            if lookup_idx_exist(higher_idx):
                return higher(higher_idx)
        return i


    # Start indexing from top
    for h in heights:
        for i in rects[h]:
            curr_idx = i
            lower_idx = lower(curr_idx)
            higher_idx = higher(curr_idx)

            index_len = (higher_idx - lower_idx + 1)
            curr_size = index_len * h

            if max_size < curr_size:
                max_size = curr_size

        curr_level = curr_level + 1

    return max_size

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
