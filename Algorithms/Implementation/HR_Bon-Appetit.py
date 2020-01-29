#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    bactual = 0

    for i, v in enumerate(bill):
        if i != k:
            bactual += v

    bactual = int(bactual / 2)

    if bactual == b:
        print("Bon Appetit")

    else:
        print(b - bactual)


if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
