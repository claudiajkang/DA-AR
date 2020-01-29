# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    dates = dict()
    fixed = 256
    s = 0
    m = 0

    for i in range(1, 13):
        if i == 2:
            if year < 1918:
                if year % 4 == 0:
                    dates[i] = 29
                else:
                    dates[i] = 28
            elif year == 1918:
                dates[i] = (29-14)
            else:
                if year % 400 == 0:
                    dates[i] = 29
                elif (year % 4 == 0) and (year % 100 != 0):
                    dates[i] = 29
                else:
                    dates[i] = 28
        elif i in [1, 3, 5, 7, 8, 10, 12]:
            dates[i] = 31
        elif i in [4, 6, 9, 11]:
            dates[i] = 30

    for i in dates.keys():
        s += dates[i]
        if s > fixed:
            m = i
            s -= dates[i]
            break

    if s < fixed:
        d = fixed - s

    else:
        d = s

    if len(str(m)) == 1:
        m = str(0) + str(m)

    if len(str(d)) == 1:
        d = str(0) + str(d)

    pr = "{}.{}.{}".format(d, m, year)

    return pr


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
