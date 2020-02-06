import sys

while True:
    res = sum(list(map(int, sys.stdin.readline().split())))
    if res == 0:
        break
    print(res)