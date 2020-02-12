#!/usr/bin/env python3
import sys

k = int(sys.stdin.readline())
w = 2*k-1

for i in range(1, k+1):
    line = ''
    if i == k:
        line = w*'*'

    else:
        pad = (k-i)*' '
        mid = (i == 1) and '*' or '*%s*' % ((2*i-3)*' ')
        line = pad + mid + pad

    print(line)
