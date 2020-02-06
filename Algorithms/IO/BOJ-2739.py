import sys

N = int(sys.stdin.readline())

for i in range(9):
    pr = "{} * {} = {}".format(str(N), str(i+1),str(N*(i+1)))
    print(pr)
