import sys

N = int(sys.stdin.readline())
v = list(sys.stdin.readline().replace('\n',''))
res = sum(map(int, v))
print(res)
