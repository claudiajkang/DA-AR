#!/bin/python3

import os
import sys

def timeConversion(s):
    convt = s.split(":")

    if "PM" in convt[-1]:
        if convt[0] != "12":
            convt[0] = str(int(convt[0]) + 12)
        convt[-1] = convt[-1].replace("PM", "")

    elif "AM" in convt[-1]:
        if convt[0] == "12":
            convt[0] = str(abs(int(convt[0]) - 12))
        if len(convt[0]) == 1:
            convt[0] = str(0) + convt[0]
        convt[-1] = convt[-1].replace("AM", "")

    return ":".join(convt)


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
