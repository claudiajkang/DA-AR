#!/bin/python3

import os
import sys


#
# Complete the equalStacks function below.
#
def equalStacks(h1, h2, h3):
    lh1 = sum(h1, 0)
    lh2 = sum(h2, 0)
    lh3 = sum(h3, 0)

    while True:
        if lh1 >= lh2:
            if lh2 >= lh3:
                min = lh3
            else:
                min = lh2
        else:
            if lh1 >= lh3:
                min = lh3
            else:
                min = lh1

        if min < lh1:
            n1 = h1.pop(0)
            lh1 = sum(h1, 0)


        if min < lh2:
            n2 = h2.pop(0)
            lh2 = sum(h2, 0)

        if min < lh3:
            n3 = h3.pop(0)
            lh3 = sum(h3, 0)

        if lh1 is lh2 and lh2 is lh3:
            break

    return lh1


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n1N2N3 = input().split()

    n1 = int(n1N2N3[0])

    n2 = int(n1N2N3[1])

    n3 = int(n1N2N3[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
